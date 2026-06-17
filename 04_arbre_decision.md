# Chapitre 6 : Arbre de décision simple

## 1. Objectif du chapitre

Un arbre de décision est un modèle de classification qui pose une suite de questions.

Chaque question coupe les données en deux groupes.

Exemples :

```text
âge <= 22 ?
poids <= 80 ?
revenu <= 2000 ?
```

L'objectif est de séparer les classes le mieux possible.

Dans ce chapitre, on cherche à comprendre :

- comment un arbre choisit une question ;
- pourquoi il compare plusieurs variables ;
- pourquoi il cherche un bon seuil ;
- comment il classe une nouvelle observation.

---

## 2. Idée générale

Un arbre de décision fonctionne comme un questionnaire.

À chaque étape, il pose une question simple.

Exemple :

```text
poids <= 80 ?
```

Puis il envoie l'observation :

- à gauche si la réponse est oui ;
- à droite si la réponse est non.

Le modèle continue jusqu'à arriver à une décision.

---

## 3. Premier exemple : un découpage parfait

Prenons un exemple avec deux variables :

| Âge | Poids | Sport |
| --- | ----- | ----- |
| 18  | 65    | Oui   |
| 20  | 70    | Oui   |
| 22  | 75    | Oui   |
| 24  | 95    | Non   |
| 26  | 100   | Non   |
| 60  | 80    | Non   |

On veut prédire :

```text
Sport = Oui ou Non
```

à partir de :

```text
âge, poids
```

---

## 4. Chercher le premier découpage

L'algorithme teste des questions sur toutes les variables.

Par exemple :

```text
âge <= 22 ?
```

### Groupe gauche

Les personnes qui répondent oui :

```text
18  65  Oui
20  70  Oui
22  75  Oui
```

### Groupe droit

Les personnes qui répondent non :

```text
24  95   Non
26  100  Non
60  80   Non
```

On obtient :

```text
Gauche : 100 % Oui
Droite : 100 % Non
```

Ce découpage est parfait.

L'arbre choisit donc :

```text
âge <= 22 ?
```

On peut représenter l'arbre ainsi :

```text
âge <= 22 ?
│
├── Oui -> Sport
│
└── Non -> Pas sport
```

---

## 5. Dataset plus réaliste

En pratique, les données sont rarement aussi propres.

Prenons maintenant ce dataset :

| Âge | Poids | Sport |
| --- | ----- | ----- |
| 18  | 65    | Oui   |
| 20  | 70    | Oui   |
| 22  | 95    | Non   |
| 24  | 75    | Oui   |
| 26  | 100   | Non   |
| 60  | 80    | Non   |

Cette fois, la question :

```text
âge <= 22 ?
```

donne dans le groupe gauche :

```text
18  Oui
20  Oui
22  Non
```

Ce groupe contient :

```text
2 Oui
1 Non
```

Il n'est pas parfaitement pur.

---

## 6. Tester une autre variable

L'algorithme teste aussi des questions sur le poids.

Par exemple :

```text
poids <= 80 ?
```

### Groupe gauche

```text
65  Oui
70  Oui
75  Oui
80  Non
```

### Groupe droit

```text
95   Non
100  Non
```

On obtient :

```text
Gauche : 3 Oui / 1 Non
Droite : 2 Non / 0 Oui
```

Ce découpage est meilleur que le découpage précédent.

Le groupe droit est parfaitement pur :

```text
100 % Non
```

L'arbre peut donc choisir :

```text
poids <= 80 ?
```

Premier niveau :

```text
poids <= 80 ?
│
├── Oui
│
└── Non -> Pas sport
```

---

## 7. Continuer dans une branche

Dans la branche gauche, il reste encore une erreur :

```text
65  Oui
70  Oui
75  Oui
80  Non
```

L'arbre cherche alors une nouvelle question seulement dans cette branche.

Par exemple :

```text
âge <= 21 ?
```

Cela donne :

### Groupe gauche

```text
18  Oui
20  Oui
```

### Groupe droit

```text
24  Oui
60  Non
```

Ce n'est pas encore parfait, mais l'idée est importante :

```text
L'arbre découpe les données étape par étape.
```

À chaque niveau, il cherche la meilleure question disponible à cet instant.

---

## 8. Résultat final possible

Un arbre possible serait :

```text
poids <= 80 ?
│
├── Oui
│   │
│   └── âge <= 21 ?
│       ├── Oui -> Sport
│       └── Non -> Vérifier autre chose
│
└── Non -> Pas sport
```

Ce n'est pas le seul arbre possible.

Selon le critère utilisé, les seuils testés et les paramètres du modèle, l'arbre peut choisir une structure légèrement différente.

Mais le raisonnement reste le même :

```text
choisir une variable
choisir un seuil
séparer les classes
continuer dans les branches restantes
```

---

## 9. Classer une nouvelle personne

Nouvelle personne :

```text
âge = 25
poids = 90
```

On parcourt l'arbre depuis le haut.

Première question :

```text
poids <= 80 ?
```

Réponse :

```text
Non
```

On suit donc la branche droite :

```text
Pas sport
```

La prédiction est :

```text
Sport = Non
```

---

## 10. Ce que l'arbre cherche vraiment

Avec plusieurs variables, l'arbre ne cherche pas seulement :

```text
Quel est le meilleur âge ?
```

Il cherche :

```text
Quelle variable ?
Quel seuil ?
```

Par exemple :

```text
âge <= 22 ?
poids <= 80 ?
revenu <= 2000 ?
```

Puis il choisit la question qui sépare le mieux les classes à cet instant.

C'est ce qui rend les arbres puissants :

```text
ils choisissent automatiquement la variable la plus pertinente à chaque niveau.
```

---

## 11. Vocabulaire important

| Mot | Signification |
| --- | ------------- |
| Noeud | endroit où l'arbre pose une question |
| Branche | chemin suivi selon la réponse |
| Feuille | décision finale |
| Seuil | valeur utilisée pour couper une variable numérique |
| Pureté | mesure du mélange des classes dans un groupe |

Un groupe est pur s'il contient une seule classe.

Exemple :

```text
Oui, Oui, Oui -> groupe pur
Oui, Oui, Non -> groupe moins pur
```

---

## 12. Avantages et limites

Avantages :

- facile à comprendre ;
- facile à expliquer ;
- fonctionne avec plusieurs variables ;
- choisit automatiquement les variables utiles ;
- peut modéliser des règles non linéaires.

Limites :

- peut apprendre trop précisément les données d'entraînement ;
- peut devenir instable si les données changent un peu ;
- peut créer un arbre trop complexe ;
- nécessite souvent de contrôler la profondeur.

Pour limiter ces problèmes, on peut régler par exemple :

```text
max_depth
min_samples_leaf
min_samples_split
```

---

## 13. Exemple avec Scikit-Learn

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    "age": [18, 20, 22, 24, 26, 60],
    "poids": [65, 70, 95, 75, 100, 80],
    "sport": ["Oui", "Oui", "Non", "Oui", "Non", "Non"]
})

X = df[["age", "poids"]]
y = df["sport"]

modele = DecisionTreeClassifier(max_depth=2, random_state=42)
modele.fit(X, y)

nouvelle_personne = pd.DataFrame({
    "age": [25],
    "poids": [90]
})

prediction = modele.predict(nouvelle_personne)

print(prediction)
```

---

## 14. À retenir

Un arbre de décision classe une observation en posant une suite de questions.

À chaque étape, il choisit :

```text
la variable et le seuil qui séparent le mieux les classes.
```

Contrairement à KNN, il ne compare pas la nouvelle observation à tous les exemples.

Contrairement à la régression logistique, il ne transforme pas un score linéaire en probabilité.

Il apprend une structure de décisions :

```text
si condition
alors branche gauche
sinon branche droite
```

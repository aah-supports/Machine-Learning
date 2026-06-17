# Chapitre 6 : Arbre de décision avec `load_wine`

## 1. Objectif du chapitre

Un arbre de décision est un modèle de classification qui apprend une suite de questions.

Chaque question ressemble à :

```text
variable <= seuil ?
```

Exemples :

```text
alcohol <= 13.0 ?
color_intensity <= 3.8 ?
flavanoids <= 1.6 ?
```

Dans ce chapitre, on utilise le dataset classique `load_wine` de Scikit-Learn.

Objectifs :

- comprendre comment un arbre choisit une variable et un seuil ;
- comprendre la notion de pureté ;
- entraîner un `DecisionTreeClassifier` ;
- lire l'arbre obtenu ;
- comprendre le risque de surapprentissage ;
- savoir quels paramètres régler.

---

## 2. Intuition rapide

Un arbre fonctionne comme un questionnaire.

Pour classer une observation, il pose une première question.

Exemple très simple :

```text
poids <= 80 ?
```

Si oui, on part à gauche.

Si non, on part à droite.

Puis l'arbre pose une autre question dans la branche où l'on se trouve.

À la fin, on arrive à une feuille :

```text
classe prédite
```

---

## 3. Exemple minimal avec deux variables

Prenons un petit dataset artificiel :

| Âge | Poids | Sport |
| --- | ----- | ----- |
| 18  | 65    | Oui   |
| 20  | 70    | Oui   |
| 22  | 95    | Non   |
| 24  | 75    | Oui   |
| 26  | 100   | Non   |
| 60  | 80    | Non   |

L'arbre teste plusieurs questions :

```text
âge <= 22 ?
poids <= 80 ?
```

Il ne cherche pas une question "jolie" ou intuitive.

Il cherche une question qui rend les groupes obtenus les plus homogènes possible.

Un groupe homogène, ou presque pur, contient surtout une seule classe.

Exemple de groupe pur :

```text
Non, Non, Non
```

Exemple de groupe impur :

```text
Oui, Non, Oui
```

Dans un groupe impur, les classes sont mélangées. L'arbre devra donc continuer à poser des questions.

La question :

```text
poids <= 80 ?
```

donne :

```text
Gauche : 3 Oui / 1 Non
Droite : 2 Non / 0 Oui
```

La branche droite est pure :

```text
100 % Non
```

La branche gauche n'est pas totalement pure, mais elle est déjà assez homogène :

```text
3 Oui
1 Non
```

L'arbre préfère ce découpage parce qu'il isole très bien les exemples `Non` les plus lourds.

L'arbre peut donc commencer par :

```text
poids <= 80 ?
│
├── Oui -> continuer à découper
│
└── Non -> Pas sport
```

L'idée importante :

```text
L'arbre ne choisit pas seulement une variable.
Il choisit une variable ET un seuil.
```

---

## 4. Dataset `load_wine`

`load_wine` est un dataset classique de Scikit-Learn.

Il contient des mesures chimiques sur des vins.

Objectif :

```text
Prédire le type de vin.
```

La cible contient trois classes :

```text
0, 1, 2
```

Chaque ligne représente un vin.

Chaque colonne représente une mesure :

- taux d'alcool ;
- acide malique ;
- alcalinité ;
- magnésium ;
- flavonoïdes ;
- intensité de couleur ;
- proline ;
- etc.

---

## 5. Charger les données

```python
import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name="target")

X.head()
```

Afficher les classes :

```python
wine.target_names
```

Afficher les dimensions :

```python
print(X.shape)
print(y.shape)
```

---

## 6. Ce que voit l'arbre

L'arbre ne voit pas directement :

```text
un vin rouge
un vin blanc
une intuition humaine
```

Il voit un tableau de nombres :

| alcohol | malic_acid | flavanoids | color_intensity | proline | target |
| ------- | ---------- | ---------- | --------------- | ------- | ------ |
| 14.23   | 1.71       | 3.06       | 5.64            | 1065    | 0      |
| 13.20   | 1.78       | 2.76       | 4.38            | 1050    | 0      |

À partir de ces nombres, il teste des questions comme :

```text
proline <= 755 ?
flavanoids <= 1.58 ?
color_intensity <= 3.82 ?
```

---

## 7. Séparer train et test

Comme pour KNN et la régression logistique, on sépare les données.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

Pourquoi `stratify=y` ?

Parce qu'on veut garder à peu près la même proportion de classes dans le train et dans le test.

---

## 8. Entraîner un arbre

```python
from sklearn.tree import DecisionTreeClassifier

modele = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

modele.fit(X_train, y_train)
```

Ici :

- `max_depth=3` limite la profondeur de l'arbre ;
- `random_state=42` rend l'expérience reproductible.

---

## 9. Évaluer le modèle

```python
score_train = modele.score(X_train, y_train)
score_test = modele.score(X_test, y_test)

print("Score train :", score_train)
print("Score test  :", score_test)
```

En classification, `score` correspond généralement à l'accuracy.

```text
accuracy = proportion de prédictions correctes
```

Il faut comparer train et test :

| Situation | Interprétation |
| --------- | -------------- |
| train élevé, test élevé | modèle correct |
| train très élevé, test faible | surapprentissage |
| train faible, test faible | modèle trop simple ou variables insuffisantes |

---

## 10. Lire un arbre

On peut afficher l'arbre sous forme de règles :

```python
from sklearn.tree import export_text

texte_arbre = export_text(
    modele,
    feature_names=list(X.columns)
)

print(texte_arbre)
```

Exemple de sortie possible :

```text
|--- proline <= 755.00
|   |--- flavanoids <= 1.58
|   |   |--- class: 2
|   |--- flavanoids >  1.58
|   |   |--- class: 1
|--- proline >  755.00
|   |--- class: 0
```

Lecture :

```text
Si proline <= 755, on va à gauche.
Sinon, on va à droite.
```

Puis l'arbre continue avec d'autres questions.

---

## 11. Visualiser l'arbre

```python
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(16, 8))

plot_tree(
    modele,
    feature_names=X.columns,
    class_names=wine.target_names,
    filled=True,
    rounded=True
)

plt.show()
```

Chaque noeud affiche :

- la question posée ;
- le critère de pureté ;
- le nombre d'exemples dans le noeud ;
- la répartition des classes ;
- la classe prédite.

---

## 12. Pureté : l'idée centrale

Un arbre cherche à créer des groupes les plus purs possibles.

Un groupe pur contient une seule classe, ou presque une seule classe.

Exemple :

```text
Classe 0, Classe 0, Classe 0
```

Groupe impur :

```text
Classe 0, Classe 1, Classe 2
```

À chaque découpage, l'arbre cherche une question qui réduit le mélange des classes.

On peut résumer ainsi :

```text
avant la question :
classes mélangées

après une bonne question :
groupes plus homogènes
```

Ce n'est donc pas seulement :

```text
trouver une règle qui marche sur un exemple
```

C'est plutôt :

```text
trouver la coupure qui organise le mieux tout le groupe d'exemples à cet endroit de l'arbre.
```

Scikit-Learn utilise par défaut le critère `gini`.

```python
DecisionTreeClassifier(criterion="gini")
```

On peut aussi utiliser l'entropie :

```python
DecisionTreeClassifier(criterion="entropy")
```

Pour ce cours, il faut retenir l'intuition :

```text
meilleur découpage = groupes plus purs
```

---

## 13. Surapprentissage

Un arbre peut devenir trop précis.

Si on ne limite pas sa profondeur, il peut apprendre des détails très spécifiques du train.

Exemple :

```python
arbre_libre = DecisionTreeClassifier(random_state=42)
arbre_libre.fit(X_train, y_train)

print(arbre_libre.score(X_train, y_train))
print(arbre_libre.score(X_test, y_test))
```

On peut obtenir :

```text
Score train très proche de 1
Score test plus faible
```

Cela signifie :

```text
Le modèle connaît très bien le train,
mais il généralise moins bien.
```

C'est le surapprentissage.

---

## 14. Paramètres importants

| Paramètre | Rôle |
| --------- | ---- |
| `max_depth` | limite la profondeur de l'arbre |
| `min_samples_split` | nombre minimum d'exemples pour diviser un noeud |
| `min_samples_leaf` | nombre minimum d'exemples dans une feuille |
| `criterion` | mesure utilisée pour choisir les découpages |
| `random_state` | rend les résultats reproductibles |

Exemple :

```python
modele = DecisionTreeClassifier(
    max_depth=3,
    min_samples_leaf=5,
    random_state=42
)
```

---

## 15. Importance des variables

Un arbre peut indiquer quelles variables ont été les plus utilisées.

```python
importances = pd.Series(
    modele.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

importances.head(10)
```

Attention :

```text
importance élevée ne signifie pas causalité.
```

Cela signifie seulement :

```text
la variable a été utile pour les découpages de cet arbre.
```

---

## 16. Avantages et limites

Avantages :

- très interprétable ;
- fonctionne avec des relations non linéaires ;
- demande peu de préparation des variables numériques ;
- ne nécessite pas forcément de normalisation ;
- donne des règles lisibles.

Limites :

- peut surapprendre ;
- peut être instable ;
- peut créer des règles trop spécifiques ;
- une petite variation des données peut changer l'arbre.

---

## 17. Ouverture : pourquoi Random Forest ?

Un arbre seul est très lisible.

Mais il peut être instable :

```text
petit changement dans les données
-> arbre différent
-> règles différentes
```

Random Forest répond à cette limite avec une idée simple :

```text
entraîner plusieurs arbres
puis faire voter les arbres
```

Exemple :

```text
arbre 1 -> classe 0
arbre 2 -> classe 1
arbre 3 -> classe 0
arbre 4 -> classe 0
arbre 5 -> classe 1
```

Vote majoritaire :

```text
classe 0
```

On utilise souvent une Random Forest quand :

- un arbre seul est trop instable ;
- on veut améliorer la performance ;
- on accepte de perdre un peu en lisibilité ;
- on veut un modèle robuste sans trop de préparation des variables.

Ce sera une suite naturelle après les arbres de décision.

---

## 18. Exercice

Exercice à faire :

- [Énoncé : arbre simple âge, poids et sport](04_arbre_decision/Exercices/02_arbre_sport_simple.md)
- [Énoncé : arbre de décision avec `load_wine`](04_arbre_decision/Exercices/01_load_wine_arbre_decision.md)
- [Correction : arbre de décision avec `load_wine`](04_arbre_decision/Corrections/01_load_wine_arbre_decision_correction.md)

---

## 19. À retenir

Un arbre de décision apprend une suite de règles.

Chaque règle a la forme :

```text
variable <= seuil ?
```

L'arbre choisit la variable et le seuil qui rendent les groupes les plus purs.

Sur `load_wine`, il peut apprendre des règles du type :

```text
proline <= 755 ?
flavanoids <= 1.58 ?
color_intensity <= 3.82 ?
```

Un arbre est facile à expliquer, mais il faut limiter sa complexité pour éviter le surapprentissage.

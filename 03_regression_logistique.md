# Chapitre 5 : Introduction à la régression logistique

## 1. Objectif du chapitre

Après KNN, nous avons vu une première manière de faire de la classification :

```text
chercher les voisins les plus proches
puis voter
```

La régression logistique propose une autre approche.

Elle ne vote pas avec des voisins.

Elle apprend une formule qui transforme les variables en probabilité.

Objectifs :

- comprendre pourquoi la régression logistique sert à la classification ;
- partir d'une combinaison linéaire comme en régression linéaire ;
- comprendre le rôle de la fonction sigmoïde ;
- interpréter une probabilité entre 0 et 1 ;
- comprendre le seuil de décision à `0.5` ;
- préparer le passage vers le perceptron.

---

## 2. Le problème : prédire une classe

Imaginons un étudiant.

On veut prédire s'il valide un module.

Variables possibles :

- nombre d'heures de révision ;
- taux de présence ;
- nombre d'exercices rendus.

La réponse n'est pas un prix ou une température.

La réponse est une classe :

```text
0 = ne valide pas
1 = valide
```

On est donc dans un problème de classification.

---

## 3. Point de départ : un score linéaire

La régression logistique ne prédit pas directement la classe au départ.

Elle calcule d'abord un score appelé `z`.

Ce score est obtenu avec une addition pondérée des variables :

```text
z = w1 * x1 + w2 * x2 + ... + b
```

Avec :

- `x1`, `x2` : les variables ;
- `w1`, `w2` : les poids appris par le modèle ;
- `b` : le biais ;
- `z` : un score linéaire.

Exemple avec une seule variable, les heures de révision :

```text
z = w * heures + b
```

Supposons que le modèle ait appris :

```text
z = 2 * heures - 6
```

On obtient :

| Heures de révision | Calcul          | z  |
| ------------------ | --------------- | -- |
| 2                  | `2 * 2 - 6`     | -2 |
| 3                  | `2 * 3 - 6`     | 0  |
| 5                  | `2 * 5 - 6`     | 4  |

À ce stade :

- `z` n'est pas une classe ;
- `z` n'est pas une probabilité ;
- `z` est seulement un score.

Le score mesure à quel point le modèle penche vers la classe `1` ou vers la classe `0`.

| z   | Interprétation      |
| --- | ------------------- |
| -10 | quasiment classe 0  |
| -1  | plutôt classe 0     |
| 0   | hésitation          |
| 1   | plutôt classe 1     |
| 10  | quasiment classe 1  |

---

## 4. Pourquoi ne pas utiliser directement le score ?

Le score `z` peut prendre n'importe quelle valeur.

Exemple :

```text
z = -3.2
z = 0.2
z = 2.8
z = 7.5
```

Ces valeurs sont utiles pour situer l'exemple par rapport à la frontière.

Mais elles ne sont pas des probabilités.

Une probabilité doit toujours être comprise entre :

```text
0 et 1
```

Donc il faut transformer le score linéaire.

---

## 5. La fonction sigmoïde

La régression logistique applique une fonction sigmoïde au score `z`.

Formule :

```text
p = 1 / (1 + e^(-z))
```

La sigmoïde écrase les valeurs :

| z  | sigmoïde(z) |
| -- | ----------- |
| -4 | 0.018       |
| -2 | 0.119       |
| 0  | 0.5         |
| 2  | 0.881       |
| 4  | 0.982       |

Le résultat `p` peut être interprété comme une probabilité.

Avec l'exemple précédent :

| Heures | z  | Probabilité environ |
| ------ | -- | ------------------- |
| 2      | -2 | 11.9 %              |
| 3      | 0  | 50 %                |
| 5      | 4  | 98.2 %              |

Le modèle ne dit donc pas :

```text
5 heures -> réussite certaine
```

Il dit plutôt :

```text
Avec ce que j'ai appris, 5 heures donnent une probabilité de réussite très élevée.
```

---

## 6. Intuition avec les heures de révision

Imaginons que l'on prédise la validation d'un module.

```text
0 h   -> presque aucune chance de réussir
2 h   -> faible chance
4 h   -> situation incertaine
6 h   -> forte chance
10 h  -> presque certain
```

On ne passe pas brutalement de `0` à `1`.

La transition est progressive.

La sigmoïde produit exactement cette forme en S :

```text
Probabilité

1.0 |                     *********
    |                 ****
0.5 |-------------****
    |         ****
0.0 |********
    +-------------------------
         heures de révision
```

---

## 7. Pourquoi le point central vaut 0.5 ?

Lorsque :

```text
z = 0
```

on obtient :

```text
p = 1 / (1 + e^0)
```

Comme :

```text
e^0 = 1
```

alors :

```text
p = 1 / 2
p = 0.5
```

`0.5` est la frontière de décision la plus classique.

Règle simple :

```text
si p >= 0.5 -> classe 1
si p < 0.5  -> classe 0
```

---

## 8. L'idée géométrique

La régression logistique cherche une frontière qui sépare les classes.

Avec deux variables, cette séparation peut être représentée par une droite.

Avec plus de variables, on parle d'hyperplan.

Attention : la régression logistique n'est pas une régression linéaire qui prédirait un prix ou une quantité.

Elle utilise une formule linéaire pour calculer un score `z`.

Ce score indique de quel côté de la frontière se trouve l'exemple, et à quelle distance.

```text
loin côté classe 0 -> z très négatif -> probabilité proche de 0
sur la frontière   -> z = 0          -> probabilité = 0.5
loin côté classe 1 -> z très positif -> probabilité proche de 1
```

La différence avec la régression linéaire est donc l'objectif :

```text
Régression linéaire :
surface -> prix prédit
sortie possible : 280000

Régression logistique :
heures, présence -> score z
z négatif -> plutôt classe 0
z positif -> plutôt classe 1
```

Ensuite seulement, la sigmoïde transforme ce score en probabilité :

```text
score z -> sigmoïde -> probabilité entre 0 et 1
```

Exemple :

```text
p = 0.82
```

Cela signifie que le modèle estime une forte probabilité pour la classe `1`.

Puis on applique un seuil :

```text
si p >= 0.5 -> classe 1
si p < 0.5  -> classe 0
```

C'est pour cela qu'elle est souvent enseignée après la régression linéaire : elle garde l'idée d'une formule avec des poids et un biais, mais elle l'utilise pour classifier.

---

## 9. Lien avec KNN

KNN et la régression logistique peuvent tous les deux faire de la classification.

Mais ils ne raisonnent pas de la même manière.

| Modèle | Idée principale |
| ------ | --------------- |
| KNN | comparer aux voisins les plus proches |
| Régression logistique | apprendre une séparation et produire une probabilité |

KNN garde les exemples.

La régression logistique apprend des paramètres :

```text
w1, w2, ..., b
```

---

## 10. Transition vers le perceptron

Le perceptron utilise une idée très proche :

```text
z = w1 * x1 + w2 * x2 + b
p = sigmoid(z)
```

Puis il corrige les poids quand la prédiction est mauvaise.

La régression logistique prépare donc naturellement le passage vers :

- les poids ;
- le biais ;
- la sigmoïde ;
- la descente de gradient ;
- les réseaux de neurones.

---

## 11. Mini-exercice : prédire une validation

On dispose d'un petit dataset d'étudiants.

Le dataset n'est pas parfaitement séparé : certains cas sont limites. C'est volontaire, car une régression logistique est surtout utile quand on veut lire une probabilité, pas seulement une classe.

```python
import pandas as pd

df = pd.DataFrame({
    "heures_revision": [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 10],
    "presence": [35, 40, 55, 45, 50, 70, 55, 75, 65, 60, 85, 80, 90, 95],
    "controle_continu": [6, 7, 8, 7, 9, 10, 10, 12, 11, 10, 14, 13, 15, 16],
    "valide": [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
})
```

Objectif :

```text
Prédire si un étudiant valide le module.
```

### Étape 1 - Séparer X et y

Créer :

```python
X = df[["heures_revision", "presence", "controle_continu"]]
y = df["valide"]
```

### Étape 2 - Entraîner le modèle

On utilise un pipeline pour normaliser les variables avant la régression logistique.

Compléter les `...` :

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

modele = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

modele.fit(..., ...)
```

### Étape 3 - Tester deux nouveaux étudiants

On veut comparer deux profils.

| Profil | Heures | Présence | Contrôle continu |
| ------ | ------ | -------- | ---------------- |
| A      | 4      | 60       | 9                |
| B      | 8      | 85       | 14               |

Compléter :

```python
nouveaux_etudiants = pd.DataFrame({
    "heures_revision": [4, 8],
    "presence": [60, 85],
    "controle_continu": [9, 14]
})

classes = ...
probabilites = ...
```

### Étape 4 - Lire les probabilités

`predict_proba` renvoie une probabilité pour chaque classe.

Afficher les classes dans l'ordre utilisé par le modèle :

```python
modele.classes_
```

Puis construire un tableau lisible :

```python
resultats = pd.DataFrame(
    probabilites,
    columns=[f"proba_classe_{c}" for c in modele.classes_]
)

resultats["classe_predite"] = classes
resultats
```

### Questions

1. Quelle classe est prédite pour le profil A ?
2. Quelle est la probabilité de validation du profil A ?
3. Quelle classe est prédite pour le profil B ?
4. Quelle est la probabilité de validation du profil B ?
5. Pourquoi le profil A peut-il être plus incertain que le profil B ?
6. Pourquoi `predict_proba` est-il plus informatif que `predict` ?

### Phrase attendue

Rédiger une phrase de ce type :

```text
Pour le profil ..., le modèle prédit la classe ... avec une probabilité de validation d'environ ... %.
```

---

## 12. Exercice pratique

Notebook :

- [Énoncé : régression logistique](notebooks/03_regression_logistique_enonce.ipynb)

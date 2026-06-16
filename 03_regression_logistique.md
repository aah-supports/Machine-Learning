# Chapitre 5 : Introduction à la régression logistique

## 1. Objectif du chapitre

Après KNN, nous avons vu une première manière de faire de la classification :

```text
chercher les voisins les plus proches
puis voter
```

La régression logistique propose une autre approche.

Elle ne vote pas avec des voisins.

Elle apprend une formule qui transforme les variables en probabilité, mais en passant par une idée intermédiaire importante : les **log-odds**.

Objectifs :

- comprendre pourquoi la régression logistique sert à la classification ;
- comprendre les odds, c'est-à-dire le rapport succès / échec ;
- comprendre pourquoi le modèle apprend une droite sur le log-odds ;
- comprendre pourquoi la sigmoïde apparaît ensuite ;
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

## 3. Point de départ : une probabilité

La régression logistique cherche d'abord une probabilité :

```text
p = P(Y = 1)
```

Dans notre exemple :

```text
Y = 1 -> l'étudiant valide
Y = 0 -> l'étudiant ne valide pas
```

Une probabilité doit toujours rester entre `0` et `1` :

```text
0 <= p <= 1
```

Le problème est qu'une droite peut produire n'importe quelle valeur :

```text
-3, 0.2, 4, 15, ...
```

On ne peut donc pas modéliser directement `p` avec une droite classique.

---

## 4. Les odds : rapport succès / échec

Au lieu de travailler directement avec `p`, on transforme la probabilité en **odds**.

Les odds comparent la chance de succès à la chance d'échec :

```text
odds = p / (1 - p)
```

Exemples :

| Probabilité p | Odds | Lecture |
| ------------- | ---- | ------- |
| 0.5 | 1 | autant de chances de réussir que d'échouer |
| 0.75 | 3 | 3 fois plus de chances de réussir que d'échouer |
| 0.9 | 9 | 9 fois plus de chances de réussir que d'échouer |
| 0.1 | 1/9 | 9 fois moins de chances de réussir que d'échouer |

Les odds sont utiles parce que beaucoup d'effets sont multiplicatifs.

Exemple :

```text
chaque heure de révision multiplie les odds par 2
```

| Heures | Odds |
| ------ | ---- |
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |

On voit que les odds peuvent augmenter très vite.

Ce n'est pas une droite : c'est une progression multiplicative.

---

## 5. Le log-odds : rendre la relation linéaire

Les odds vont de `0` à `+infini`.

Une droite, elle, peut aller de `-infini` à `+infini`.

Pour obtenir une quantité compatible avec une droite, on prend le logarithme des odds :

```text
log-odds = log(p / (1 - p))
```

Exemples :

| p | odds | log-odds |
| -- | ---- | -------- |
| 0.1 | 1/9 | -2.2 |
| 0.5 | 1 | 0 |
| 0.9 | 9 | 2.2 |

Le logarithme transforme une multiplication en addition.

Donc si les odds évoluent de manière multiplicative, le log-odds peut évoluer de manière presque linéaire.

---

## 6. L'hypothèse fondamentale

La régression logistique fait une hypothèse simple :

> Le log-odds est une fonction linéaire des variables.

Avec une variable :

```text
log(p / (1 - p)) = a * x + b
```

Avec plusieurs variables :

```text
log(p / (1 - p)) = w1 * x1 + w2 * x2 + ... + b
```

Cette ligne est le coeur du modèle.

La régression logistique ne dit pas :

```text
la probabilité est une droite
```

Elle dit :

```text
le logarithme du rapport succès / échec est une droite
```

---

## 7. D'où vient la sigmoïde ?

On part de l'hypothèse :

```text
log(p / (1 - p)) = z
```

où :

```text
z = w1 * x1 + w2 * x2 + ... + b
```

Si on résout cette équation pour retrouver `p`, on obtient :

```text
p = 1 / (1 + e^(-z))
```

C'est la fonction sigmoïde.

La sigmoïde n'est donc pas un choix arbitraire.

Elle apparaît parce qu'on veut repasser du log-odds à une probabilité.

Quelques valeurs :

| z | sigmoïde(z) |
| -- | ----------- |
| -4 | 0.018 |
| -2 | 0.119 |
| 0 | 0.5 |
| 2 | 0.881 |
| 4 | 0.982 |

---

## 8. Score, probabilité, classe

Le modèle suit donc cette chaîne :

```text
variables
-> score linéaire z
-> sigmoïde(z)
-> probabilité p
-> classe 0 ou 1
```

Exemple avec les heures de révision :

```text
z = 2 * heures - 6
```

| Heures | z | Probabilité environ |
| ------ | -- | ------------------- |
| 2 | -2 | 11.9 % |
| 3 | 0 | 50 % |
| 5 | 4 | 98.2 % |

Le modèle ne dit pas :

```text
5 heures -> réussite certaine
```

Il dit plutôt :

```text
Avec ce que j'ai appris, 5 heures donnent une probabilité de réussite très élevée.
```

Puis on applique un seuil :

```text
si p >= 0.5 -> classe 1
si p < 0.5  -> classe 0
```

---

## 9. Lien avec KNN

KNN et la régression logistique peuvent tous les deux faire de la classification.

Mais ils ne raisonnent pas de la même manière.

| Modèle | Idée principale |
| ------ | --------------- |
| KNN | comparer aux voisins les plus proches |
| Régression logistique | modéliser le log-odds, puis produire une probabilité |

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

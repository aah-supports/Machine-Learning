# Exercice 2 : entraîner une régression logistique avec Scikit-Learn

## Objectif

Entraîner une régression logistique sur un petit dataset d'étudiants, lire les probabilités et interpréter les prédictions.

On travaille sur une classification binaire :

```text
0 = ne valide pas
1 = valide
```

---

## Étape 1 - Créer le dataset

Exécuter le code suivant :

```python
import pandas as pd

df = pd.DataFrame({
    "heures_revision": [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 10],
    "presence": [35, 40, 55, 45, 50, 70, 55, 75, 65, 60, 85, 80, 90, 95],
    "controle_continu": [6, 7, 8, 7, 9, 10, 10, 12, 11, 10, 14, 13, 15, 16],
    "valide": [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
})

df
```

### Questions

1. Quelles sont les variables explicatives ?
2. Quelle est la variable cible ?
3. Pourquoi ce dataset contient-il des cas limites ?

---

## Étape 2 - Séparer X et y

Créer :

```python
X = df[["heures_revision", "presence", "controle_continu"]]
y = df["valide"]
```

### Question

Pourquoi `X` contient-il plusieurs colonnes alors que `y` ne contient qu'une seule colonne ?

---

## Étape 3 - Créer un pipeline

On utilise :

- `StandardScaler` pour mettre les variables à une échelle comparable ;
- `LogisticRegression` pour entraîner le modèle.

Compléter :

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

modele = make_pipeline(
    ...,
    ...
)

modele.fit(..., ...)
```

### Questions

1. Pourquoi normalise-t-on les variables ?
2. Quelle méthode entraîne le modèle ?
3. Le modèle prédit-il directement une probabilité ou une classe avec `predict` ?

---

## Étape 4 - Comparer trois profils

Créer :

```python
profils = pd.DataFrame({
    "heures_revision": [3, 5, 9],
    "presence": [50, 65, 90],
    "controle_continu": [8, 11, 15]
})
```

Puis calculer :

```python
classes = modele.predict(profils)
probabilites = modele.predict_proba(profils)
```

Afficher l'ordre des classes :

```python
modele.classes_
```

Construire un tableau de résultats :

```python
resultats = profils.copy()

resultats["proba_classe_0"] = probabilites[:, 0]
resultats["proba_classe_1"] = probabilites[:, 1]
resultats["classe_predite"] = classes

resultats
```

### Questions

1. Quel profil a la probabilité de validation la plus faible ?
2. Quel profil a la probabilité de validation la plus élevée ?
3. Quel profil est le plus incertain ?
4. Pourquoi `predict_proba` est-il plus intéressant que `predict` pour analyser un cas limite ?

---

## Étape 5 - Changer le seuil de décision

Avec le seuil classique :

```text
si p >= 0.5 -> classe 1
sinon       -> classe 0
```

Créer une nouvelle règle :

```text
si p >= 0.7 -> classe 1
sinon       -> classe 0
```

Compléter :

```python
proba_validation = probabilites[:, 1]

classe_seuil_07 = ...

resultats["classe_seuil_07"] = classe_seuil_07
resultats
```

### Questions finales

1. Qu'est-ce qui change quand le seuil passe de `0.5` à `0.7` ?
2. Dans quel contexte voudrait-on utiliser un seuil plus strict ?
3. Pourquoi la régression logistique est-elle utile pour prendre ce type de décision ?


# TP : Régression linéaire simple avec BMI

## Objectif

Construire une première régression linéaire avec Scikit-Learn pour prédire la progression du diabète à partir d'une seule variable médicale : l'IMC, appelé `bmi` dans le dataset.

Question centrale :

> Le BMI permet-il d'expliquer une partie de la progression du diabète ?

---

## Étape 1 - Charger le dataset

Importer :

```python
from sklearn.datasets import load_diabetes
import pandas as pd
```

Charger les données :

```python
data = load_diabetes(as_frame=True, scaled=False)

X = data.data
y = data.target
```

### Questions

1. Afficher les 5 premières lignes de `X`.
2. Afficher les 5 premières valeurs de `y`.
3. Combien d'observations contient le dataset ?
4. Combien de variables explicatives possède-t-il ?

---

## Étape 2 - Sélectionner la variable BMI

On ne garde qu'une seule variable explicative :

```python
X_bmi = X[["bmi"]]
```

### Questions

1. Pourquoi utilise-t-on deux crochets autour de `"bmi"` ?
2. Quelle est la variable utilisée pour prédire ?
3. Quelle est la valeur à prédire ?

---

## Étape 3 - Créer et entraîner le modèle

Importer :

```python
from sklearn.linear_model import LinearRegression
```

Créer le modèle :

```python
reg = LinearRegression()
```

Puis entraîner le modèle avec `X_bmi` et `y`.

### Questions

1. Quelle commande permet d'entraîner le modèle ?
2. Que signifie `.fit(X_bmi, y)` dans ce cas ?

---

## Étape 4 - Faire les prédictions

Utiliser le modèle entraîné pour prédire la progression du diabète :

```python
y_pred = ...
```

### Question

Que représentent les valeurs contenues dans `y_pred` ?

---

## Étape 5 - Préparer les données pour le graphique

Créer un DataFrame contenant :

- le BMI ;
- la progression réelle du diabète ;
- la prédiction du modèle.

Structure attendue :

```python
df = pd.DataFrame({
    "bmi": ...,
    "target": ...,
    "prediction": ...
}).sort_values("bmi")
```

### Questions

1. Pourquoi trie-t-on le DataFrame par `bmi` ?
2. Quelle colonne servira à tracer les points réels ?
3. Quelle colonne servira à tracer la droite de régression ?

---

## Étape 6 - Visualiser la droite de régression

Importer :

```python
import matplotlib.pyplot as plt
```

Tracer :

- un nuage de points avec `bmi` en abscisse et `target` en ordonnée ;
- une ligne avec `bmi` en abscisse et `prediction` en ordonnée.

Ajouter :

```python
plt.xlabel("BMI")
plt.ylabel("Progression du diabète")
plt.title("Régression linéaire : BMI -> Progression du diabète")
plt.show()
```

### Questions

1. Que représente chaque point ?
2. Que représente la droite ?
3. La droite monte-t-elle ou descend-elle quand le BMI augmente ?

---

## Étape 7 - Lire les résultats du modèle

Afficher :

```python
print("Pente :", ...)
print("Intercept :", ...)
print("R² :", ...)
```

### Questions

1. Comment accéder à la pente du modèle ?
2. Comment accéder à l'intercept ?
3. Comment calculer le score R² avec Scikit-Learn ?

---

## Étape 8 - Interpréter

Répondre avec des phrases courtes.

### Questions finales

1. Le BMI a-t-il une relation positive ou négative avec la progression du diabète ?
2. Que signifie une pente positive ?
3. Le BMI seul suffit-il à expliquer toute la progression du diabète ?
4. Que mesure le coefficient R² ?
5. Pourquoi faudra-t-il utiliser plusieurs variables pour améliorer le modèle ?


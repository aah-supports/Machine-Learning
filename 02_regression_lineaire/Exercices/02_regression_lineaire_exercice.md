# TP : Première régression avec Scikit-Learn

## Objectif

Construire un premier modèle de Machine Learning capable de prédire la progression d'un diabète à partir d'informations médicales.

---

# Étape 1 - Charger le dataset

```python
from sklearn.datasets import load_diabetes

data = load_diabetes(as_frame=True)

X = data.data
y = data.target
```

### Questions

1. Afficher les 5 premières lignes de `X`.
2. Afficher les 5 premières valeurs de `y`.
3. Combien d'observations contient le dataset ?
4. Combien de variables explicatives possède-t-il ?

---

# Étape 2 - Explorer les données

Afficher :

```python
X.info()
```

Puis :

```python
X.describe()
```

### Questions

1. Y a-t-il des valeurs manquantes ?
2. Quelle est la moyenne de la variable `bmi` ?
3. Quelle est la valeur maximale de `bp` ?

---

# Étape 3 - Séparer les données

Créer :

```python
X_train
X_test
y_train
y_test
```

avec :

```python
test_size=0.2
random_state=42
```

### Questions

1. Combien d'observations dans le train ?
2. Combien d'observations dans le test ?

---

# Étape 4 - Créer le modèle

Importer :

```python
LinearRegression
```

Créer :

```python
model
```

Puis entraîner le modèle.

### Question

Quelle commande permet d'entraîner le modèle ?

---

# Étape 5 - Faire une prédiction

Prédire les valeurs du jeu de test :

```python
predictions = ...
```

Afficher :

```python
print(predictions[:10])
```

### Question

Que représentent ces valeurs ?

---

# Étape 6 - Évaluer le modèle

Calculer la MAE :

```python
from sklearn.metrics import mean_absolute_error
```

### Questions

1. Calculer la MAE.
2. Interpréter le résultat.

Phrase attendue :

> En moyenne, le modèle se trompe de ______ unités sur la progression du diabète.

---

# Étape 7 - Comparer réel / prédit

Afficher les 10 premières prédictions :

```python
for real, pred in zip(y_test[:10], predictions[:10]):
    print(...)
```

Exemple attendu :

```text
Réel : 219
Prédit : 198.5
```

### Question

Le modèle semble-t-il proche de la réalité ?

---

# Étape 8 - Comprendre les coefficients

Afficher :

```python
model.coef_
```

Afficher :

```python
X.columns
```

### Questions

1. Combien de coefficients possède le modèle ?
2. Quelle variable possède le coefficient positif le plus élevé ?
3. Que signifie un coefficient positif ?
4. Que signifie un coefficient négatif ?

---

# Bonus 1

Calculer le score :

```python
model.score(X_test, y_test)
```

### Question

Que mesure le coefficient (R^2) ?

---

# Bonus 2

Tracer :

```python
Valeurs réelles
```

contre

```python
Valeurs prédites
```

avec Matplotlib.

### Question

Que devrait-on observer si le modèle était parfait ?

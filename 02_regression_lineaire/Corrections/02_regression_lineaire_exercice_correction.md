# Correction : première régression avec Scikit-Learn

## Étape 1 - Charger le dataset

```python
from sklearn.datasets import load_diabetes

data = load_diabetes(as_frame=True)

X = data.data
y = data.target
```

Le dataset contient `442` observations et `10` variables explicatives.

---

## Étape 2 - Explorer les données

```python
X.info()
X.describe()
```

Il n'y a pas de valeurs manquantes dans ce dataset.

---

## Étape 3 - Séparer les données

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Le split donne `353` observations pour le train et `89` pour le test.

---

## Étape 4 - Créer le modèle

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

La commande clé pour entraîner le modèle est `model.fit(X_train, y_train)`.

---

## Étape 5 - Faire une prédiction

```python
predictions = model.predict(X_test)
print(predictions[:10])
```

Les valeurs affichées sont les prédictions du modèle sur le jeu de test.

---

## Étape 6 - Évaluer le modèle

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, predictions)
print(mae)
```

La MAE mesure l'erreur moyenne absolue du modèle. Plus elle est faible, plus le modèle est proche des valeurs réelles.

---

## Étape 7 - Comparer réel / prédit

```python
for real, pred in zip(y_test[:10], predictions[:10]):
    print(f"Réel : {real}")
    print(f"Prédit : {pred}")
```

On doit observer que les prédictions sont parfois proches des valeurs réelles, mais jamais exactes partout.

---

## Étape 8 - Comprendre les coefficients

```python
print(model.coef_)
print(X.columns)
```

Réponses :

1. Le modèle possède `10` coefficients.
2. La variable avec le coefficient positif le plus élevé dépend de l'entraînement, mais on peut l'identifier avec `model.coef_`.
3. Un coefficient positif signifie que lorsque la variable augmente, la prédiction tend à augmenter.
4. Un coefficient négatif signifie que lorsque la variable augmente, la prédiction tend à diminuer.

---

## Bonus 1

```python
model.score(X_test, y_test)
```

Le score `R^2` mesure la qualité globale de l'ajustement.

---

## Bonus 2

On peut tracer un nuage de points :

```python
import matplotlib.pyplot as plt

plt.scatter(y_test, predictions)
plt.xlabel("Valeurs réelles")
plt.ylabel("Valeurs prédites")
plt.show()
```

Si le modèle était parfait, tous les points seraient exactement sur la diagonale.

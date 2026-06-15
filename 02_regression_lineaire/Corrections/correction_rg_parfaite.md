### Exemple 1 : droite presque parfaite

```python
import numpy as np
import pandas as pd

np.random.seed(42)

surface = np.random.randint(20, 200, 500)

prix = 3000 * surface + np.random.normal(0, 10000, 500)

df = pd.DataFrame({
    "surface": surface,
    "prix": prix
})
```

Puis :

```python
from sklearn.linear_model import LinearRegression

X = df[["surface"]]
y = df["prix"]

reg = LinearRegression()
reg.fit(X, y)

print("R² =", reg.score(X, y))
```

Vous obtenez généralement :

```text
R² ≈ 0.99
```

La droite est très visible.

---

### Exemple 2 : plan presque parfait

```python
import numpy as np
import pandas as pd

np.random.seed(42)

surface = np.random.randint(20, 200, 1000)
pieces = np.random.randint(1, 8, 1000)

prix = (
    3000 * surface
    + 15000 * pieces
    + np.random.normal(0, 5000, 1000)
)

df = pd.DataFrame({
    "surface": surface,
    "pieces": pieces,
    "prix": prix
})
```

Régression :

```python
from sklearn.linear_model import LinearRegression

X = df[["surface", "pieces"]]
y = df["prix"]

reg = LinearRegression()
reg.fit(X, y)

print("R² =", reg.score(X, y))
```

On obtient souvent :

```text
R² ≈ 0.995
```

Le plan est presque parfait car les données ont été générées par une formule linéaire.

---

### Exemple 3 : dataset réel très corrélé

Si vous voulez un dataset officiel :

```python
from sklearn.datasets import load_diabetes
```

donne environ :

```text
R² ≈ 0.52
```

```python
from sklearn.datasets import fetch_california_housing
```

donne souvent :

```text
R² ≈ 0.60
```

Les vrais jeux de données dépassent rarement 0.8 avec une simple régression linéaire.

---

Pour un cours, je conseille souvent la progression suivante :

1. Dataset synthétique → (R^2 \approx 0.99) pour comprendre la mécanique.
2. Dataset immobilier synthétique à 2 variables → visualisation du plan.
3. Dataset Diabetes ou California Housing → montrer qu'en pratique la réalité est plus complexe et que (R^2) baisse.

C'est très parlant pour les étudiants : ils voient d'abord un cas « parfait », puis les limites du monde réel.

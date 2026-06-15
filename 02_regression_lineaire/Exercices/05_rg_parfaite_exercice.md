# Exercice : Quand une régression linéaire est presque parfaite

## Objectif

Comprendre pourquoi une régression linéaire peut obtenir un score R² très élevé lorsque les données suivent presque exactement une formule linéaire.

Dans cet exercice, on travaille avec des données synthétiques : elles sont générées par du code, donc on connaît la logique qui relie les variables au prix.

---

## Partie 1 - Droite presque parfaite

On donne le dataset immobilier synthétique suivant :

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

Ce dataset contient :

- une variable `surface` ;
- une cible `prix` ;
- une relation presque linéaire entre les deux.

### Questions

1. Quelle formule relie principalement `surface` et `prix` ?
2. À quoi sert le bruit aléatoire ?
3. Pourquoi parle-t-on d'une relation presque parfaite, et pas parfaitement parfaite ?

---

## Partie 2 - Entraîner une régression simple

Créer :

```python
X = df[["surface"]]
y = df["prix"]
```

Puis entraîner :

```python
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
```

### Questions

1. Quelle commande entraîne le modèle ?
2. Combien de coefficients le modèle apprend-il ?
3. À quelle valeur le coefficient devrait-il être proche ?

---

## Partie 3 - Mesurer le R²

Afficher le score :

```python
print("R² =", ...)
```

### Questions

1. Le R² est-il proche de 1 ?
2. Que signifie un R² proche de 1 ?
3. Pourquoi obtient-on un meilleur R² que dans un dataset réel comme diabetes ?

---

## Partie 4 - Ajouter une deuxième variable

Créer un nouveau dataset avec :

- `surface` ;
- `pieces` ;
- `prix`.

Le prix doit dépendre de la surface et du nombre de pièces.

Structure attendue :

```python
np.random.seed(42)

surface = ...
pieces = ...

prix = (
    ...
    + ...
    + ...
)

df = pd.DataFrame({
    "surface": surface,
    "pieces": pieces,
    "prix": prix
})
```

### Questions

1. Quelles sont les deux variables explicatives ?
2. Quelle est la cible ?
3. Pourquoi parle-t-on maintenant de régression linéaire multiple ?

---

## Partie 5 - Entraîner une régression multiple

Créer :

```python
X = df[["surface", "pieces"]]
y = df["prix"]
```

Puis entraîner une nouvelle régression linéaire et afficher le R².

### Questions finales

1. Le R² est-il encore très élevé ?
2. Pourquoi le modèle retrouve-t-il presque parfaitement la relation ?
3. Pourquoi les vrais datasets dépassent-ils rarement 0.8 avec une simple régression linéaire ?
4. À quoi sert un dataset synthétique dans un cours de Machine Learning ?

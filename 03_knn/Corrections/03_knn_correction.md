# Correction - KNN

## 1. Exercice sur Alan

Données :

```python
students = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "math": [15, 8, 12, 18, 10],
    "python": [14, 10, 15, 17, 9],
    "status": [1, 0, 1, 1, 0]
})

alan = {
    "math": 11,
    "python": 10
}
```

Distances principales :

- Emma : `sqrt((11-10)^2 + (10-9)^2) = sqrt(2) ≈ 1.41`
- Bob : `sqrt((11-8)^2 + (10-10)^2) = 3`
- Charlie : `sqrt((11-12)^2 + (10-15)^2) = sqrt(26) ≈ 5.10`

Résultat :

- `k = 1` : la classe prédite est `0`
- `k = 3` : la classe prédite est `0`

Le voisin le plus proche est Emma, puis le vote des 3 plus proches donne encore la classe `0`.

---

## 2. Exercice Iris

Nouvelle fleur :

```text
(5.9, 3.0, 4.2, 1.5)
```

Distances données dans le cours :

- Versicolor : `0.33`
- Virginica : `1.85`
- Setosa : `3.20`

Conclusion :

- le plus proche voisin est `Versicolor`
- avec `k = 3`, la majorité reste `Versicolor`

---

## 3. Exercice `k` et normalisation

Points à retenir :

- `k` est le nombre de voisins, pas le nombre de variables ;
- on choisit `k` par expérimentation ;
- en pratique, on regarde plutôt la validation que le test final ;
- la normalisation est apprise sur `X_train` uniquement ;
- on applique ensuite la même transformation à `X_test`.

Code attendu :

```python
scaler = StandardScaler()

X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)
```

Effet de `k` :

- `k` petit : très local, sensible au bruit ;
- `k` moyen : compromis souvent utile ;
- `k` grand : plus lissé, parfois trop général.


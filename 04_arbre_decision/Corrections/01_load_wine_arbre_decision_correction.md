# Correction : arbre de décision avec `load_wine`

## 1. Charger les données

```python
import pandas as pd
from sklearn.datasets import load_wine

wine = load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name="target")

X.head()
```

Dimensions :

```python
print(X.shape)
print(y.shape)
print(wine.target_names)
```

Réponses :

- `X` contient `178` lignes ;
- `X` contient `13` variables explicatives ;
- la cible contient `3` classes.

---

## 2. Séparer train et test

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

`stratify=y` permet de garder à peu près la même proportion de classes dans le train et dans le test.

---

## 3. Entraîner un arbre simple

```python
from sklearn.tree import DecisionTreeClassifier

modele = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

modele.fit(X_train, y_train)
```

---

## 4. Évaluer le modèle

```python
score_train = modele.score(X_train, y_train)
score_test = modele.score(X_test, y_test)

print("Score train :", score_train)
print("Score test  :", score_test)
```

Interprétation :

- le score train mesure la performance sur les données vues ;
- le score test mesure la performance sur des données non vues ;
- si le score train est beaucoup plus élevé que le score test, il faut suspecter du surapprentissage.

---

## 5. Lire les règles de l'arbre

```python
from sklearn.tree import export_text

texte_arbre = export_text(
    modele,
    feature_names=list(X.columns)
)

print(texte_arbre)
```

Un arbre est interprétable parce qu'il peut s'écrire comme une suite de règles :

```text
si variable <= seuil
alors aller à gauche
sinon aller à droite
```

---

## 6. Visualiser l'arbre

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

Chaque noeud indique :

- la question posée ;
- le critère de pureté ;
- le nombre d'exemples ;
- la répartition des classes ;
- la classe prédite.

---

## 7. Variables importantes

```python
importances = pd.Series(
    modele.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

importances.head(10)
```

Une variable importante ne prouve pas une relation causale.

Elle indique seulement que cette variable a été utile pour les découpages de cet arbre.

---

## 8. Comparer avec un arbre non limité

```python
arbre_libre = DecisionTreeClassifier(random_state=42)

arbre_libre.fit(X_train, y_train)

print("Score train :", arbre_libre.score(X_train, y_train))
print("Score test  :", arbre_libre.score(X_test, y_test))
```

Un arbre non limité peut obtenir un score train très élevé, parfois `1.0`.

Cela ne signifie pas forcément qu'il est meilleur.

Il peut avoir appris des détails trop spécifiques du train.

C'est le surapprentissage.

---

## Conclusion

Un arbre de décision apprend une suite de questions du type :

```text
variable <= seuil ?
```

Sur `load_wine`, il cherche les mesures chimiques qui séparent le mieux les classes de vin.

Il est facile à interpréter, mais il faut contrôler sa complexité avec des paramètres comme :

```text
max_depth
min_samples_leaf
min_samples_split
```

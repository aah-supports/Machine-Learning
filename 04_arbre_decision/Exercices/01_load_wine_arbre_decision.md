# Exercice : arbre de décision avec `load_wine`

## Objectif

Entraîner un arbre de décision sur le dataset `load_wine`.

Le but est de comprendre :

- comment charger un dataset Scikit-Learn ;
- comment entraîner un `DecisionTreeClassifier` ;
- comment comparer score train et score test ;
- comment lire les règles de l'arbre ;
- comment interpréter les variables importantes.

---

## 1. Charger les données

Compléter :

```python
import pandas as pd
from sklearn.datasets import load_wine

wine = ...

X = pd.DataFrame(..., columns=...)
y = pd.Series(..., name="target")

X.head()
```

Questions :

1. Combien de lignes contient `X` ?
2. Combien de variables explicatives contient `X` ?
3. Combien de classes contient la cible ?

---

## 2. Séparer train et test

Compléter :

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    ...,
    ...,
    test_size=0.2,
    random_state=42,
    stratify=...
)
```

Question :

Pourquoi utilise-t-on `stratify=y` ?

---

## 3. Entraîner un arbre simple

Compléter :

```python
from sklearn.tree import DecisionTreeClassifier

modele = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

modele.fit(..., ...)
```

---

## 4. Évaluer le modèle

Compléter :

```python
score_train = ...
score_test = ...

print("Score train :", score_train)
print("Score test  :", score_test)
```

Questions :

1. Le score train est-il élevé ?
2. Le score test est-il proche du score train ?
3. Le modèle semble-t-il surapprendre ?

---

## 5. Lire les règles de l'arbre

Compléter :

```python
from sklearn.tree import export_text

texte_arbre = export_text(
    ...,
    feature_names=list(...)
)

print(texte_arbre)
```

Questions :

1. Quelle est la première variable utilisée par l'arbre ?
2. Quel est le premier seuil ?
3. Pourquoi peut-on dire que l'arbre est interprétable ?

---

## 6. Visualiser l'arbre

Compléter :

```python
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(16, 8))

plot_tree(
    ...,
    feature_names=...,
    class_names=...,
    filled=True,
    rounded=True
)

plt.show()
```

---

## 7. Variables importantes

Compléter :

```python
importances = pd.Series(
    ...,
    index=...
).sort_values(ascending=False)

importances.head(10)
```

Question :

Une variable importante prouve-t-elle une relation causale ?

---

## 8. Comparer avec un arbre non limité

Entraîner un arbre sans `max_depth`.

```python
arbre_libre = DecisionTreeClassifier(random_state=42)

arbre_libre.fit(..., ...)

print("Score train :", ...)
print("Score test  :", ...)
```

Questions :

1. Le score train augmente-t-il ?
2. Le score test augmente-t-il toujours ?
3. Pourquoi un arbre trop profond peut-il surapprendre ?

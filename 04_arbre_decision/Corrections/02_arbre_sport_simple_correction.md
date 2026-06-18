# Correction : arbre simple avec âge et poids

## 1. Comprendre le dataset

```python
import pandas as pd

data = pd.DataFrame({
    "age": [18, 20, 22, 24, 26, 60],
    "poids": [65, 70, 95, 75, 100, 80],
    "sport": ["Oui", "Oui", "Non", "Oui", "Non", "Non"]
})

data
```

Les variables explicatives sont :

```text
age
poids
```

La cible est :

```text
sport
```

Elle contient deux classes :

```text
Oui
Non
```

---

## 2. Séparer `X` et `y`

```python
X = data[["age", "poids"]]
y = data["sport"]
```

`X` contient les informations utilisées pour prédire.

`y` contient la réponse que le modèle doit apprendre.

---

## 3. Entraîner l'arbre

```python
from sklearn.tree import DecisionTreeClassifier

modele = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

modele.fit(X, y)
```

`max_depth=2` empêche l'arbre de créer trop de niveaux.

Sur ce petit dataset, une seule question suffit déjà à séparer parfaitement les classes.

---

## 4. Prédire une nouvelle personne

```python
nouvelle_personne = pd.DataFrame({
    "age": [25],
    "poids": [90]
})

prediction = modele.predict(nouvelle_personne)

print("Classe prédite :", prediction[0])
```

Résultat :

```text
Classe prédite : Non
```

La personne pèse `90 kg`.

Elle se trouve du côté des observations classées `Non`.

---

## 5. Lire les règles

```python
from sklearn.tree import export_text

regles = export_text(
    modele,
    feature_names=list(X.columns)
)

print(regles)
```

L'arbre obtenu est équivalent à :

```text
poids <= 77.5 ?
├── Oui -> Sport = Oui
└── Non -> Sport = Non
```

La première variable utilisée est donc :

```text
poids
```

Le seuil se situe entre `75` et `80` :

```text
77.5
```

Ce seuil sépare parfaitement les données :

```text
65, 70, 75  -> Oui
80, 95, 100 -> Non
```

L'arbre est interprétable parce que sa prédiction peut être expliquée avec une règle lisible.

---

## 6. Visualisation facultative

```python
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10, 5))

plot_tree(
    modele,
    feature_names=X.columns,
    class_names=modele.classes_,
    filled=True,
    rounded=True
)

plt.show()
```

---

## Synthèse

```text
Un arbre de décision pose des questions du type :
variable <= seuil ?

Il choisit la question qui rend les groupes
les plus homogènes possible.
```

Dans cet exemple, le poids suffit à séparer les deux classes.

Il faut toutefois rester prudent : le dataset est très petit et artificiel. Cette règle ne doit pas être interprétée comme une vérité générale sur la pratique sportive.

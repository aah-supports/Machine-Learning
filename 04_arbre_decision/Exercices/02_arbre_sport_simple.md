# Exercice : arbre de décision simple avec âge et poids

## Objectif

On veut prédire si une personne fait du sport à partir de deux variables :

- `age` ;
- `poids`.

La cible est :

```text
Sport = Oui ou Non
```

Le but est de s'entraîner à :

- créer un petit dataset ;
- séparer `X` et `y` ;
- entraîner un arbre de décision ;
- prédire une nouvelle personne ;
- lire les règles apprises par l'arbre.

---

## 1. Créer le dataset

Compléter :

```python
import pandas as pd

data = pd.DataFrame({
    "age": [18, 20, 22, 24, 26, 60],
    "poids": [65, 70, 95, 75, 100, 80],
    "sport": ["Oui", "Oui", "Non", "Oui", "Non", "Non"]
})

data
```

Questions :

1. Quelles sont les variables explicatives ?
2. Quelle est la cible ?
3. Combien y a-t-il de classes possibles ?

---

## 2. Séparer `X` et `y`

Compléter :

```python
X = ...
y = ...
```

---

## 3. Entraîner un arbre de décision

Compléter :

```python
from sklearn.tree import DecisionTreeClassifier

modele = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

modele.fit(..., ...)
```

Question :

Pourquoi limite-t-on ici la profondeur avec `max_depth=2` ?

---

## 4. Prédire une nouvelle personne

Nouvelle personne :

```text
age = 25
poids = 90
```

Compléter :

```python
nouvelle_personne = pd.DataFrame({
    "age": [25],
    "poids": [90]
})

prediction = ...

print(prediction)
```

Question :

Quelle classe est prédite ?

---

## 5. Lire les règles de l'arbre

Compléter :

```python
from sklearn.tree import export_text

regles = export_text(
    ...,
    feature_names=list(...)
)

print(regles)
```

Questions :

1. Quelle variable est utilisée dans la première question ?
2. Quel seuil est utilisé ?
3. Pourquoi un arbre de décision est-il plus interprétable qu'un modèle purement numérique ?

---

## 6. Question de synthèse

Compléter :

```text
Un arbre de décision cherche à poser des questions du type ...
Il choisit la question qui rend les groupes ...
```

---

[Voir la correction](../Corrections/02_arbre_sport_simple_correction.md)

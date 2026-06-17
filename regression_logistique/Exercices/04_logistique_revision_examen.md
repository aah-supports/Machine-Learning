# Exercice 4 : régression logistique et heures de révision

## Objectif

On veut prédire la réussite à un examen à partir d'une seule variable :

```text
heures de révision
```

La cible est binaire :

```text
0 = échec
1 = réussite
```

Le but est de s'entraîner à :

- créer un petit dataset ;
- séparer `X` et `y` ;
- entraîner une régression logistique ;
- utiliser `predict` ;
- utiliser `predict_proba` ;
- lire les paramètres appris par le modèle.

---

## 1. Créer le dataset

Compléter et exécuter :

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "heures_revision": [1, 2, 3, 4, 5, 6, 7, 8],
    "reussite": [0, 0, 0, 0, 1, 1, 1, 1]
})

print("Dataset")
print(data)
```

Question :

1. À partir de combien d'heures les étudiants réussissent-ils dans ce petit dataset ?

---

## 2. Séparer les variables explicatives et la cible

Créer :

```python
X = ...
y = ...
```

Questions :

1. Que contient `X` ?
2. Que contient `y` ?
3. Pourquoi `X` doit-il rester sous forme de tableau avec une colonne ?

---

## 3. Créer et entraîner le modèle

Compléter :

```python
modele = ...
modele.fit(..., ...)
```

Question :

1. Que fait `fit(X, y)` ?

---

## 4. Prédire pour un étudiant qui a révisé 4 heures

Compléter :

```python
etudiant_4h = pd.DataFrame({
    "heures_revision": [4]
})

prediction_4h = ...
proba_4h = ...

print("Classe prédite :", prediction_4h[0])
print("Probabilité échec :", round(proba_4h[0][0], 3))
print("Probabilité réussite :", round(proba_4h[0][1], 3))
```

Questions :

1. Quelle classe est prédite ?
2. Quelle est la probabilité de réussite ?
3. Le cas semble-t-il proche de la frontière ?

---

## 5. Prédire pour un étudiant qui a révisé 7 heures

Compléter :

```python
etudiant_7h = pd.DataFrame({
    "heures_revision": [7]
})

prediction_7h = ...
proba_7h = ...

print("Classe prédite :", prediction_7h[0])
print("Probabilité échec :", round(proba_7h[0][0], 3))
print("Probabilité réussite :", round(proba_7h[0][1], 3))
```

Questions :

1. Quelle classe est prédite ?
2. Quelle est la probabilité de réussite ?
3. Pourquoi le modèle est-il plus confiant que pour 4 heures ?

---

## 6. Afficher les paramètres appris

Compléter :

```python
print("Coefficient :", ...)
print("Intercept :", ...)
```

Questions :

1. Le coefficient est-il positif ou négatif ?
2. Qu'est-ce que cela signifie ?
3. Pourquoi plus d'heures de révision augmentent-elles la probabilité de réussite ?

---

## Conclusion attendue

Rédiger une phrase de synthèse :

```text
Le modèle apprend que plus le nombre d'heures de révision augmente,
plus la probabilité de réussite augmente.
```

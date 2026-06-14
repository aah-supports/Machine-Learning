# Chapitre 5 : Régression logistique

## 1. Objectif du chapitre

Avec la régression linéaire, nous avons prédit une valeur numérique.

Exemple :

```text
surface → prix
```

La **régression logistique** sert à prédire une catégorie.

Plus précisément, elle est souvent utilisée pour une **classification binaire** :

```text
0 ou 1
non ou oui
échec ou réussite
spam ou non spam
```

Dans ce chapitre, nous allons utiliser un exemple simple :

```text
Prédire si un étudiant valide un examen.
```

Objectifs :

- distinguer régression linéaire et régression logistique ;
- comprendre la notion de probabilité ;
- transformer une probabilité en classe ;
- entraîner un modèle avec `LogisticRegression` ;
- évaluer avec l'accuracy et la matrice de confusion ;
- comprendre les faux positifs et faux négatifs.

---

## 2. Exemple métier : validation d'un examen

On dispose d'un dataset d'étudiants.

Pour chaque étudiant, on connaît :

| Variable | Signification |
| -------- | ------------- |
| heures_revision | nombre d'heures de révision |
| presence | taux de présence en cours |
| controle_continu | note de contrôle continu |
| projet_rendu | projet rendu ou non |
| valide | examen validé ou non |

Exemple :

| heures_revision | presence | controle_continu | projet_rendu | valide |
| --------------- | -------- | ---------------- | ------------ | ------ |
| 2               | 0.45     | 7                | 0            | 0      |
| 8               | 0.75     | 11               | 1            | 1      |
| 15              | 0.92     | 14               | 1            | 1      |

La colonne `valide` est le label.

```text
0 → l'étudiant ne valide pas
1 → l'étudiant valide
```

---

## 3. Pourquoi pas une régression linéaire ?

On pourrait être tenté d'utiliser une régression linéaire.

Mais une régression linéaire produit une valeur numérique libre.

Elle peut prédire :

```text
-0.2
0.7
1.4
```

Pour une classe binaire, ce n'est pas idéal.

Une probabilité doit rester entre `0` et `1`.

```text
0   → impossible ou très peu probable
0.5 → incertain
1   → très probable
```

La régression logistique répond à ce besoin.

Elle produit une probabilité.

---

## 4. L'idée de la régression logistique

La régression logistique commence comme une régression linéaire.

Elle combine les variables :

```text
score = a1 × heures_revision
      + a2 × presence
      + a3 × controle_continu
      + a4 × projet_rendu
      + b
```

Puis elle transforme ce score en probabilité entre `0` et `1`.

Cette transformation s'appelle la **sigmoïde**.

```text
probabilité = sigmoid(score)
```

Intuition :

```text
score très négatif → probabilité proche de 0
score proche de 0  → probabilité proche de 0.5
score très positif → probabilité proche de 1
```

Il n'est pas nécessaire de maîtriser la formule au début.

Ce qui compte ici :

```text
La régression logistique prédit une probabilité.
```

---

## 5. Du score à la décision

Le modèle peut prédire une probabilité.

Exemple :

```text
probabilité de valider = 0.82
```

Pour obtenir une classe, on choisit un seuil.

Le seuil le plus courant est `0.5`.

```text
probabilité >= 0.5 → classe 1
probabilité < 0.5  → classe 0
```

Exemple :

| Étudiant | Probabilité | Classe prédite |
| -------- | ----------- | -------------- |
| A | 0.18 | 0 |
| B | 0.63 | 1 |
| C | 0.91 | 1 |

Le seuil peut être modifié selon le contexte métier.

Si l'erreur coûte cher, on ne choisit pas forcément `0.5`.

---

## 6. En Python avec scikit-learn

Modules utiles :

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
```

Exemple :

```python
X = data[["heures_revision", "presence", "controle_continu", "projet_rendu"]]
y = data["valide"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modele = LogisticRegression()
modele.fit(X_train, y_train)

predictions = modele.predict(X_test)
```

---

## 7. Prédire une probabilité

Avec `predict`, le modèle donne directement une classe.

```python
modele.predict(X_test)
```

Avec `predict_proba`, il donne les probabilités.

```python
modele.predict_proba(X_test)
```

Exemple :

```text
[0.22, 0.78]
```

Cela signifie :

```text
probabilité classe 0 = 0.22
probabilité classe 1 = 0.78
```

Ici, le modèle prédit donc la classe `1`.

---

## 8. Accuracy

L'**accuracy** mesure la proportion de bonnes réponses.

```text
accuracy = nombre de prédictions correctes / nombre total de prédictions
```

Exemple :

```text
8 bonnes prédictions sur 10 → accuracy = 0.8
```

En Python :

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print(accuracy)
```

L'accuracy est facile à comprendre.

Mais elle ne dit pas tout.

---

## 9. Matrice de confusion

La matrice de confusion montre le détail des erreurs.

Pour une classification binaire :

| | Prédit 0 | Prédit 1 |
| --- | --- | --- |
| Réel 0 | vrais négatifs | faux positifs |
| Réel 1 | faux négatifs | vrais positifs |

Dans notre exemple :

- **faux positif** : le modèle prédit que l'étudiant valide, mais il ne valide pas ;
- **faux négatif** : le modèle prédit que l'étudiant ne valide pas, mais il valide.

En Python :

```python
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, predictions)
```

---

## 10. Pourquoi c'est important métier ?

Toutes les erreurs ne se valent pas.

Exemple dans un contexte médical :

```text
faux négatif = patient malade prédit non malade
```

Cette erreur peut être plus grave qu'un faux positif.

Dans notre exemple étudiant :

```text
faux négatif = étudiant qui aurait pu valider, mais que le modèle classe en échec
```

Il faut donc regarder les erreurs, pas seulement le score global.

---

## 11. Lien avec KNN

La régression logistique et KNN peuvent tous les deux faire de la classification.

Mais ils ne raisonnent pas de la même manière.

| Modèle | Idée |
| ------ | ---- |
| Régression logistique | apprendre une frontière de décision |
| KNN | regarder les voisins les plus proches |

La régression logistique apprend des coefficients.

KNN compare la nouvelle donnée aux exemples connus.

---

## 12. Ce qu'il faut retenir

- La régression logistique sert à faire de la classification.
- Elle est très utilisée pour les problèmes binaires.
- Elle prédit une probabilité entre `0` et `1`.
- Un seuil transforme la probabilité en classe.
- `predict` donne une classe.
- `predict_proba` donne les probabilités.
- L'accuracy mesure le pourcentage de bonnes réponses.
- La matrice de confusion montre le détail des erreurs.
- Les faux positifs et faux négatifs doivent être interprétés avec le métier.

---

## 13. Exercice pratique

Dans le notebook associé, vous allez prédire si un étudiant valide un examen à partir de ses données de travail et de présence.

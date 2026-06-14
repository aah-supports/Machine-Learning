# Préparer et nettoyer les données

## 1. Objectif du chapitre

Avant d'entraîner un modèle, il faut préparer le dataset.

En pratique, un modèle de Machine Learning ne reçoit presque jamais des données parfaites.

On rencontre souvent :

- des valeurs manquantes ;
- des doublons ;
- des types incorrects ;
- des valeurs impossibles ;
- des colonnes inutiles ;
- des catégories sous forme de texte ;
- des unités mélangées.

Ce chapitre sert à comprendre le travail qui vient **avant** le modèle.

Objectifs :

- inspecter un dataset ;
- repérer les problèmes courants ;
- nettoyer les valeurs ;
- transformer les colonnes ;
- préparer `X` et `y` ;
- appliquer des bonnes pratiques métier.

---

## 2. Pourquoi cette étape est importante ?

Un modèle apprend à partir des données qu'on lui donne.

Si les données sont incohérentes, le modèle peut apprendre une relation incohérente.

Exemple :

| surface | pièces | quartier | prix |
| ------- | ------ | -------- | ---- |
| 70      | 3      | centre   | 350000 |
| ?       | 4      | nord     | 420000 |
| 85 m2   | 3      | centre   | 390000 |
| 70      | 3      | centre   | 350000 |
| -10     | 2      | sud      | 180000 |

Ce tableau pose plusieurs problèmes :

- `?` n'est pas une valeur numérique ;
- `85 m2` mélange nombre et texte ;
- une ligne est dupliquée ;
- `-10` est une surface impossible ;
- `quartier` est du texte, donc il faudra le transformer.

Avant de faire :

```python
modele.fit(X_train, y_train)
```

il faut donc vérifier que les données ont du sens.

---

## 3. Les premières questions à poser

Avant de corriger, on observe.

Questions utiles :

```text
Combien de lignes ?
Combien de colonnes ?
Quelles sont les colonnes numériques ?
Quelles sont les colonnes textuelles ?
Y a-t-il des valeurs manquantes ?
Y a-t-il des doublons ?
Y a-t-il des valeurs impossibles ?
Quelle colonne veut-on prédire ?
```

En Python :

```python
data.shape
data.head()
data.info()
data.describe()
data.isna().sum()
data.duplicated().sum()
```

Ces commandes ne nettoient rien.

Elles servent à comprendre le dataset.

---

## 4. Bonnes pratiques métier

### 1. Toujours garder une version brute

On ne modifie pas directement le fichier original.

Bonne pratique :

```text
données brutes → copie de travail → données nettoyées
```

Pourquoi ?

Parce qu'il faut pouvoir revenir en arrière et expliquer ce qui a été changé.

En Python :

```python
data_brut = data.copy()
data_clean = data.copy()
```

---

### 2. Documenter les choix de nettoyage

Nettoyer une donnée n'est pas neutre.

Exemples :

- supprimer une ligne ;
- remplacer une valeur manquante ;
- corriger une valeur impossible ;
- fusionner deux catégories ;
- retirer une colonne.

Chaque décision doit pouvoir être justifiée.

Exemple :

```text
Les lignes avec une surface négative sont supprimées, car une surface habitable ne peut pas être négative.
```

---

### 3. Ne pas inventer une information que l'on ne connaît pas

Une valeur manquante ne doit pas être remplacée au hasard.

Mauvaise idée :

```text
surface manquante → 100
```

Meilleure approche :

- vérifier si l'information peut être retrouvée ;
- remplacer par une valeur raisonnable si cela se justifie ;
- ou supprimer la ligne si elle est trop problématique.

Exemple :

```python
data_clean["surface"] = data_clean["surface"].fillna(data_clean["surface"].median())
```

La médiane est souvent plus robuste que la moyenne si certaines valeurs sont extrêmes.

---

### 4. Vérifier les valeurs impossibles

Certaines valeurs sont techniquement numériques, mais impossibles métier.

Exemples :

```text
surface < 0
prix < 0
nombre de pièces = 0
âge < 0
```

Python ne sait pas que `-10 m2` est impossible.

C'est au métier de le dire.

```python
data_clean = data_clean[data_clean["surface"] > 0]
data_clean = data_clean[data_clean["prix"] > 0]
```

---

### 5. Transformer le texte avant le modèle

La plupart des modèles scikit-learn ne savent pas utiliser directement une colonne texte.

Exemple :

| quartier |
| -------- |
| centre |
| nord |
| sud |

On peut transformer cette colonne en colonnes numériques avec `get_dummies`.

```python
data_clean = pd.get_dummies(data_clean, columns=["quartier"])
```

Résultat :

| quartier_centre | quartier_nord | quartier_sud |
| --------------- | ------------- | ------------ |
| 1               | 0             | 0            |
| 0               | 1             | 0            |
| 0               | 0             | 1            |

---

### 6. Éviter la fuite de données

La **fuite de données** arrive quand le modèle reçoit une information qu'il ne devrait pas connaître au moment de prédire.

Exemple :

```text
On veut prédire le prix de vente.
```

Colonne dangereuse :

```text
date_signature_vente
```

Si cette information n'est connue qu'après la vente, elle ne doit pas servir à prédire.

Question métier à poser :

```text
Cette information sera-t-elle disponible au moment de la prédiction ?
```

Si la réponse est non, la colonne ne doit pas être dans `X`.

---

### 7. Faire le split avant les transformations apprises

Certaines transformations calculent des informations sur les données.

Exemples :

- moyenne ;
- médiane ;
- écart-type ;
- catégories observées.

Pour éviter que le test influence le train, on sépare d'abord :

```python
X_train, X_test, y_train, y_test = train_test_split(...)
```

Puis on apprend les transformations sur le train.

Principe :

```text
fit sur le train
transform sur le test
```

C'est la même logique que pour la normalisation avec `StandardScaler`.

---

## 5. Exemple complet de nettoyage

Dataset initial :

```python
import pandas as pd

data = pd.DataFrame({
    "surface": ["70", "?", "85 m2", "70", "-10", "120"],
    "pieces": [3, 4, 3, 3, 2, None],
    "quartier": ["centre", "nord", "centre", "centre", "sud", "ouest"],
    "prix": [350000, 420000, 390000, 350000, 180000, 610000]
})
```

---

### Étape 1 : observer

```python
data.head()
data.info()
data.isna().sum()
data.duplicated().sum()
```

---

### Étape 2 : créer une copie de travail

```python
data_clean = data.copy()
```

---

### Étape 3 : corriger la surface

On transforme la colonne `surface` en nombre.

```python
data_clean["surface"] = (
    data_clean["surface"]
    .astype(str)
    .str.replace(" m2", "", regex=False)
    .replace("?", None)
)

data_clean["surface"] = pd.to_numeric(data_clean["surface"])
```

---

### Étape 4 : gérer les valeurs manquantes

```python
data_clean["surface"] = data_clean["surface"].fillna(data_clean["surface"].median())
data_clean["pieces"] = data_clean["pieces"].fillna(data_clean["pieces"].median())
```

---

### Étape 5 : supprimer doublons et valeurs impossibles

```python
data_clean = data_clean.drop_duplicates()
data_clean = data_clean[data_clean["surface"] > 0]
data_clean = data_clean[data_clean["prix"] > 0]
```

---

### Étape 6 : transformer les catégories

```python
data_clean = pd.get_dummies(data_clean, columns=["quartier"], dtype=int)
```

---

### Étape 7 : préparer X et y

```python
X = data_clean.drop(columns=["prix"])
y = data_clean["prix"]
```

À partir de ce moment, on peut passer à la régression linéaire.

---

## 6. Ce qu'il faut retenir

- Les données réelles sont rarement propres.
- Nettoyer les données fait partie du travail de Machine Learning.
- On commence toujours par observer le dataset.
- On garde une version brute.
- On documente les décisions de nettoyage.
- On vérifie les valeurs impossibles avec du bon sens métier.
- On transforme le texte en nombres avant d'entraîner.
- On évite les colonnes qui créent une fuite de données.
- On prépare `X` et `y` seulement après avoir clarifié le dataset.

---

## 7. Suite du cours

Après avoir préparé les données, on peut entraîner un premier modèle.

La suite logique est la **régression linéaire**.

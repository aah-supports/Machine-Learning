# Chapitre 3 : KNN, voisins et normalisation

## 1. Objectif du chapitre

Dans les chapitres précédents, nous avons vu :

- comment séparer `X` et `y` ;
- comment séparer train et test ;
- comment entraîner un modèle ;
- comment mesurer une erreur ou un score sur des données non vues.

Dans ce chapitre, on étudie un nouveau modèle : **KNN**.

KNN signifie :

```text
K-Nearest Neighbors
```

En français :

```text
K plus proches voisins
```

Objectifs :

- comprendre l'idée de voisin proche ;
- comprendre pourquoi KNN correspond à une forme de bon sens humain ;
- représenter les données comme des points dans un espace mathématique ;
- comprendre l'hypothèse de régularité locale ;
- comprendre comment KNN prédit ;
- distinguer KNN classification et KNN régression ;
- comprendre pourquoi les distances peuvent être trompeuses ;
- comprendre pourquoi la normalisation est importante ;
- choisir une valeur raisonnable pour `k` ;
- tester le modèle sur des données non vues.

---

## 2. La question de départ

La question centrale de KNN est simple :

```text
À quels exemples déjà connus ma nouvelle donnée ressemble-t-elle le plus ?
```

Exemple immobilier :

```text
Je veux estimer le prix d'un logement de 76 m², 3 pièces, dans un quartier donné.
```

KNN va chercher dans le dataset les logements les plus proches.

Puis il utilise ces voisins pour prédire.

---

## 3. L'intuition humaine derrière KNN

KNN est probablement l'un des algorithmes de Machine Learning les plus proches du bon sens humain.

On peut le résumer ainsi :

```text
Les choses qui se ressemblent ont tendance à appartenir à la même catégorie.
```

Exemple :

```text
Si une nouvelle fleur ressemble beaucoup à des fleurs déjà identifiées comme iris versicolor,
alors elle est probablement aussi une iris versicolor.
```

Cette idée semble presque triviale.

Mais elle devient un vrai algorithme dès qu'on précise :

- comment représenter les données ;
- comment mesurer la ressemblance ;
- combien de voisins regarder ;
- comment décider à partir de ces voisins.

---

## 4. L'espace des données

Pour KNN, chaque ligne du dataset est représentée comme un point dans un espace.

Mathématiquement, une ligne est un vecteur :

```text
x = (x1, x2, ..., xn)
```

Exemple avec un logement :

```text
x = (surface, pieces, revenu_quartier)
```

Exemple concret :

```text
x = (76, 3, 49000)
```

Chaque variable correspond à une dimension.

Avec deux variables, on peut dessiner les points sur un plan.

Avec trois variables, on peut les imaginer dans l'espace.

Avec plus de variables, on ne peut plus facilement dessiner, mais le calcul reste possible.

---

## 5. L'hypothèse de régularité locale

KNN repose sur une hypothèse importante :

```text
Si deux points sont proches dans l'espace des variables,
alors leurs comportements sont probablement proches.
```

C'est l'hypothèse de régularité locale.

Exemple :

```text
Deux logements proches en surface, nombre de pièces et quartier
ont probablement des prix proches.
```

Exemple en classification :

```text
Deux fleurs proches en longueur et largeur de pétale
ont probablement la même espèce.
```

KNN fonctionne bien quand cette hypothèse est raisonnable.

Il fonctionne moins bien si des points proches dans les variables peuvent avoir des labels très différents.

---

## 6. Pourquoi ce n'est pas seulement une recette ?

KNN paraît simple, mais il repose sur une vraie structure mathématique :

1. les données sont des vecteurs ;
2. les vecteurs vivent dans un espace ;
3. une distance mesure la proximité ;
4. la proximité sert à prédire.

La distance euclidienne s'écrit souvent :

```text
d(x, y) = √((x1 - y1)² + (x2 - y2)² + ... + (xn - yn)²)
```

Cela donne une définition précise de la phrase :

```text
Ces deux exemples se ressemblent.
```

---

## 7. KNN n'apprend pas une formule

Une régression linéaire apprend une formule :

```text
prix = coefficient × surface + intercept
```

KNN fonctionne autrement.

Il garde les exemples d'entraînement en mémoire.

Quand une nouvelle donnée arrive, il :

1. calcule la distance entre cette nouvelle donnée et les lignes d'entraînement ;
2. sélectionne les `k` lignes les plus proches ;
3. utilise leurs labels pour prédire.

Donc KNN est un modèle basé sur la proximité.

On parle souvent de méthode **non paramétrique**.

Cela ne veut pas dire qu'il n'y a aucun réglage.

Il y a bien des paramètres comme `k`.

Mais KNN ne résume pas le phénomène dans une équation simple comme :

```text
y = ax + b
```

Il raisonne surtout par comparaison avec les exemples gardés en mémoire.

---

## 8. Que veut dire "proche" ?

Pour savoir si deux lignes sont proches, KNN calcule une distance.

Exemple avec deux logements :

| Logement | Surface | Pièces |
| -------- | ------- | ------ |
| A        | 75      | 3      |
| B        | 80      | 3      |

Ils sont proches :

```text
surface proche
nombre de pièces identique
```

Autre exemple :

| Logement | Surface | Pièces |
| -------- | ------- | ------ |
| A        | 75      | 3      |
| C        | 130     | 6      |

Ils sont moins proches.

KNN transforme cette intuition en calcul numérique.

---

## 9. Distance euclidienne

La distance la plus courante est la distance euclidienne.

Avec deux variables :

```text
distance = √((surface_a - surface_b)² + (pieces_a - pieces_b)²)
```

Idée :

```text
Plus la distance est petite, plus les lignes sont proches.
```

KNN classe ensuite les lignes par distance croissante.

---

## 10. KNN pour classification

En classification, le label est une catégorie.

Exemple Iris :

```text
mesures d'une fleur → espèce
```

Si `k = 5`, KNN regarde les 5 fleurs les plus proches.

Puis il fait un vote.

Exemple :

| Voisin | Espèce     |
| ------ | ---------- |
| 1      | versicolor |
| 2      | versicolor |
| 3      | virginica  |
| 4      | versicolor |
| 5      | virginica  |

Résultat :

```text
versicolor gagne avec 3 votes sur 5
```

En Python :

```python
from sklearn.neighbors import KNeighborsClassifier

modele = KNeighborsClassifier(n_neighbors=5)
modele.fit(X_train, y_train)
```

---

## 11. KNN pour régression

En régression, le label est une valeur numérique.

Exemple :

```text
caractéristiques d'un logement → prix
```

Si `k = 3`, KNN prend les 3 logements les plus proches.

Puis il calcule souvent la moyenne de leurs prix.

Exemple :

| Voisin | Prix   |
| ------ | ------ |
| 1      | 250000 |
| 2      | 270000 |
| 3      | 310000 |

Prédiction :

```text
(250000 + 270000 + 310000) / 3 = 276666
```

En Python :

```python
from sklearn.neighbors import KNeighborsRegressor

modele = KNeighborsRegressor(n_neighbors=3)
modele.fit(X_train, y_train)
```

---

## 12. Pourquoi normaliser ?

KNN utilise des distances.

Donc l'échelle des colonnes a un impact direct.

Exemple :

| Variable          | Écart possible |
| ----------------- | -------------- |
| surface           | 10             |
| pièces            | 1              |
| revenu_quartier   | 15000          |

Si on calcule une distance brute, `revenu_quartier` peut dominer.

Le modèle risque alors de choisir les voisins surtout parce qu'ils ont un revenu de quartier proche, même si la surface ou le nombre de pièces sont différents.

Question pratique :

```text
Est-ce que je veux vraiment que la colonne avec les plus grands nombres décide presque seule de la proximité ?
```

Souvent, la réponse est non.

---

## 13. StandardScaler

Pour éviter qu'une variable domine uniquement à cause de son échelle, on normalise.

Avec `StandardScaler`, chaque colonne est transformée pour avoir :

```text
moyenne ≈ 0
écart-type ≈ 1
```

Code :

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_normalise = scaler.fit_transform(X_train)
X_test_normalise = scaler.transform(X_test)
```

Règle importante :

```text
fit_transform sur le train
transform sur le test
```

Pourquoi ?

Parce que le test doit rester une donnée non vue.

On ne doit pas utiliser les informations du test pour préparer l'entraînement.

---

## 14. Choisir k

`k` est le nombre de voisins utilisés.

Il ne correspond pas au nombre de critères.

Dans Iris :

```text
features = 4 mesures de la fleur
k = nombre de fleurs voisines utilisées pour voter
```

Si le train contient `120` fleurs et que `k = 5`, KNN compare la nouvelle fleur aux `120` fleurs, puis garde les `5` plus proches.

### Interprétation mathématique

`k` définit la taille du voisinage local autour du point à prédire.

```text
k petit  → voisinage très local
k grand  → voisinage plus large
```

Si `k` est trop petit :

```text
Le modèle peut être très sensible au bruit.
```

Exemple :

```text
k = 1
```

Le modèle copie presque le voisin le plus proche.

Si ce voisin est atypique, la prédiction peut être mauvaise.

Si `k` est trop grand :

```text
Le modèle devient trop général.
```

Il prend en compte des voisins parfois trop éloignés.

Compromis :

```text
k petit  → modèle très local
k grand  → modèle plus lissé
```

### La recette pratique

On ne devine pas `k` parfaitement à l'avance.

On teste plusieurs valeurs, puis on compare les performances.

Exemple :

```python
from sklearn.neighbors import KNeighborsClassifier

for k in [1, 3, 5, 7, 9, 11]:
    modele = KNeighborsClassifier(n_neighbors=k)
    modele.fit(X_train, y_train)
    score_test = modele.score(X_test, y_test)
    print(k, score_test)
```

Puis on choisit une valeur de `k` qui donne un bon score test.

En classification binaire, on utilise souvent un nombre impair :

```text
k = 3, 5, 7, 9
```

Cela limite les égalités de vote.

Mais ce n'est pas une règle absolue.

Pour Iris, `k = 5` est un choix pédagogique raisonnable :

```text
assez petit pour rester local
assez grand pour ne pas dépendre d'un seul voisin
```

---

## 15. Évaluer KNN

Comme pour la régression linéaire, on sépare train et test.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Puis :

```python
modele.fit(X_train, y_train)
score_test = modele.score(X_test, y_test)
```

En classification, `score` correspond généralement à l'accuracy :

```text
proportion de bonnes prédictions
```

En régression, `score` correspond au coefficient R².

On peut aussi utiliser :

- `mean_absolute_error` pour une régression ;
- `accuracy_score` ou une matrice de confusion pour une classification.

---

## 16. Pipeline conseillé

Quand on combine normalisation et KNN, l'ordre des étapes compte.

Schéma :

```text
Dataset
  ↓
Séparer X et y
  ↓
Train/test split
  ↓
Normaliser X_train avec fit_transform
  ↓
Normaliser X_test avec transform
  ↓
Entraîner KNN sur X_train normalisé
  ↓
Évaluer sur X_test normalisé
```

Ce pipeline évite de mélanger les données de test avec les données d'entraînement.

---

## 17. Limites de KNN

KNN est simple à comprendre, mais il a des limites.

### Sensible à l'échelle

Sans normalisation, les distances peuvent être dominées par certaines colonnes.

### Sensible aux variables inutiles

Si on ajoute des colonnes sans lien avec le problème, elles peuvent perturber les distances.

### Coût à la prédiction

KNN garde les exemples d'entraînement.

Pour prédire, il doit comparer la nouvelle donnée à beaucoup d'exemples.

Avec un très grand dataset, cela peut devenir coûteux.

### Choix de k

Le résultat dépend de `n_neighbors`.

Il faut tester plusieurs valeurs.

---

## 18. Analogie : raisonner par cas similaires

On peut comparer deux approches.

### Médecin A : approche KNN

```text
Ce patient ressemble beaucoup à 50 patients déjà vus.
Je vais utiliser le diagnostic le plus fréquent parmi ces cas.
```

Cette approche raisonne par analogie.

### Médecin B : approche avec modèle explicatif

```text
J'ai construit une théorie qui explique la relation entre les symptômes et la maladie.
```

Cette approche raisonne par modélisation.

Les deux approches peuvent être utiles.

KNN représente une forme très pure de raisonnement par cas similaires.

---

## 19. Lien avec les systèmes modernes

L'idée de KNN reste très actuelle.

Dans les systèmes modernes, on représente souvent des textes, images ou documents par des vecteurs.

On appelle souvent ces vecteurs des **embeddings**.

Puis on cherche les éléments les plus proches dans cet espace vectoriel.

Exemples :

- recherche d'images similaires ;
- recommandation de produits ;
- recherche sémantique ;
- RAG avec recherche de documents proches d'une question.

L'idée de fond reste proche de KNN :

```text
Les choses qui se ressemblent sont proches dans un espace mathématique.
```

---

## 20. Règles pratiques

À retenir :

- KNN prédit à partir des voisins les plus proches.
- La notion de proximité dépend d'une distance.
- Si les colonnes n'ont pas la même échelle, il faut souvent normaliser.
- Pour KNN, `StandardScaler` est souvent utile.
- On entraîne sur le train.
- On évalue sur le test.
- On ne normalise jamais le test avec `fit_transform`.
- `k` doit être choisi expérimentalement.

---

## 21. Exercice pratique

Notebooks :

- [Énoncé : KNN avec Iris](notebooks/03_knn_iris_enonce.ipynb)
- [Correction : KNN avec Iris](notebooks/corrections/03_knn_iris_correction.ipynb)

- [Énoncé : choisir k et normaliser](notebooks/04_knn_k_normalisation_enonce.ipynb)
- [Correction : choisir k et normaliser](notebooks/corrections/04_knn_k_normalisation_correction.ipynb)

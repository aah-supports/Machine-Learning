# Chapitre 4 : KNN, voisins et normalisation

Dans KNN, il faut distinguer :

les variables explicatives (les caractéristiques du vecteur X)
le label (la réponse y)

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

## 3. L'intuition derrière KNN

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

Deux individus très semblables peuvent parfois produire des résultats très différents. Par exemple, deux étudiants ayant effectué un nombre d'heures de travail équivalent peuvent obtenir des notes très différentes. Dans ce cas, la proximité des variables n'implique pas nécessairement une proximité des résultats, ce qui limite l'efficacité de KNN.

| Heures | Résultat (label) |
| ------ | -------- |
| 5      | Réussite |
| 5.1    | Échec    |
| 5.2    | Réussite |
| 5.3    | Échec    |

Des élèves très proches ont des résultats opposés.

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

Il raisonne surtout par comparaison avec les exemples gardés en mémoire.

### Exercice 

Pour `k=1`, puis pour `k=3`, décidez à quel statut appartient Alan ? 

```python
import pandas as pd

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

---

## 8. Exemple (vrais données)  : Iris

Le dataset **Iris** est un grand classique du Machine Learning.

Il a été utilisé par Ronald Fisher en 1936.

Le problème :

```text
mesures d'une fleur → espèce
```

On a trois espèces :

- Iris Setosa ;
- Iris Versicolor ;
- Iris Virginica.

Pour chaque fleur, on mesure :

| Variable     | Signification      |
| ------------ | ------------------ |
| Sepal Length | Longueur du sépale |
| Sepal Width  | Largeur du sépale  |
| Petal Length | Longueur du pétale |
| Petal Width  | Largeur du pétale  |

Exemples de fleurs connues :

| Sepal L | Sepal W | Petal L | Petal W | Espèce     |
| ------- | ------- | ------- | ------- | ---------- |
| 5.1     | 3.5     | 1.4     | 0.2     | Setosa     |
| 4.9     | 3.0     | 1.4     | 0.2     | Setosa     |
| 6.0     | 2.9     | 4.5     | 1.5     | Versicolor |
| 6.5     | 3.0     | 5.8     | 2.2     | Virginica  |

Chaque fleur devient donc un point dans un espace à 4 dimensions :

```text
(longueur sépale, largeur sépale, longueur pétale, largeur pétale)
```

---

## 9. Nouvelle fleur à classer

On reçoit une nouvelle fleur :

| Sepal L | Sepal W | Petal L | Petal W |
| ------- | ------- | ------- | ------- |
| 5.9     | 3.0     | 4.2     | 1.5     |

Sous forme de vecteur :

```text
(5.9, 3.0, 4.2, 1.5)
```

On ne connaît pas son espèce.

KNN doit la prédire en comparant cette fleur aux fleurs connues du train.

---

## 10. Calculer les distances

On compare la nouvelle fleur avec quelques fleurs connues.

### Fleur A : Setosa

```text
(5.1, 3.5, 1.4, 0.2)
```

Différences avec la nouvelle fleur :

```text
0.8, 0.5, 2.8, 1.3
```

Distance :

```text
≈ 3.20
```

### Fleur B : Versicolor

```text
(6.0, 2.9, 4.5, 1.5)
```

Différences :

```text
0.1, 0.1, 0.3, 0.0
```

Distance :

```text
≈ 0.33
```

### Fleur C : Virginica

```text
(6.5, 3.0, 5.8, 2.2)
```

Différences :

```text
0.6, 0.0, 1.6, 0.7
```

Distance :

```text
≈ 1.85
```

La formule générale de distance a déjà été donnée plus haut.

Ici, on l'applique aux 4 mesures de la fleur.

---

## 11. Trouver les voisins

On classe les fleurs par distance croissante.

| Fleur | Espèce     | Distance |
| ----- | ---------- | -------- |
| B     | Versicolor | 0.33     |
| C     | Virginica  | 1.85     |
| A     | Setosa     | 3.20     |

Le plus proche voisin est :

```text
Versicolor
```

Si `k = 1`, KNN prend seulement ce voisin.

La prédiction est donc :

```text
Versicolor
```

---

## 12. KNN pour classification

En classification, le label est une catégorie.

Si `k = 5`, KNN regarde les 5 fleurs les plus proches.

Puis il fait un vote.

Déroulé complet :

1. Une nouvelle fleur arrive.
2. On calcule sa distance avec toutes les fleurs connues du train.
3. On trie toutes les fleurs connues de la plus proche à la plus éloignée.
4. On garde seulement les `k` plus proches.
5. On regarde les catégories de ces `k` voisins.
6. La catégorie majoritaire gagne.

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

KNN ne connaît rien à la botanique.

Il applique simplement :

1. calculer les distances ;
2. trouver les `k` voisins les plus proches ;
3. faire voter les voisins ;
4. retourner la classe majoritaire.

Question qu'il se pose :

```text
Parmi toutes les fleurs que j'ai déjà vues,
lesquelles ressemblent le plus à celle-ci ?
```

---

## 13. KNN pour régression

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

## 14. Pourquoi normaliser ?

KNN utilise des distances.

Donc l'échelle des colonnes a un impact direct.

Prenons un exemple volontairement simple.

On veut prédire si une personne aime un film.

Dataset :

| Personne | Âge | Salaire (€) | Aime le film |
| -------- | --- | ----------- | ------------ |
| A | 20 | 20000 | Oui |
| B | 25 | 25000 | Oui |
| C | 60 | 100000 | Non |

Nouvelle personne :

| Âge | Salaire (€) |
| --- | ----------- |
| 22 | 90000 |

### Sans normalisation

Distance avec la personne A :

```text
d(A) = sqrt((22 - 20)^2 + (90000 - 20000)^2)
d(A) ≈ 70000
```

Distance avec la personne C :

```text
d(C) = sqrt((22 - 60)^2 + (90000 - 100000)^2)
d(C) ≈ 10000
```

KNN conclut donc :

```text
voisin le plus proche -> personne C
prédiction -> Non
```

Pourtant, en âge, la nouvelle personne ressemble beaucoup plus à A :

```text
nouvelle personne : 22 ans
personne A        : 20 ans
personne C        : 60 ans
```

Le salaire a écrasé l'âge dans le calcul de distance, simplement parce qu'il est exprimé en grands nombres.

### Après normalisation

Après normalisation, chaque variable est remise sur une échelle comparable.

Exemple de valeurs normalisées :

| Personne | Âge normalisé | Salaire normalisé |
| -------- | ------------- | ----------------- |
| A | -0.8 | -0.9 |
| B | -0.6 | -0.7 |
| C | 1.4 | 1.3 |
| Nouvelle | -0.7 | 1.0 |

Maintenant :

- l'âge compte autant que le salaire ;
- les distances sont plus équilibrées ;
- le voisin choisi peut changer.

Idée à retenir :

```text
Sans normalisation, KNN ne cherche pas forcément les voisins les plus ressemblants.
Il cherche surtout les voisins les plus proches sur les variables qui ont les plus grandes unités.
```

### Exercice

Avec la méthode du min/max retrouvez la colonne normalisée

| Variable | Valeur initiale | Min    | Max     | Valeur normalisée |
| -------- | --------------- | ------ | ------- | ----------------- |
| Surface  | 100             | 50     | 200     | 0.333             |
| Pièces   | 4               | 1      | 8       | 0.429             |
| Revenu   | 50 000          | 20 000 | 100 000 | 0.375             |


```txt
x = (x-min)/(max-min)
```

---



## 15. StandardScaler

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

Ce que fait le code :

```text
fit_transform(X_train)
→ calcule la moyenne et l'écart-type du train
→ transforme le train avec ces valeurs

transform(X_test)
→ transforme le test avec la même moyenne et le même écart-type
```

Pourquoi ?

Parce que le test doit rester une donnée non vue.

On ne doit pas utiliser les informations du test pour préparer l'entraînement.

Exemple concret :

```text
surface_train = [80, 100, 120]
moyenne_train = 100
```

Si une surface de test vaut `110`, on la normalise avec la moyenne du train :

```text
110 - 100 = 10
```

On ne recalcule pas une nouvelle moyenne avec les surfaces du test.

Sinon, le test participe indirectement à la préparation du modèle. L'évaluation devient moins honnête.

---

## 16. Choisir k

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

Dans un vrai projet, on choisit idéalement `k` avec un jeu de validation ou une validation croisée.

Dans ce cours d'introduction, on observe parfois le score test pour comprendre le mécanisme, mais il faut retenir que le test final sert surtout à confirmer la performance du modèle choisi.

Exemple :

```python
from sklearn.neighbors import KNeighborsClassifier

for k in [1, 3, 5, 7, 9, 11]:
    modele = KNeighborsClassifier(n_neighbors=k)
    modele.fit(X_train, y_train)
    score_test = modele.score(X_test, y_test)
    print(k, score_test)
```

Dans l'exercice, ce tableau permet de voir concrètement que `k` change le résultat.

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

## 17. Évaluer KNN

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

## 18. Pipeline conseillé

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

## 19. Limites de KNN

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

## 20. Analogie : raisonner par cas similaires

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

## 21. Lien avec les systèmes modernes

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

## 22. Règles pratiques

À retenir :

- KNN prédit à partir des voisins les plus proches.
- La notion de proximité dépend d'une distance.
- Si les colonnes n'ont pas la même échelle, il faut souvent normaliser.
- Pour KNN, `StandardScaler` est souvent utile.
- On entraîne sur le train.
- On évalue sur le test.
- La normalisation apprend ses paramètres sur le train, puis les applique au test.
- `k` doit être choisi expérimentalement.

---

## 23. Exercice pratique

Notebooks :

- [Énoncé : KNN avec Iris](notebooks/03_knn_iris_enonce.ipynb)
- [Correction : KNN avec Iris, sans normalisation](Corrections/CORRECTION.ipynb)
- [Énoncé : choisir k et normaliser](notebooks/04_knn_k_normalisation_enonce.ipynb)

---

## 24. Transition vers la régression logistique

KNN classe une nouvelle observation en regardant les voisins les plus proches.

La régression logistique va proposer une autre logique :

```text
apprendre une séparation
puis transformer le score en probabilité
```

Elle garde l'idée de classification, mais elle introduit les notions de poids, biais et sigmoïde.

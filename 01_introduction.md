# Introduction au Machine Learning

## 1. Situer l'IA, le Machine Learning, les réseaux de neurones et les LLM

Avant de commencer, il faut distinguer plusieurs termes souvent mélangés.

L'**Intelligence Artificielle (IA)** est le domaine le plus large.

Son objectif est de construire des systèmes capables de réaliser des tâches que l'on associe habituellement à l'intelligence humaine :

- reconnaître une image ;
- comprendre un texte ;
- prendre une décision ;
- recommander un contenu ;
- prédire une valeur.

Le **Machine Learning (ML)** est une partie de l'IA.

L'idée centrale du ML est simple :

```text
au lieu d'écrire toutes les règles à la main,
on apprend un modèle à partir de données.
```

Les **réseaux de neurones** sont une famille particulière de modèles de Machine Learning.

Ils sont composés de couches de calcul qui apprennent progressivement des représentations utiles dans les données.

Ils sont très utilisés pour :

- les images ;
- le son ;
- le texte ;
- les grands volumes de données.

Les **LLM** (*Large Language Models*) sont des grands modèles de langage.

Ils reposent sur des réseaux de neurones très grands, entraînés sur d'immenses quantités de textes.

ChatGPT, Claude, Gemini ou Mistral appartiennent à cette famille.

On peut donc retenir cette carte :

```text
Intelligence Artificielle
└── Machine Learning
    ├── Régression linéaire
    ├── KNN
    ├── Arbres de décision
    └── Réseaux de neurones
        └── LLM
```

Dans ce cours, nous ne faisons pas encore des LLM.

Nous faisons du **Machine Learning classique**.

Nous allons apprendre les bases :

- préparer des données ;
- entraîner un modèle ;
- faire une prédiction ;
- mesurer l'erreur ;
- comprendre pourquoi un modèle peut se tromper.

---

## 2. Repère historique rapide

L'IA n'est pas née avec ChatGPT.

Quelques dates clés, avec le contexte :

| Date | Repère | Contexte rapide |
| ---- | ------ | --------------- |
| 1950 | Alan Turing publie une question fondatrice. | Il ne demande pas seulement si une machine "pense", mais si elle peut imiter une conversation humaine de manière crédible. |
| 1956 | Conférence de Dartmouth. | Le terme **Intelligence Artificielle** est popularisé. L'IA devient un champ de recherche identifié. |
| 1958 | Frank Rosenblatt présente le **perceptron**. | C'est un ancêtre des réseaux de neurones : une machine apprend à séparer des exemples simples. |
| Années 1970-1980 | Développement des **systèmes experts**. | L'IA repose surtout sur des règles écrites par des spécialistes : "si symptôme A et symptôme B, alors diagnostic C". |
| 1986 | Diffusion de la **rétropropagation**. | Les réseaux de neurones redeviennent intéressants, car on sait mieux ajuster leurs paramètres à partir des erreurs. |
| Années 1990-2000 | Essor du **Machine Learning statistique**. | Les modèles apprennent davantage à partir des données : arbres, SVM, forêts aléatoires, méthodes d'évaluation. |
| 2012 | AlexNet gagne une compétition majeure de vision par ordinateur. | Le deep learning montre sa puissance avec beaucoup de données, des cartes graphiques et des réseaux plus profonds. |
| 2017 | Publication de l'architecture **Transformer**. | Cette architecture devient la base de nombreux grands modèles de langage modernes. |
| 2020 | GPT-3 montre les capacités des modèles de langage à grande échelle. | Les LLM deviennent capables de produire du texte, répondre à des questions et généraliser à de nombreuses tâches. |
| 2022 | ChatGPT popularise les LLM auprès du grand public. | L'IA générative devient un outil visible dans le travail, l'éducation, le code et la création de contenu. |

On peut résumer l'évolution ainsi :

```text
IA symbolique      → écrire des règles
Machine Learning   → apprendre depuis des données
Deep Learning      → apprendre avec de grands réseaux de neurones
LLM                → grands réseaux spécialisés dans le langage
```

Ce cours se place principalement dans l'étape **Machine Learning statistique**.

On commence par des modèles simples, car ils permettent de comprendre les principes qui restent valables ensuite :

- données d'entraînement ;
- généralisation ;
- test ;
- erreur ;
- choix des variables ;
- limites du modèle.

---

## 3. Qu'est-ce que le Machine Learning ?

Le **Machine Learning (ML)** est une branche de l'Intelligence Artificielle qui permet à une machine d'apprendre à partir de données sans être explicitement programmée pour chaque cas.

### Programmation classique

```text
Règles + Données
        ↓
     Programme
        ↓
      Résultat
```

Exemple :

```python
if temperature > 30:
    print("Chaud")
```

Le développeur écrit toutes les règles.

---

### Machine Learning

```text
Données + Résultats attendus
            ↓
      Algorithme ML
            ↓
         Modèle
            ↓
      Prédictions
```

Exemple :

On montre à l'algorithme :

| Surface | Prix      |
| ------- | --------- |
| 50 m²   | 200 000 € |
| 80 m²   | 320 000 € |
| 100 m²  | 400 000 € |

Il apprend la relation entre surface et prix.

---

## 4. Vocabulaire essentiel

### Donnée (Data)

Information utilisée pour entraîner le modèle.

Exemple :

```text
Age = 35
Salaire = 2500€
```

---

### Feature

Caractéristique utilisée pour prédire.

Pour un logement :

- Surface
- Nombre de pièces
- Ville
- Étage

---

### Label

Valeur à prédire.

Exemple :

```text
Prix du logement
```

---

### Dataset

Ensemble des données.

| Surface | Pièces | Prix   |
| ------- | ------ | ------ |
| 50      | 2      | 200000 |
| 80      | 3      | 320000 |
| 100     | 4      | 400000 |

---

### Modèle

Objet mathématique appris par l'algorithme.

Une fois entraîné on peut demander au modèle de prédire un prix pour une surface donnée.

```python
prix = modele.predict([70])
```

---

## 5. Les grandes familles de Machine Learning

### 1. Apprentissage supervisé

On possède :

- les données
- les bonnes réponses

Exemple :

| Email        | Spam |
| ------------ | ---- |
| Gagnez 1000€ | Oui  |
| Bonjour      | Non  |

Le modèle apprend à détecter les spams.

---

### 2. Apprentissage non supervisé

Pas de réponse connue.

Le modèle cherche des groupes ou structures.

Exemple :

Segmentation clients :

```text
Groupe A : étudiants
Groupe B : retraités
Groupe C : cadres
```

---

### 3. Apprentissage par renforcement

Un agent agit dans un environnement.

Il reçoit :

- récompense
- pénalité

Exemple :

- Jeux vidéo
- Robotique
- Voiture autonome

---

## 6. Régression et Classification

### Régression

Prédire une valeur numérique.

Exemples :

- Prix d'une maison
- Température
- Chiffre d'affaires

Fonction typique :

```txt
y = ax + b
```

---

### Classification

Prédire une catégorie.

Exemples :

* Spam / Non spam
* Malade / Sain
* Chien / Chat

Résultat :

```text
Classe = Chat
```

---

## 7. Le cycle complet d'un projet ML

### Étape 1 : Collecte des données

Sources :

- Base SQL
- API
- CSV
- Capteurs

---

### Étape 2 : Nettoyage

Exemple, dans un dataset on peut rencontrer 

```text
Age = NULL
Salaire = ????
```

On corrige :

- valeurs manquantes
- doublons
- erreurs

---

### Étape 3 : Préparation

La préparation consiste à transformer les données brutes en données exploitables par un modèle.

Un modèle ne comprend pas directement les mots. Il faut donc convertir les valeurs textuelles en valeurs numériques.

#### Exemple 1 : transformer une ville en nombre

```text
Paris → 1
Lyon → 2
Marseille → 3
```

Cette transformation est simple, mais elle peut poser un problème.

Le modèle peut croire que :

```text
Marseille > Lyon > Paris
```

Or une ville n'est pas plus grande qu'une autre dans ce contexte. Ce sont seulement des catégories.

Pour des villes, on préfère souvent utiliser des vecteurs avec la méthode appelée **One-Hot Encoding**.

```text
Ville       Paris   Lyon   Marseille
Paris       1       0      0
Lyon        0       1      0
Marseille   0       0      1
```

Chaque ville possède sa propre colonne.

Exemple :

| Surface | Ville     | Prix   |
| ------- | --------- | ------ |
| 50      | Paris     | 300000 |
| 80      | Lyon      | 280000 |
| 100     | Marseille | 250000 |

Après transformation :

| Surface | Paris | Lyon | Marseille | Prix   |
| ------- | ----- | ---- | --------- | ------ |
| 50      | 1     | 0    | 0         | 300000 |
| 80      | 0     | 1    | 0         | 280000 |
| 100     | 0     | 0    | 1         | 250000 |

Le modèle peut maintenant utiliser la ville sans croire qu'il existe un ordre entre les villes.

#### Exemple 2 : normaliser les valeurs numériques

La normalisation sert à mettre les valeurs sur une échelle comparable.

Exemple de données brutes :

| Logement | Surface | Pièces | Prix   |
| -------- | ------- | ------ | ------ |
| A        | 70      | 3      | 200000 |
| B        | 80      | 4      | 250000 |

Sans normalisation, les différences entre les deux logements sont :

```txt
Différence de surface : 80 - 70 = 10
Différence de pièces  : 4 - 3 = 1
Différence de prix    : 250000 - 200000 = 50000
```

Le prix a des nombres beaucoup plus grands que les autres colonnes. Pour certains modèles, comme KNN ou SVM, cette colonne peut donc dominer les calculs.

##### Pourquoi c'est important avec KNN ?

KNN signifie **K Nearest Neighbors**, c'est-à-dire **K plus proches voisins**.

Le principe est simple : pour prédire une nouvelle valeur, le modèle cherche les exemples connus qui ressemblent le plus à la nouvelle donnée.

Exemple :

```text
On veut prédire le prix d'un logement de 75 m² avec 3 pièces.
```

Le modèle regarde les logements déjà connus :

| Logement | Surface | Pièces | Prix   |
| -------- | ------- | ------ | ------ |
| A        | 70      | 3      | 210000 |
| B        | 80      | 3      | 240000 |
| C        | 150     | 6      | 500000 |

KNN va considérer que le logement à prédire ressemble plus à A et B qu'à C.

Il peut donc prédire un prix proche de A et B :

```text
Prix prédit ≈ 225000
```

Mais KNN utilise une distance entre les lignes pour savoir quels logements sont les plus proches.

Si on compare ces deux logements :

```text
Logement à prédire :
surface = 75
pièces = 3
revenu_quartier = 30000

Logement connu :
surface = 80
pièces = 4
revenu_quartier = 45000
```

Les différences sont :

```text
surface         : 5
pièces          : 1
revenu_quartier : 15000
```

Sans normalisation, `15000` écrase les autres différences. KNN risque alors de considérer que le revenu du quartier est presque le seul critère important.

La normalisation permet d'éviter qu'une colonne devienne importante uniquement parce que ses nombres sont plus grands.

Après normalisation entre 0 et 1, on obtient par exemple :

| Logement | Surface normalisée | Pièces normalisées | Prix normalisé |
| -------- | ------------------ | ------------------ | -------------- |
| A        | 0.0                | 0.0                | 0.0            |
| B        | 1.0                | 1.0                | 1.0            |

Les colonnes sont maintenant sur une échelle comparable.

Autre exemple avec trois surfaces :

```txt
Surface brute       : 20, 50, 100
Surface normalisée  : 0, 0.375, 1
```

Cela ne change pas l'information de départ. Cela change seulement l'échelle.

#### Exemple 3 : prédire avec des données normalisées

Si le modèle apprend avec des données normalisées, il faut aussi normaliser les nouvelles données avant de prédire.

```python
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

X = [[20], [50], [100]]
y = [100000, 250000, 500000]

scaler = MinMaxScaler()
X_normalise = scaler.fit_transform(X)

modele = LinearRegression()
modele.fit(X_normalise, y)

surface = [[70]]
surface_normalisee = scaler.transform(surface)

prix = modele.predict(surface_normalisee)
```

Le modèle n'a pas appris sur `70`, il a appris sur la version normalisée de `70`.

#### Quand faut-il normaliser ?

On normalise souvent pour :

- KNN
- SVM
- régression logistique
- réseaux de neurones
- K-Means
- PCA

Ces modèles utilisent des distances, des coefficients ou des calculs sensibles à l'échelle.

On normalise moins souvent pour :

- arbre de décision
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM

Ces modèles découpent les données avec des règles du type :

```text
surface > 70 ?
```

Ils sont donc moins sensibles aux différences d'échelle.

Donc résumé :

- **Transformation** = convertir les textes en nombres.
- **Normalisation** = mettre les nombres sur une même échelle, souvent entre 0 et 1.

*Remarque : on ne normalise pas systématiquement. On normalise surtout quand le modèle est sensible à l'échelle des valeurs.*

Exercice pratique :

- [Énoncé : nettoyage de données](notebooks/00_nettoyage_donnees_enonce.ipynb)
- [Énoncé : régression linéaire](notebooks/01_regression_lineaire_enonce.ipynb)
- [Énoncé : train / test split](notebooks/02_train_test_split_enonce.ipynb)
- [Énoncé : régression logistique](notebooks/03_regression_logistique_enonce.ipynb)
- [Énoncé : KNN avec Iris](notebooks/03_knn_iris_enonce.ipynb)
- [Énoncé : KNN, k et normalisation](notebooks/04_knn_k_normalisation_enonce.ipynb)

---

### Étape 4 : Entraînement

Le modèle apprend sur les données.

```python
model.fit(X_train, y_train)
```

---

### Étape 5 : Évaluation

On teste sur des données jamais vues.

```python
model.score(X_test, y_test)
```

---

### Étape 6 : Déploiement

API REST :

```text
POST /predict
```

Application web :

```text
React
↓
FastAPI
↓
Modèle ML
```

---

## 8. Exemple concret : Prédiction du prix d'un logement

Dataset :

| Surface | Prix   |
| ------- | ------ |
| 50      | 200000 |
| 80      | 320000 |
| 100     | 400000 |

Entraînement :

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)
```

Prédiction :

```python
model.predict([[70]])
```

Résultat :

```text
280000 €
```

---

## 9. Algorithmes à connaître

### Régression

* Linear Regression
* Ridge
* Lasso

### Classification

* Logistic Regression
* Decision Tree
* Random Forest
* SVM
* KNN

### Clustering

* K-Means
* DBSCAN

### Deep Learning

* Réseaux de neurones
* CNN
* RNN
* Transformers

---

## 10. Outils Python incontournables

### NumPy

Calcul matriciel.

```python
import numpy as np
```

---

### Pandas

Manipulation des données.

```python
import pandas as pd
```

---

### Matplotlib

Graphiques.

```python
import matplotlib.pyplot as plt
```

---

### Scikit-Learn

Machine Learning classique.

```python
from sklearn import *
```

---

### TensorFlow / PyTorch

Deep Learning.

```python
import tensorflow as tf
```

ou

```python
import torch
```

---

## 11. Pourquoi les mathématiques sont importantes ?

Le Machine Learning repose principalement sur :

- Algèbre linéaire (vecteurs, matrices)
- Probabilités
- Statistiques
- Optimisation

Par exemple, lors de l'entraînement, le modèle cherche à minimiser une erreur :

Erreur = Valeur\ réelle - Valeur\ prédite

---

## 12. Suite du cours

Après cette introduction, le prochain chapitre conseillé est :

- [Chapitre 2 : Préparer et nettoyer les données](02_preparation_donnees.md)

Cette étape permet de comprendre ce qui vient avant le modèle :

- inspecter un dataset ;
- corriger les valeurs incohérentes ;
- préparer les variables ;
- éviter les erreurs métier avant l'entraînement.

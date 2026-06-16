# ============================================================
# Correction 03 : comprendre KNN avec le dataset Iris
# ============================================================

# Objectif :
# Utiliser l'algorithme KNN pour prédire l'espèce d'une fleur.
# KNN signifie K Nearest Neighbors, c'est-à-dire :
# "les K plus proches voisins".
#
# L'idée :
# - on connaît déjà des fleurs avec leurs mesures et leur espèce ;
# - une nouvelle fleur arrive ;
# - on cherche les fleurs les plus proches ;
# - on fait voter leurs espèces ;
# - l'espèce majoritaire devient la prédiction.

# ------------------------------------------------------------
# 1. Importer les bibliothèques nécessaires
# ------------------------------------------------------------

import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# ------------------------------------------------------------
# 2. Charger le dataset Iris
# ------------------------------------------------------------

iris = load_iris()

# X contient les variables explicatives.
# Ce sont les informations utilisées pour faire une prédiction.
#
# Dans Iris, chaque fleur est décrite par 4 mesures :
# - longueur du sépale
# - largeur du sépale
# - longueur du pétale
# - largeur du pétale

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# y contient la variable cible.
# C'est ce que l'on cherche à prédire.
#
# Dans Iris :
# 0 = setosa
# 1 = versicolor
# 2 = virginica

y = pd.Series(iris.target)


# ------------------------------------------------------------
# 3. Afficher les premières lignes du dataset
# ------------------------------------------------------------

print("Premières lignes de X :")
print(X.head())

print("\nNoms des espèces :")
print(iris.target_names)


# ------------------------------------------------------------
# 4. Séparer les données en train et test
# ------------------------------------------------------------

# On sépare les données en deux parties :
#
# X_train : caractéristiques des fleurs utilisées pour apprendre
# y_train : vraies espèces des fleurs utilisées pour apprendre
#
# X_test  : caractéristiques des fleurs gardées pour tester
# y_test  : vraies espèces des fleurs gardées pour tester
#
# test_size=0.2 signifie :
# - 80 % des données pour l'entraînement
# - 20 % des données pour le test
#
# random_state=42 fixe le hasard.
# Cela permet d'obtenir toujours le même découpage.
#
# stratify=y permet de garder une bonne répartition des espèces
# dans le train et dans le test.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nDimensions des données :")
print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)


# ------------------------------------------------------------
# 5. Créer le modèle KNN
# ------------------------------------------------------------

# n_neighbors=5 signifie :
# le modèle regarde les 5 fleurs les plus proches.
#
# Attention :
# cela ne veut pas dire qu'il utilise 5 variables.
# Il utilise bien les 4 mesures de chaque fleur.
#
# Le nombre 5 correspond seulement au nombre de voisins.

modele = KNeighborsClassifier(n_neighbors=5)


# ------------------------------------------------------------
# 6. Entraîner le modèle
# ------------------------------------------------------------

# Avec KNN, "entraîner" signifie surtout mémoriser les données.
# Le modèle garde X_train et y_train en mémoire.
#
# Ensuite, quand une nouvelle fleur arrive,
# il compare cette fleur aux fleurs de X_train.

modele.fit(X_train, y_train)


# ------------------------------------------------------------
# 7. Évaluer le modèle sur les données de test
# ------------------------------------------------------------

# Le score correspond à la proportion de bonnes réponses.
#
# Exemple :
# score = 0.966 signifie que le modèle a bien classé
# environ 96,6 % des fleurs du test.

score_test = modele.score(X_test, y_test)

print("\nScore sur les données de test :")
print(score_test)


# ------------------------------------------------------------
# 8. Prendre une fleur inconnue pour le modèle
# ------------------------------------------------------------

# On prend une fleur dans X_test.
# Elle est "inconnue" car le modèle n'a pas appris avec X_test.

index = X_test.index[0]

# On récupère les mesures de cette fleur.
# Les doubles crochets [[index]] permettent de garder un DataFrame,
# car scikit-learn attend souvent un tableau à 2 dimensions.

nouvelle_fleur = X_test.loc[[index]]

# On récupère aussi la vraie espèce pour vérifier ensuite.

vraie_classe = y_test.loc[index]

print("\nNouvelle fleur à classer :")
print(nouvelle_fleur)


# ------------------------------------------------------------
# 9. Faire une prédiction
# ------------------------------------------------------------

prediction = modele.predict(nouvelle_fleur)

print("\nRésultat de la prédiction :")
print("Vraie espèce   :", iris.target_names[vraie_classe])
print("Espèce prédite :", iris.target_names[prediction[0]])


# ------------------------------------------------------------
# 10. Observer les voisins utilisés par KNN
# ------------------------------------------------------------

# kneighbors permet de voir concrètement les voisins utilisés.
#
# distances contient les distances entre la nouvelle fleur
# et ses 5 plus proches voisines.
#
# indices contient les positions de ces voisines dans X_train.

distances, indices = modele.kneighbors(nouvelle_fleur)

# On récupère les fleurs voisines dans X_train, ici notre modèle récupère les 5 plus proches

voisins = X_train.iloc[indices[0]].copy()

# On ajoute la distance de chaque voisine.

voisins["distance"] = distances[0]

# On ajoute la classe numérique de chaque voisine.

voisins["classe"] = y_train.iloc[indices[0]].values

# On ajoute le nom de l'espèce pour rendre le tableau lisible.

voisins["espece"] = [
    iris.target_names[classe]
    for classe in voisins["classe"]
]

print("\nLes 5 plus proches voisines :")
print(voisins)


# ------------------------------------------------------------
# 11. Comprendre le vote
# ------------------------------------------------------------

# KNN regarde les espèces des voisines.
# La classe la plus fréquente gagne le vote.

vote = voisins["espece"].value_counts()

print("\nVote des voisines :")
print(vote)

print("\nConclusion :")
print("KNN compare la nouvelle fleur aux fleurs connues.")
print("Il garde les plus proches voisines.")
print("Puis il prédit l'espèce majoritaire parmi ces voisines.")
"""
Correction - Arbre de décision simple avec âge et poids

Objectif :
prédire si une personne fait du sport à partir de son âge et de son poids.
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text


# -----------------------------------------------------
# 1. Créer le dataset
# -----------------------------------------------------

data = pd.DataFrame({
    "age": [18, 20, 22, 24, 26, 60],
    "poids": [65, 70, 95, 75, 100, 80],
    "sport": ["Oui", "Oui", "Non", "Oui", "Non", "Non"]
})

print("Dataset")
print(data)

# -----------------------------------------------------
# 2. Séparer X et y
# -----------------------------------------------------

X = data[["age", "poids"]]
y = data["sport"]

# -----------------------------------------------------
# 3. Entraîner un arbre de décision
# -----------------------------------------------------

modele = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

modele.fit(X, y)

# -----------------------------------------------------
# 4. Prédire une nouvelle personne
# -----------------------------------------------------

nouvelle_personne = pd.DataFrame({
    "age": [25],
    "poids": [90]
})

prediction = modele.predict(nouvelle_personne)

print("\nNouvelle personne")
print(nouvelle_personne)
print("Classe prédite :", prediction[0])

# -----------------------------------------------------
# 5. Lire les règles de l'arbre
# -----------------------------------------------------

regles = export_text(
    modele,
    feature_names=list(X.columns)
)

print("\nRègles apprises")
print(regles)

print("\nConclusion")
print("L'arbre pose des questions du type variable <= seuil.")
print("Il cherche à créer des groupes les plus homogènes possible.")

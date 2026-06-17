"""
=====================================================
EXERCICE CORRIGÉ : RÉGRESSION LOGISTIQUE
Objectif : prédire la réussite à un examen
=====================================================

0 = échec
1 = réussite
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

# -----------------------------------------------------
# 1. Créer le dataset
# -----------------------------------------------------

data = pd.DataFrame({
    "heures_revision": [1, 2, 3, 4, 5, 6, 7, 8],
    "reussite": [0, 0, 0, 0, 1, 1, 1, 1]
})

print("Dataset")
print(data)

# -----------------------------------------------------
# 2. Séparer les variables explicatives et la cible
# -----------------------------------------------------

# X contient les variables explicatives.
X = data[["heures_revision"]]

# y contient la cible à prédire.
y = data["reussite"]

# -----------------------------------------------------
# 3. Créer et entraîner le modèle
# -----------------------------------------------------

modele = LogisticRegression()
modele.fit(X, y)

# -----------------------------------------------------
# 4. Prédire pour un étudiant qui a révisé 4 heures
# -----------------------------------------------------

etudiant_4h = pd.DataFrame({
    "heures_revision": [4]
})

prediction_4h = modele.predict(etudiant_4h)
proba_4h = modele.predict_proba(etudiant_4h)

print("\nÉtudiant avec 4 heures de révision")
print("Classe prédite :", prediction_4h[0])
print("Probabilité échec :", round(proba_4h[0][0], 3))
print("Probabilité réussite :", round(proba_4h[0][1], 3))

# -----------------------------------------------------
# 5. Prédire pour un étudiant qui a révisé 7 heures
# -----------------------------------------------------

etudiant_7h = pd.DataFrame({
    "heures_revision": [7]
})

prediction_7h = modele.predict(etudiant_7h)
proba_7h = modele.predict_proba(etudiant_7h)

print("\nÉtudiant avec 7 heures de révision")
print("Classe prédite :", prediction_7h[0])
print("Probabilité échec :", round(proba_7h[0][0], 3))
print("Probabilité réussite :", round(proba_7h[0][1], 3))

# -----------------------------------------------------
# 6. Afficher les paramètres appris par le modèle
# -----------------------------------------------------

print("\nParamètres du modèle")
print("Coefficient :", modele.coef_[0][0])
print("Intercept :", modele.intercept_[0])

print("\nConclusion")
print("Le coefficient est positif.")
print("Cela signifie que plus les heures de révision augmentent,")
print("plus la probabilité de réussite augmente.")

# Régression linéaire simple avec BMI

Nous allons essayer de prédire la progression du diabète à partir d'une seule variable : l'IMC (*Body Mass Index* ou BMI).

L'objectif est de répondre à la question :

> Le BMI permet-il d'expliquer une partie de la progression du diabète ?

## Code

```python
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
data = load_diabetes(as_frame=True, scaled=False)

X = data.data
y = data.target

# Sélection de la variable BMI
X_bmi = X[["bmi"]]

# Création du modèle
reg = LinearRegression()

# Entraînement
reg.fit(X_bmi, y)

# Prédictions
y_pred = reg.predict(X_bmi)

# Préparation du graphique
df = pd.DataFrame({
    "bmi": X["bmi"],
    "target": y,
    "prediction": y_pred
}).sort_values("bmi")

# Affichage
plt.figure(figsize=(8, 5))

plt.scatter(
    df["bmi"],
    df["target"],
    alpha=0.6
)

plt.plot(
    df["bmi"],
    df["prediction"]
)

plt.xlabel("BMI")
plt.ylabel("Progression du diabète")
plt.title("Régression linéaire : BMI -> Progression du diabète")

plt.show()

# Résultats du modèle
print("Pente :", reg.coef_[0])
print("Intercept :", reg.intercept_)
print("R² :", reg.score(X_bmi, y))
```

---

# Comment lire le graphique ?

Chaque point représente un patient.

* Axe horizontal : BMI du patient.
* Axe vertical : progression du diabète observée.

La droite représente la meilleure relation linéaire trouvée par l'algorithme.

```text
Progression du diabète
^
|
|                          •
|                     •
|                •
|           •
|      •
| •
+---------------------------------> BMI
```

Lorsque le BMI augmente, la droite monte.

Cela signifie que :

> Les patients ayant un BMI plus élevé ont tendance à présenter une progression plus importante du diabète.

---

# Interprétation de la pente

Le modèle apprend une équation de la forme :

\hat y = a \cdot BMI + b

* (a) : pente de la droite ;
* (b) : intercept ;
* (\hat y) : valeur prédite.

Si la pente est positive :

> Une augmentation du BMI entraîne une augmentation de la valeur prédite.

---

# Interprétation du R²

Le coefficient de détermination (R^2) mesure :

> À quel point le modèle parvient à expliquer la réalité observée.

Dans ce cas :

```text
R² ≈ 0.35
```

Cela signifie que :

> Le BMI seul permet d'expliquer environ 35 % des variations observées dans la progression du diabète.

Attention :

* cela ne signifie pas que le BMI est responsable de 35 % du diabète ;
* cela ne signifie pas qu'un patient a « 35 % de diabète ».

Le (R^2) mesure uniquement la qualité du modèle.

---

# Conclusion

Le BMI est une variable utile :

* la corrélation entre BMI et progression du diabète est positive ;
* la droite de régression est croissante ;
* le modèle explique environ 35 % de la variabilité observée.

Cependant :

> Le BMI ne suffit pas à lui seul à expliquer complètement la progression du diabète.

Pour améliorer les prédictions, il faudra utiliser plusieurs variables simultanément (âge, tension artérielle, glycémie, cholestérol, etc.), ce qui nous conduira à la régression linéaire multiple.

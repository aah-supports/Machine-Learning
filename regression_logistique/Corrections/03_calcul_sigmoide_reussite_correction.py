import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def prediction_reussite(x):
    z = -4 + 0.5 * x
    p = sigmoid(z)
    resultat = "Succès" if p >= 0.5 else "Échec"
    return z, p, resultat


print("Cas principal")
print("-------------")

x = 10
z, p, resultat = prediction_reussite(x)

print("heures =", x)
print("z =", z)
print("probabilité =", p)
print("résultat =", resultat)

print()
print("Variante")
print("--------")

for heures in [4, 8, 12]:
    z, p, resultat = prediction_reussite(heures)
    print(
        f"{heures:2d} heures | "
        f"z = {z:4.1f} | "
        f"probabilité = {p:.3f} | "
        f"{resultat}"
    )

print()
print("Conclusion")
print("----------")
print("Le score z peut prendre n'importe quelle valeur.")
print("La sigmoïde transforme ce score en probabilité entre 0 et 1.")
print("On applique ensuite un seuil pour obtenir Succès ou Échec.")

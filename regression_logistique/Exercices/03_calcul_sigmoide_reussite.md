# Exercice 3 : calculer une probabilité avec un modèle logistique

## Objectif

Dans cet exercice, on ne cherche pas encore à entraîner un modèle.

On suppose que les coefficients sont déjà connus.

Le but est de comprendre le mécanisme :

```text
heures de révision
   ↓
score linéaire ax + b
   ↓
sigmoïde
   ↓
probabilité
   ↓
succès / échec
```

---

## Énoncé

On étudie la réussite à un examen en fonction du nombre d'heures de révision.

Le modèle logistique est :

$$
\text{logit}(p) = -4 + 0.5x
$$

où :

- `x` = nombre d'heures révisées ;
- `p` = probabilité de réussite.

La probabilité est obtenue grâce à la sigmoïde :

$$
p = \frac{1}{1+e^{-(-4+0.5x)}}
$$

On souhaite prédire la probabilité de réussite d'un étudiant ayant révisé `10` heures.

---

## Question 1 - Calcul du score

Calculer :

$$
z = -4 + 0.5 \times 10
$$

---

## Question 2 - Calcul de la probabilité

On applique la sigmoïde :

$$
p = \frac{1}{1+e^{-z}}
$$

Utiliser :

```text
e^{-1} ≈ 0.3679
```

Calculer la probabilité de réussite.

---

## Question 3 - Décision

On utilise le seuil suivant :

```text
p >= 0.5  -> succès
p < 0.5   -> échec
```

Quelle est la prédiction finale ?

---

## Vérification Python

Compléter et exécuter :

```python
import numpy as np

x = 10

z = ...

p = ...

print("z =", z)
print("probabilité =", p)

if p >= 0.5:
    print("Succès")
else:
    print("Échec")
```

---

## Variante

Faire les calculs à la main pour les trois cas suivants.

| Heures | z | Probabilité | Résultat |
| ------ | - | ----------- | -------- |
| 4      | ? | ?           | ?        |
| 8      | ? | ?           | ?        |
| 12     | ? | ?           | ?        |

On pourra utiliser les approximations suivantes :

```text
e^2 ≈ 7.389
e^0 = 1
e^-2 ≈ 0.135
```

---

## Question de synthèse

Expliquer avec vos mots pourquoi on ne garde pas directement le score `z`.

Votre réponse doit faire apparaître les mots :

- score ;
- sigmoïde ;
- probabilité ;
- seuil.

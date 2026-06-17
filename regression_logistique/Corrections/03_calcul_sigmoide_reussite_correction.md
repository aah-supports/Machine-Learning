# Correction - Exercice 3 : calculer une probabilité avec un modèle logistique

## Modèle

Le modèle est :

[
\text{logit}(p) = -4 + 0.5x
]

On note :

[
z = -4 + 0.5x
]

Puis on transforme ce score avec la sigmoïde :

[
p = \frac{1}{1+e^{-z}}
]

---

## Question 1 - Calcul du score

Pour un étudiant qui a révisé `10` heures :

[
z = -4 + 0.5 \times 10
]

[
z = -4 + 5
]

[
z = 1
]

Le score vaut donc :

```text
z = 1
```

---

## Question 2 - Calcul de la probabilité

On applique la sigmoïde :

[
p = \frac{1}{1+e^{-1}}
]

On utilise :

[
e^{-1}\approx 0.3679
]

Donc :

[
p=\frac{1}{1+0.3679}
]

[
p=\frac{1}{1.3679}
]

[
p \approx 0.731
]

La probabilité de réussite est donc environ :

```text
73.1 %
```

---

## Question 3 - Décision

Le seuil est :

```text
p >= 0.5  -> succès
p < 0.5   -> échec
```

Ici :

```text
0.731 > 0.5
```

La prédiction est donc :

```text
Succès
```

---

## Vérification Python

```python
import numpy as np

x = 10

z = -4 + 0.5 * x

p = 1 / (1 + np.exp(-z))

print("z =", z)
print("probabilité =", p)

if p >= 0.5:
    print("Succès")
else:
    print("Échec")
```

Sortie :

```text
z = 1.0
probabilité = 0.7310585786300049
Succès
```

---

## Variante

### Cas 1 - `x = 4`

[
z = -4 + 0.5 \times 4
]

[
z = -4 + 2
]

[
z = -2
]

[
p = \frac{1}{1+e^{-(-2)}}
]

[
p = \frac{1}{1+e^2}
]

Avec :

[
e^2 \approx 7.389
]

[
p = \frac{1}{1+7.389}
]

[
p \approx 0.119
]

Résultat :

```text
11.9 % -> échec
```

---

### Cas 2 - `x = 8`

[
z = -4 + 0.5 \times 8
]

[
z = -4 + 4
]

[
z = 0
]

[
p = \frac{1}{1+e^0}
]

[
p = \frac{1}{1+1}
]

[
p = 0.5
]

Résultat :

```text
50 % -> frontière de décision
```

Avec la règle `p >= 0.5`, on prédit :

```text
Succès
```

Mais c'est un cas limite.

---

### Cas 3 - `x = 12`

[
z = -4 + 0.5 \times 12
]

[
z = -4 + 6
]

[
z = 2
]

[
p = \frac{1}{1+e^{-2}}
]

Avec :

[
e^{-2} \approx 0.135
]

[
p = \frac{1}{1+0.135}
]

[
p \approx 0.881
]

Résultat :

```text
88.1 % -> succès
```

---

## Tableau récapitulatif

| Heures | z  | Probabilité | Résultat |
| ------ | -- | ----------- | -------- |
| 4      | -2 | 0.119       | Échec    |
| 8      | 0  | 0.500       | Succès avec seuil `>= 0.5`, mais cas limite |
| 12     | 2  | 0.881       | Succès   |

---

## Question de synthèse

On ne garde pas directement le score `z`, car `z` peut prendre n'importe quelle valeur :

```text
-10, -2, 0, 3, 15, ...
```

Ce n'est pas une probabilité.

La sigmoïde transforme ce score en probabilité entre `0` et `1`.

Ensuite, on applique un seuil pour obtenir une classe :

```text
probabilité -> seuil -> succès ou échec
```

Le mécanisme complet est donc :

```text
x
-> z = ax + b
-> sigmoïde(z)
-> probabilité
-> décision avec un seuil
```

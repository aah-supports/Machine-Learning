# Chapitre 5 : Introduction à la régression logistique

## 1. Objectif du chapitre

Après KNN, nous avons vu une première manière de faire de la classification :

```text
chercher les voisins les plus proches
puis voter
```

La régression logistique propose une autre approche.

Elle ne vote pas avec des voisins.

Elle apprend une formule qui transforme les variables en probabilité.

Objectifs :

- comprendre pourquoi la régression logistique sert à la classification ;
- partir d'une combinaison linéaire comme en régression linéaire ;
- comprendre le rôle de la fonction sigmoïde ;
- interpréter une probabilité entre 0 et 1 ;
- comprendre le seuil de décision à `0.5` ;
- préparer le passage vers le perceptron.

---

## 2. Le problème : prédire une classe

Imaginons un étudiant.

On veut prédire s'il valide un module.

Variables possibles :

- nombre d'heures de révision ;
- taux de présence ;
- nombre d'exercices rendus.

La réponse n'est pas un prix ou une température.

La réponse est une classe :

```text
0 = ne valide pas
1 = valide
```

On est donc dans un problème de classification.

---

## 3. Point de départ : une formule linéaire

La régression logistique commence comme une régression linéaire.

Elle calcule d'abord un score :

```text
z = w1 * x1 + w2 * x2 + ... + b
```

Avec :

- `x1`, `x2` : les variables ;
- `w1`, `w2` : les poids appris par le modèle ;
- `b` : le biais ;
- `z` : un score linéaire.

Exemple avec les heures de révision :

```text
z = w * heures + b
```

À ce stade, `z` n'est pas encore une probabilité.

---

## 4. Pourquoi ne pas garder la droite ?

Une droite peut donner n'importe quelle valeur.

Exemple :

```text
x = 1   -> 0.2
x = 10  -> 2.8
x = 20  -> 7.5
x = -5  -> -3.2
```

Ces valeurs peuvent être utiles comme score, mais pas comme probabilité.

Une probabilité doit toujours être comprise entre :

```text
0 et 1
```

Donc il faut transformer le score linéaire.

---

## 5. La fonction sigmoïde

La régression logistique applique une fonction sigmoïde au score `z`.

Formule :

```text
p = 1 / (1 + e^(-z))
```

La sigmoïde écrase les valeurs :

```text
z très négatif  -> proche de 0
z = 0           -> 0.5
z très positif  -> proche de 1
```

Le résultat `p` peut être interprété comme une probabilité.

---

## 6. Intuition avec les heures de révision

Imaginons que l'on prédise la validation d'un module.

```text
0 h   -> presque aucune chance de réussir
2 h   -> faible chance
4 h   -> situation incertaine
6 h   -> forte chance
10 h  -> presque certain
```

On ne passe pas brutalement de `0` à `1`.

La transition est progressive.

La sigmoïde produit exactement cette forme en S :

```text
Probabilité

1.0 |                     *********
    |                 ****
0.5 |-------------****
    |         ****
0.0 |********
    +-------------------------
         heures de révision
```

---

## 7. Pourquoi le point central vaut 0.5 ?

Lorsque :

```text
z = 0
```

on obtient :

```text
p = 1 / (1 + e^0)
```

Comme :

```text
e^0 = 1
```

alors :

```text
p = 1 / 2
p = 0.5
```

`0.5` est la frontière de décision la plus classique.

Règle simple :

```text
si p >= 0.5 -> classe 1
si p < 0.5  -> classe 0
```

---

## 8. L'idée géométrique

La régression logistique cherche une droite, ou un hyperplan, qui sépare les classes.

Avec deux variables, cette séparation peut être représentée par une droite.

Avec plus de variables, on parle d'hyperplan.

La différence avec la régression linéaire est la sortie :

```text
Régression linéaire :
score linéaire -> valeur numérique

Régression logistique :
score linéaire -> sigmoïde -> probabilité
```

On peut retenir :

```text
Régression linéaire
        +
Transformation sigmoïde
        =
Probabilité entre 0 et 1
```

C'est pour cela qu'elle est souvent enseignée juste après la régression linéaire.

Mathématiquement, elle prolonge l'idée de la droite, mais pour résoudre un problème de classification.

---

## 9. Lien avec KNN

KNN et la régression logistique peuvent tous les deux faire de la classification.

Mais ils ne raisonnent pas de la même manière.

| Modèle | Idée principale |
| ------ | --------------- |
| KNN | comparer aux voisins les plus proches |
| Régression logistique | apprendre une séparation et produire une probabilité |

KNN garde les exemples.

La régression logistique apprend des paramètres :

```text
w1, w2, ..., b
```

---

## 10. Transition vers le perceptron

Le perceptron utilise une idée très proche :

```text
z = w1 * x1 + w2 * x2 + b
p = sigmoid(z)
```

Puis il corrige les poids quand la prédiction est mauvaise.

La régression logistique prépare donc naturellement le passage vers :

- les poids ;
- le biais ;
- la sigmoïde ;
- la descente de gradient ;
- les réseaux de neurones.

---

## 11. Exercice pratique

Notebook :

- [Énoncé : régression logistique](notebooks/03_regression_logistique_enonce.ipynb)


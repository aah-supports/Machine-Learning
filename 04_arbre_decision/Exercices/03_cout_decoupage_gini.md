# Exercice : calculer le coût d'un découpage

## Objectif

Un arbre de décision teste plusieurs questions.

Pour choisir la meilleure, il calcule le niveau d'impureté obtenu après chaque découpage.

Dans cet exercice, on utilise l'impureté de Gini :

$$
Gini = 1 - \sum_{k=1}^{K} p_k^2
$$

Pour deux classes `Oui` et `Non` :

$$
Gini = 1 - p_{Oui}^2 - p_{Non}^2
$$

---

## Situation initiale

On dispose de six personnes :

```text
Oui, Oui, Non, Oui, Non, Non
```

La population contient donc :

```text
3 Oui
3 Non
```

### Question 1

Calculer les proportions :

$$
p_{Oui} = \frac{3}{6}
$$

$$
p_{Non} = \frac{3}{6}
$$

Puis calculer l'impureté de Gini du groupe initial.

---

## Découpage testé

L'arbre teste la question :

```text
poids <= 80 ?
```

Il obtient :

### Branche gauche

```text
Oui, Oui, Oui, Non
```

Soit :

```text
3 Oui
1 Non
```

### Branche droite

```text
Non, Non
```

Soit :

```text
0 Oui
2 Non
```

---

## Question 2

Calculer le Gini de la branche gauche :

$$
Gini_{gauche} = 1 - (3/4)^2 - (1/4)^2
$$

---

## Question 3

Calculer le Gini de la branche droite :

$$
Gini_{droite} = 1 - (0/2)^2 - (2/2)^2
$$

Pourquoi cette branche est-elle pure ?

---

## Question 4

Le coût du découpage est la moyenne pondérée des impuretés :

Coût = (4/6) × Gini_gauche + (2/6) × Gini_droite

Calculer ce coût.

---

## Question 5

Le gain de pureté est :

$$
Gain = Gini_{initial} - Coût
$$

Calculer le gain.

Puis compléter :

```text
Plus le coût d'un découpage est ..., plus les groupes obtenus sont purs.
```

---

## À retenir

L'arbre compare plusieurs questions :

```text
âge <= 22 ?
poids <= 80 ?
```

Il choisit généralement la question qui produit :

```text
le coût le plus faible
```

car elle réduit le plus le mélange des classes.

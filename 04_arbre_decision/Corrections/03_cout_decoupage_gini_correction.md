# Correction : calculer le coût d'un découpage

## 1. Gini initial

Le groupe initial contient :

```text
3 Oui
3 Non
```

Donc :

$$
p_{Oui} = \frac{3}{6} = 0.5
$$

$$
p_{Non} = \frac{3}{6} = 0.5
$$

$$
Gini_{initial}
=
1 - 0.5^2 - 0.5^2
$$

$$
Gini_{initial} = 0.5
$$

---

## 2. Gini de la branche gauche

La branche gauche contient :

```text
3 Oui
1 Non
```

$$
Gini_{gauche}
=
1
-
\left(\frac{3}{4}\right)^2
-
\left(\frac{1}{4}\right)^2
$$

$$
Gini_{gauche}
=
1 - 0.5625 - 0.0625
$$

$$
Gini_{gauche} = 0.375
$$

---

## 3. Gini de la branche droite

La branche droite contient uniquement des `Non` :

```text
0 Oui
2 Non
```

$$
Gini_{droite}
=
1 - 0^2 - 1^2
$$

$$
Gini_{droite} = 0
$$

Cette branche est pure parce qu'elle ne contient qu'une seule classe.

---

## 4. Coût du découpage

La branche gauche contient quatre exemples sur six.

La branche droite contient deux exemples sur six.

$$
Coût
=
\frac{4}{6} \times 0.375
+
\frac{2}{6} \times 0
$$

$$
Coût = 0.25
$$

---

## 5. Gain de pureté

$$
Gain = Gini_{initial} - Coût
$$

$$
Gain = 0.5 - 0.25
$$

$$
Gain = 0.25
$$

Le découpage réduit donc l'impureté de `0.25`.

La phrase attendue est :

```text
Plus le coût d'un découpage est faible,
plus les groupes obtenus sont purs.
```

## Conclusion

L'arbre teste plusieurs découpages et compare leurs coûts.

Il préfère le découpage qui produit la plus faible impureté pondérée.

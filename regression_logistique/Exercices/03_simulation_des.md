# Exercice 3 : simuler une distribution avec deux dés

## Objectif

Dans cet exercice, on simule un grand nombre de lancers de deux dés.

Le but est de comprendre qu'un phénomène aléatoire peut produire une distribution très structurée quand on observe beaucoup d'événements.

Ce n'est pas encore de la régression logistique, mais c'est un bon rappel sur les probabilités avant de manipuler des probabilités prédites par un modèle.

---

## Code de départ

Exécuter le code suivant :

```python
import numpy as np

np.random.seed(42)

nb_lancers = 10000

```

---

## Questions

1. Quelles sont les valeurs possibles pour la somme de deux dés ?
2. Quelle somme apparaît le plus souvent ?
3. Pourquoi la somme `7` est-elle plus fréquente que la somme `2` ?
4. Pourquoi les fréquences ne sont-elles pas exactement égales aux probabilités théoriques ?
5. Que se passerait-il si on augmentait `nb_lancers` à `100000` ?
6. La distribution obtenue est-elle uniforme ?
7. La distribution obtenue est-elle exactement une loi normale ?

---

## Conclusion attendue

Rédiger une courte conclusion en expliquant :

- pourquoi les valeurs centrales sont plus fréquentes ;
- pourquoi les valeurs extrêmes sont plus rares ;
- pourquoi cette expérience produit une forme proche d'une cloche ;
- pourquoi il faut rester prudent : la somme de deux dés ne suit pas exactement une loi normale.

On pourra aussi citer des exemples de phénomènes qui sont souvent modélisés par une loi normale :

- erreurs de mesure ;
- bruit autour d'une valeur moyenne ;
- tailles humaines dans une population homogène ;
- moyennes obtenues à partir d'un grand nombre d'événements indépendants.

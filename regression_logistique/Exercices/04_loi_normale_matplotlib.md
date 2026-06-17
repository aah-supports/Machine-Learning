# Supplément : visualiser une loi normale avec Matplotlib

## Objectif

Dans l'exercice précédent, la somme de deux dés produisait une forme avec plus de valeurs au centre qu'aux extrêmes.

Ici, on va visualiser une vraie forme en cloche avec une simulation de loi normale.

Le but est de comprendre :

- ce que représente la moyenne ;
- ce que représente l'écart-type ;
- pourquoi certains phénomènes naturels peuvent être modélisés par une loi normale ;
- quelles hypothèses rendent cette modélisation raisonnable.

---

## Partie 1 - Générer une loi normale

Exécuter le code suivant :

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

n = 10000

moyenne = 0
ecart_type = 1

valeurs = np.random.normal(moyenne, ecart_type, n)

plt.hist(valeurs, bins=50, density=True, edgecolor="black")
plt.title("Simulation d'une loi normale")
plt.xlabel("Valeurs")
plt.ylabel("Densité")
plt.show()
```

Questions :

1. Quelle forme observes-tu ?
2. Autour de quelle valeur les observations sont-elles concentrées ?
3. Les valeurs très éloignées de la moyenne sont-elles fréquentes ?
4. Pourquoi parle-t-on de forme en cloche ?

---

## Partie 2 - Modifier la moyenne

Modifier le code :

```python
moyenne = 10
ecart_type = 1
```

Questions :

1. Que devient le centre de la courbe ?
2. La forme générale change-t-elle ?
3. Que représente la moyenne dans une loi normale ?

---

## Partie 3 - Modifier l'écart-type

Modifier maintenant :

```python
moyenne = 10
ecart_type = 3
```

Questions :

1. La courbe est-elle plus serrée ou plus étalée ?
2. Les valeurs éloignées de la moyenne deviennent-elles plus fréquentes ?
3. Que représente l'écart-type ?

---

## Partie 4 - Exemple concret : poids d'un produit

Une usine fabrique des paquets censés peser `500 g`.

À cause de petites variations de fabrication, le poids exact varie légèrement.

On peut simuler cette situation :

```python
np.random.seed(42)

n = 10000

moyenne = 500
ecart_type = 8

poids = np.random.normal(moyenne, ecart_type, n)

plt.hist(poids, bins=50, density=True, edgecolor="black")
plt.title("Poids simulés de paquets")
plt.xlabel("Poids en grammes")
plt.ylabel("Densité")
plt.show()
```

Questions :

1. Quelle est la valeur centrale ?
2. Pourquoi tous les paquets ne pèsent-ils pas exactement `500 g` ?
3. Est-il normal d'observer quelques paquets à `480 g` ou `520 g` ?
4. Que signifierait un écart-type plus grand ?

---

## Partie 5 - Hypothèses à discuter

Une loi normale est souvent pertinente quand :

- la variable mesurée dépend de beaucoup de petites causes indépendantes ;
- aucune cause unique ne domine toutes les autres ;
- les effets peuvent aller dans les deux sens : un peu plus grand, un peu plus petit ;
- on observe une population relativement homogène ;
- la variable est continue ou presque continue ;
- on ne travaille pas sur une variable naturellement bornée de façon forte.

Questions :

1. Pourquoi le poids d'un produit fabriqué peut-il suivre approximativement une loi normale ?
2. Pourquoi la taille humaine dans une population homogène peut-elle avoir une forme proche d'une loi normale ?
3. Pourquoi le revenu d'une population ne suit-il généralement pas une loi normale ?
4. Pourquoi une note entre `0` et `20` ne suit-elle pas forcément une loi normale ?

---

## Conclusion attendue

Rédiger une conclusion qui explique :

- que la loi normale produit une courbe en cloche ;
- que la moyenne indique le centre ;
- que l'écart-type indique la dispersion ;
- que cette forme apparaît souvent quand une mesure résulte de nombreux petits effets indépendants ;
- qu'il ne faut pas supposer automatiquement qu'une variable suit une loi normale.

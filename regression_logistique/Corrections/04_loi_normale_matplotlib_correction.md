# Correction - Supplément : visualiser une loi normale avec Matplotlib

## Partie 1 - Générer une loi normale

Code :

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

On observe une courbe en cloche.

Les valeurs sont concentrées autour de `0`, car la moyenne vaut `0`.

Les valeurs très éloignées de `0` existent, mais elles sont rares.

On parle de forme en cloche parce que :

- le centre est élevé ;
- les côtés descendent progressivement ;
- les extrêmes sont peu fréquents.

---

## Partie 2 - Modifier la moyenne

Si on utilise :

```python
moyenne = 10
ecart_type = 1
```

la courbe garde la même forme générale, mais elle est déplacée vers `10`.

La moyenne représente donc le centre de la distribution.

Dans un contexte réel, si on modélise le poids d'un objet, la moyenne correspond au poids autour duquel les observations se concentrent.

---

## Partie 3 - Modifier l'écart-type

Si on utilise :

```python
moyenne = 10
ecart_type = 3
```

la courbe devient plus étalée.

Les valeurs sont moins concentrées autour de `10`.

Les observations éloignées de la moyenne deviennent plus fréquentes.

L'écart-type mesure la dispersion :

```text
petit écart-type  -> valeurs très regroupées
grand écart-type  -> valeurs plus dispersées
```

---

## Partie 4 - Exemple concret : poids d'un produit

Code :

```python
import numpy as np
import matplotlib.pyplot as plt

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

La valeur centrale est `500 g`.

Tous les paquets ne pèsent pas exactement `500 g`, car une fabrication réelle contient de petites variations :

- quantité de matière légèrement différente ;
- précision limitée de la machine ;
- petites variations de température ;
- vibrations ;
- arrondis de mesure.

Observer quelques paquets à `480 g` ou `520 g` peut être normal si l'écart-type est suffisant.

Un écart-type plus grand signifie que la machine est moins régulière : les poids sont plus dispersés autour de `500 g`.

---

## Partie 5 - Hypothèses pour retrouver ce phénomène dans la nature

Une forme proche de la loi normale apparaît souvent quand une grandeur résulte de l'accumulation de nombreux petits effets.

### Hypothèse 1 - Beaucoup de petites causes

La variable doit dépendre de nombreuses causes.

Exemple pour le poids d'un produit :

- réglage de la machine ;
- humidité ;
- quantité de matière ;
- vibration ;
- précision du capteur.

Chaque cause ajoute une petite variation.

### Hypothèse 2 - Causes à peu près indépendantes

Les causes ne doivent pas toutes aller ensemble dans la même direction.

Si toutes les variations viennent d'un seul problème majeur, on n'obtient pas forcément une courbe normale.

### Hypothèse 3 - Aucun facteur ne domine complètement

Si une seule cause explique presque toute la variation, la forme peut être très différente.

Exemple : une machine mal réglée qui produit deux types de paquets, certains trop légers et certains trop lourds, peut créer deux bosses au lieu d'une seule cloche.

### Hypothèse 4 - Effets positifs et négatifs

Les petites variations doivent pouvoir augmenter ou diminuer la valeur.

Pour un poids :

```text
un peu moins de matière -> poids plus faible
un peu plus de matière  -> poids plus élevé
```

### Hypothèse 5 - Population homogène

Pour la taille humaine, une loi normale peut être raisonnable si on observe une population homogène :

- même tranche d'âge ;
- même sexe si nécessaire ;
- conditions de mesure identiques ;
- population comparable.

Si on mélange enfants, adultes, hommes, femmes et populations très différentes, la distribution peut ne plus être une seule belle cloche.

### Hypothèse 6 - Variable continue

La loi normale convient mieux à des grandeurs continues :

- taille ;
- poids ;
- erreur de mesure ;
- bruit autour d'un signal ;
- diamètre d'une pièce fabriquée.

Elle convient moins directement à des variables discrètes ou fortement bornées.

---

## Exemples pertinents

### Poids d'un produit fabriqué

Un paquet annoncé à `500 g` peut avoir un poids réel légèrement différent.

Comme beaucoup de petites causes interviennent, les poids peuvent être proches d'une loi normale autour de `500 g`.

### Taille humaine

Dans une population homogène, la taille dépend de nombreux facteurs génétiques et environnementaux.

La distribution peut donc avoir une forme proche d'une cloche.

### Erreurs de mesure

Quand un appareil mesure une grandeur, il produit souvent de petites erreurs autour de la vraie valeur.

Ces erreurs peuvent être positives ou négatives.

Elles sont souvent modélisées par une loi normale.

---

## Contre-exemples

### Revenus

Les revenus ne suivent généralement pas une loi normale.

Ils sont très asymétriques :

- beaucoup de revenus moyens ou modestes ;
- quelques revenus extrêmement élevés.

La distribution a souvent une longue queue à droite.

### Notes entre 0 et 20

Une note est bornée entre `0` et `20`.

Elle dépend aussi du sujet, du barème, du niveau de la classe et de la difficulté de l'examen.

Elle peut avoir une forme normale, mais ce n'est pas automatique.

### Temps d'attente

Les temps d'attente sont souvent positifs et asymétriques.

On observe parfois beaucoup de petits temps d'attente et quelques très grands temps d'attente.

Ce n'est généralement pas une loi normale.

---

## Conclusion possible

Une loi normale produit une courbe en cloche.

La moyenne indique le centre de la distribution.

L'écart-type indique à quel point les valeurs sont dispersées autour de ce centre.

Cette forme apparaît souvent quand une grandeur résulte de nombreux petits effets indépendants, dont aucun ne domine complètement les autres.

C'est pour cela que des phénomènes comme les erreurs de mesure, le poids de produits fabriqués ou la taille dans une population homogène peuvent être modélisés par une loi normale.

Mais ce n'est pas une règle automatique.

Avant de supposer une loi normale, il faut regarder les données, vérifier la forme de l'histogramme et réfléchir au mécanisme qui produit les observations.

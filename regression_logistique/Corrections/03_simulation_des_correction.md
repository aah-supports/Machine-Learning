# Correction - Exercice 3 : simuler une distribution avec deux dés

## Code complet

```python
import numpy as np

np.random.seed(42)

nb_lancers = 10000

de1 = np.random.randint(1, 7, nb_lancers)
de2 = np.random.randint(1, 7, nb_lancers)

sommes = de1 + de2

valeurs, frequences = np.unique(sommes, return_counts=True)

for valeur, freq in zip(valeurs, frequences):
    etoiles = "*" * (freq // 100)

    print(f"{valeur:2d} : {etoiles}")
```

Avec `np.random.seed(42)`, on obtient par exemple :

```text
 2 : **
 3 : ******
 4 : ********
 5 : ***********
 6 : *************
 7 : ****************
 8 : **************
 9 : ***********
10 : ********
11 : *****
12 : **
```

Les fréquences exactes de cette simulation sont :

| Somme | Fréquence simulée |
| ----- | ----------------- |
| 2     | 273               |
| 3     | 608               |
| 4     | 811               |
| 5     | 1101              |
| 6     | 1383              |
| 7     | 1616              |
| 8     | 1414              |
| 9     | 1105              |
| 10    | 858               |
| 11    | 556               |
| 12    | 275               |

---

## Réponses

### 1. Quelles sont les valeurs possibles ?

Avec deux dés, la plus petite somme est :

```text
1 + 1 = 2
```

La plus grande somme est :

```text
6 + 6 = 12
```

Les valeurs possibles sont donc :

```text
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
```

---

### 2. Quelle somme apparaît le plus souvent ?

La somme `7` apparaît le plus souvent.

Dans cette simulation, elle apparaît `1616` fois.

---

### 3. Pourquoi `7` est-il plus fréquent que `2` ?

La somme `2` ne peut être obtenue que d'une seule manière :

```text
1 + 1
```

La somme `7` peut être obtenue de plusieurs manières :

```text
1 + 6
2 + 5
3 + 4
4 + 3
5 + 2
6 + 1
```

Il y a donc beaucoup plus de combinaisons qui donnent `7`.

---

### 4. Pourquoi les fréquences ne sont-elles pas exactement théoriques ?

On fait une simulation aléatoire.

Même avec `10000` lancers, il reste une part de hasard.

Les fréquences simulées se rapprochent des probabilités théoriques, mais elles ne sont pas parfaitement identiques.

---

### 5. Que se passerait-il avec `100000` lancers ?

Les fréquences deviendraient plus stables.

La forme générale resterait la même :

```text
peu de 2 et de 12
beaucoup de valeurs autour de 7
```

Mais les proportions seraient plus proches des probabilités théoriques.

---

### 6. La distribution est-elle uniforme ?

Non.

Une distribution uniforme donnerait à peu près la même fréquence pour chaque somme.

Ici, les sommes centrales sont beaucoup plus fréquentes que les sommes extrêmes.

---

### 7. Est-ce une loi normale ?

Non, pas exactement.

La somme de deux dés suit une distribution discrète en forme de triangle.

Elle ressemble un peu à une cloche, car les valeurs centrales sont plus probables que les valeurs extrêmes, mais ce n'est pas une vraie loi normale.

---

## Conclusion possible

Quand on lance deux dés, toutes les sommes ne sont pas aussi probables.

Les valeurs centrales, surtout `7`, apparaissent plus souvent parce qu'elles peuvent être obtenues par plusieurs combinaisons.

Les valeurs extrêmes, comme `2` ou `12`, sont rares parce qu'elles n'ont qu'une seule combinaison possible.

Cette expérience montre qu'un phénomène aléatoire peut produire une structure très régulière quand on répète l'expérience un grand nombre de fois.

La forme obtenue n'est pas exactement une loi normale : avec deux dés, on obtient plutôt une distribution triangulaire et discrète.

En revanche, cette idée prépare à la loi normale. Quand on additionne ou moyenne un grand nombre d'événements indépendants, les valeurs ont souvent tendance à se concentrer autour d'une moyenne et à former une courbe en cloche.

C'est pourquoi la loi normale est souvent utilisée pour modéliser :

- des erreurs de mesure ;
- du bruit autour d'une valeur moyenne ;
- certaines caractéristiques humaines dans une population homogène, comme la taille ;
- des moyennes calculées à partir de nombreux événements indépendants.

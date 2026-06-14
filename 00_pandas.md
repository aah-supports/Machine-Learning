# Introduction à Pandas

## Objectif

Pandas est la bibliothèque Python de référence pour manipuler des données tabulaires (CSV, Excel, bases de données, etc.). Les deux structures principales sont :

* **Series** : une colonne de données.
* **DataFrame** : un tableau de données avec lignes et colonnes. ([Pandas][1])

---

# 1. Installation et import

```python
import pandas as pd
```

Convention universelle :

```python
pd
```

désigne la bibliothèque Pandas.

---

# 2. Créer un DataFrame

```python
import pandas as pd

students = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 21],
    "city": ["Paris", "Lyon", "Marseille"]
})

print(students)
```

Résultat :

```text
      name  age       city
0    Alice   22      Paris
1      Bob   25       Lyon
2  Charlie   21  Marseille
```

Un DataFrame ressemble à une feuille Excel. 

---

# 3. Charger un CSV

```python
df = pd.read_csv("students.csv")
```

Les données sont automatiquement chargées dans un DataFrame.

---

# 4. Explorer les données

Afficher les premières lignes :

```python
df.head()
```

Afficher les dernières :

```python
df.tail()
```

Informations générales :

```python
df.info()
```

Statistiques :

```python
df.describe()
```


---

# 5. Sélectionner une colonne

```python
df["name"]
```

ou

```python
df["age"]
```

Résultat :

```text
0    22
1    25
2    21
```

---

# 6. Sélectionner plusieurs colonnes

```python
df[["name", "age"]]
```

---

# 7. Filtrer les données

Étudiants majeurs de plus de 22 ans :

```python
df[df["age"] > 22]
```

Plusieurs conditions :

```python
df[
    (df["age"] > 20)
    & (df["city"] == "Paris")
]
```


---

# 8. Ajouter une colonne

```python
df["score"] = [12, 15, 18]
```

---

# 9. Calculs simples

Moyenne :

```python
df["score"].mean()
```

Maximum :

```python
df["score"].max()
```

Minimum :

```python
df["score"].min()
```

---

# 10. Trier

Par âge croissant :

```python
df.sort_values("age")
```

Par âge décroissant :

```python
df.sort_values("age", ascending=False)
```

---

# Exercice 1 - Création

Créer le DataFrame suivant :

| name    | age | city      |
| ------- | --- | --------- |
| Alice   | 22  | Paris     |
| Bob     | 25  | Lyon      |
| Charlie | 21  | Marseille |

Afficher le DataFrame.

---

# Exercice 2 - Sélection

À partir du DataFrame précédent :

1. Afficher uniquement la colonne `name`.
2. Afficher uniquement les colonnes `name` et `age`.

---

# Exercice 3 - Filtre

Afficher uniquement :

* les étudiants ayant plus de 22 ans.

Résultat attendu :

```text
Bob
```

---

# Exercice 4 - Nouvelle colonne

Ajouter :

```text
score
```

avec les valeurs :

```text
12
15
18
```

Puis afficher le DataFrame.

---

# Exercice 5 - Statistiques

Calculer :

* la moyenne des scores ;
* le score maximum ;
* le score minimum.

---

# Exercice 6 - Cas réel

Créer le DataFrame :

```python
products = pd.DataFrame({
    "name": ["Laptop", "Mouse", "Keyboard"],
    "price": [1200, 25, 75],
    "stock": [10, 50, 20]
})
```

Questions :

1. Afficher tous les produits.
2. Afficher les produits dont le prix est supérieur à 100 €.
3. Ajouter une colonne :

```python
inventory_value
```

correspondant à :

```python
price * stock
```

4. Afficher la valeur totale du stock.

# Exercice : Nettoyage d'un fichier clients

## Contexte

Vous recevez un export CSV provenant d'un ancien logiciel de gestion.

Les données sont incomplètes et incohérentes.

Votre mission est de nettoyer le DataFrame avant de pouvoir l'analyser.

---

## Données de départ

```python
import pandas as pd

customers = pd.DataFrame({
    "name": [
        "Alice",
        "Bob",
        None,
        "Charlie",
        "alice"
    ],
    "age": [
        22,
        None,
        25,
        -5,
        22
    ],
    "city": [
        "Paris",
        "Lyon",
        "Paris ",
        None,
        "paris"
    ],
    "email": [
        "alice@mail.com",
        None,
        "charlie@mail.com",
        "charlie@mail.com",
        "alice@mail.com"
    ]
})

print(customers)
```

Résultat :

```text
      name   age    city              email
0    Alice  22.0   Paris     alice@mail.com
1      Bob   NaN    Lyon               None
2     None  25.0  Paris    charlie@mail.com
3  Charlie  -5.0    None   charlie@mail.com
4    alice  22.0   paris     alice@mail.com
```

---

# Travail demandé

## 1. Explorer les données

Afficher :

```python
customers.info()
```

et

```python
customers.describe()
```

---

## 2. Rechercher les valeurs manquantes

Afficher :

```python
customers.isnull().sum()
```

---

## 3. Supprimer les lignes sans nom

Résultat attendu :

```text
Alice
Bob
Charlie
alice
```

---

## 4. Remplacer les âges manquants

Remplacer les âges manquants par l'âge moyen.

---

## 5. Supprimer les âges incohérents

Supprimer les personnes dont :

```python
age < 0
```

---

## 6. Uniformiser les villes

Transformer :

```text
Paris
Paris
paris
```

en :

```text
PARIS
PARIS
PARIS
```

Indice :

```python
.str.upper()
```

---

## 7. Supprimer les espaces inutiles

Transformer :

```text
"Paris "
```

en :

```text
"Paris"
```

Indice :

```python
.str.strip()
```

---

## 8. Uniformiser les noms

Transformer :

```text
Alice
alice
```

en :

```text
Alice
Alice
```

Indice :

```python
.str.title()
```

---

## 9. Supprimer les doublons

Certaines lignes représentent la même personne.

Supprimer les doublons.

Indice :

```python
drop_duplicates()
```

---

## Résultat attendu

Le DataFrame final doit ressembler à :

```text
      name   age   city           email
0    Alice  22.0  PARIS  alice@mail.com
1      Bob  23.0   LYON            None
```

(selon la stratégie retenue pour les valeurs manquantes)

---

# Bonus

Créer une colonne :

```python
is_adult
```

qui vaut :

```text
True
```

si l'âge est supérieur ou égal à 18.

Exemple :

```python
customers["is_adult"] = customers["age"] >= 18
```

---

Cet exercice permet de manipuler les méthodes Pandas les plus utilisées en entreprise :

```python
isnull()
fillna()
dropna()
drop_duplicates()
str.upper()
str.strip()
str.title()
loc[]
mean()
```
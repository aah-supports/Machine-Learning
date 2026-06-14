# Correction Exercice 1

Créer le DataFrame :

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

---

# Correction Exercice 2

### 1. Afficher la colonne name

```python
students["name"]
```

Résultat :

```text
0      Alice
1        Bob
2    Charlie
```

---

### 2. Afficher name et age

```python
students[["name", "age"]]
```

Résultat :

```text
      name  age
0    Alice   22
1      Bob   25
2  Charlie   21
```

---

# Correction Exercice 3

Afficher les étudiants de plus de 22 ans :

```python
students[students["age"] > 22]
```

Résultat :

```text
  name  age  city
1  Bob   25  Lyon
```

---

# Correction Exercice 4

Ajouter la colonne score :

```python
students["score"] = [12, 15, 18]

print(students)
```

Résultat :

```text
      name  age       city  score
0    Alice   22      Paris     12
1      Bob   25       Lyon     15
2  Charlie   21  Marseille     18
```

---

# Correction Exercice 5

### Moyenne

```python
students["score"].mean()
```

Résultat :

```python
15.0
```

---

### Maximum

```python
students["score"].max()
```

Résultat :

```python
18
```

---

### Minimum

```python
students["score"].min()
```

Résultat :

```python
12
```

---

# Correction Exercice 6

Création du DataFrame :

```python
products = pd.DataFrame({
    "name": ["Laptop", "Mouse", "Keyboard"],
    "price": [1200, 25, 75],
    "stock": [10, 50, 20]
})
```

---

## 1. Afficher tous les produits

```python
print(products)
```

Résultat :

```text
       name  price  stock
0    Laptop   1200     10
1     Mouse     25     50
2  Keyboard     75     20
```

---

## 2. Produits dont le prix est supérieur à 100 €

```python
products[products["price"] > 100]
```

Résultat :

```text
     name  price  stock
0  Laptop   1200     10
```

---

## 3. Ajouter inventory_value

```python
products["inventory_value"] = (
    products["price"] * products["stock"]
)

print(products)
```

Résultat :

```text
       name  price  stock  inventory_value
0    Laptop   1200     10            12000
1     Mouse     25     50             1250
2  Keyboard     75     20             1500
```

---

## 4. Valeur totale du stock

```python
products["inventory_value"].sum()
```

Résultat :

```python
14750
```

---

# Exercice bonus

Afficher les produits dont le stock est inférieur à 30 :

```python
products[products["stock"] < 30]
```

Résultat :

```text
       name  price  stock  inventory_value
0    Laptop   1200     10            12000
2  Keyboard     75     20             1500
```

---

# Exercice bonus 2

Trier les produits du plus cher au moins cher :

```python
products.sort_values(
    by="price",
    ascending=False
)
```

Résultat :

```text
       name  price  stock
0    Laptop   1200     10
2  Keyboard     75     20
1     Mouse     25     50
```

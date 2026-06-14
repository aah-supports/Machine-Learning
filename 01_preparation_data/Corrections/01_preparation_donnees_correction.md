# Correction - Préparer et nettoyer les données

## 1. Ce qu'il fallait retenir

Avant le modèle, on doit vérifier que le dataset est exploitable.

Les points clés sont :

- inspecter la structure du tableau ;
- repérer les valeurs manquantes ;
- détecter les doublons ;
- corriger les types de colonnes ;
- supprimer les valeurs impossibles ;
- encoder les variables texte ;
- séparer `X` et `y` seulement une fois le nettoyage terminé ;
- éviter toute fuite de données.

---

## 2. Vérification initiale

Les commandes utiles sont :

```python
data.shape
data.head()
data.info()
data.describe()
data.isna().sum()
data.duplicated().sum()
```

Elles servent à comprendre le dataset avant toute modification.

---

## 3. Nettoyage attendu sur l'exemple immobilier

Sur le tableau :

```text
surface | pièces | quartier | prix
```

les corrections attendues sont :

```python
data_clean = data.copy()

data_clean["surface"] = data_clean["surface"].replace("?", None)
data_clean["surface"] = data_clean["surface"].str.replace(" m2", "", regex=False)
data_clean["surface"] = pd.to_numeric(data_clean["surface"], errors="coerce")

data_clean["surface"] = data_clean["surface"].fillna(data_clean["surface"].median())
data_clean["pieces"] = data_clean["pieces"].fillna(data_clean["pieces"].median())

data_clean = data_clean.drop_duplicates()
data_clean = data_clean[data_clean["surface"] > 0]

data_clean = pd.get_dummies(data_clean, columns=["quartier"], dtype=int)

X = data_clean.drop(columns=["prix"])
y = data_clean["prix"]
```

---

## 4. Bonnes pratiques métier

Les règles à justifier devant un public sont :

- garder une version brute ;
- documenter chaque correction ;
- ne pas inventer une valeur sans raison ;
- vérifier les valeurs impossibles avec le métier ;
- éviter d'utiliser une information indisponible au moment de la prédiction ;
- séparer le jeu d'entraînement du test avant toute transformation qui apprend quelque chose.


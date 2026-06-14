# Chapitre 3 : Régression linéaire

## 1. Objectif du chapitre

Dans les chapitres précédents, nous avons vu qu'un modèle de Machine Learning apprend à partir de données et qu'un dataset doit être préparé avant l'entraînement.

Dans ce chapitre, nous allons construire un premier modèle complet avec la **régression linéaire**.

Objectifs :

- comprendre ce qu'est une régression ;
- identifier les modules Python utilisés ;
- séparer les features, le label, puis le train et le test ;
- entraîner un modèle avec `fit` ;
- faire une prédiction avec `predict` ;
- lire ce que le modèle a appris ;
- comprendre la notion d'erreur ;
- évaluer le modèle sur des données jamais vues ;
- interpréter une droite de régression.

---

## 2. Rappel : régression ou classification ?

La **régression** sert à prédire une valeur numérique.

Exemples :

- prix d'un logement ;
- température ;
- chiffre d'affaires ;
- durée d'un trajet ;
- consommation électrique.

La **classification** sert à prédire une catégorie.

Exemples :

- spam ou non spam ;
- malade ou sain ;
- client fidèle ou client à risque ;
- chien ou chat.

Dans ce chapitre, on travaille sur un problème de régression :

```text
Surface du logement → Prix du logement
```

---

## 3. Idée générale de la régression linéaire

La régression linéaire cherche une relation sous forme de droite.

Formule :

```text
y = ax + b
```

Dans notre exemple :

```text
prix = coefficient × surface + intercept
```

Avec :

- `surface` : la donnée d'entrée ;
- `prix` : la valeur à prédire ;
- `coefficient` : l'impact de la surface sur le prix ;
- `intercept` : la valeur de départ de la droite.

Exemple simple :

```text
prix = 4000 × surface
```

Si un logement fait `70 m²` :

```text
prix = 4000 × 70
prix = 280000
```

Le modèle prédirait donc :

```text
280000 €
```

---

## 4. Exemple de dataset

On dispose de logements déjà vendus :

| Surface | Prix   |
| ------- | ------ |
| 30      | 120000 |
| 40      | 160000 |
| 50      | 200000 |
| 60      | 240000 |
| 70      | 280000 |
| 80      | 320000 |
| 90      | 360000 |

On voit une relation simple :

```text
Quand la surface augmente, le prix augmente.
```

Le rôle du modèle est d'apprendre cette relation automatiquement.

---

## 5. Outils Python utilisés

Pour ce chapitre, on utilise quelques bibliothèques Python classiques.

### pandas

`pandas` sert à manipuler les données sous forme de tableau.

```python
import pandas as pd
```

On l'utilise pour créer ou lire un dataset :

```python
data = pd.DataFrame({
    "surface": [30, 40, 50],
    "prix": [120000, 160000, 200000]
})
```

### scikit-learn

`scikit-learn` fournit les outils de Machine Learning.

On utilise ici :

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
```

Rôle de chaque import :

- `train_test_split` : sépare les données en entraînement et test ;
- `LinearRegression` : crée un modèle de régression linéaire ;
- `mean_absolute_error` : mesure l'erreur moyenne du modèle.

### matplotlib

`matplotlib` sert à afficher des graphiques.

```python
import matplotlib.pyplot as plt
```

On l'utilise pour visualiser les points du dataset et la droite apprise par le modèle.

---

## 6. Features et label

Pour entraîner le modèle, on sépare les données en deux parties.

### Feature

La feature est la donnée utilisée pour prédire.

Ici :

```text
surface
```

### Label

Le label est la valeur à prédire.

Ici :

```text
prix
```

En Python :

```python
X = data[["surface"]]
y = data["prix"]
```

Attention :

```python
X = data[["surface"]]
```

On utilise deux crochets car `X` doit être un tableau de features, même s'il n'y a qu'une seule colonne.

Cette étape sépare les colonnes du dataset :

```text
surface → donnée utilisée pour prédire
prix    → valeur à prédire
```

Mais cette étape ne sépare pas encore les lignes entre entraînement et test.

---

## 7. Séparer entraînement et test

Après avoir séparé `X` et `y`, on sépare le dataset en deux parties :

- **données d'entraînement** : utilisées par le modèle pour apprendre ;
- **données de test** : gardées de côté pour vérifier si le modèle fonctionne sur des exemples non vus.

Code :

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Avec `test_size=0.2` :

```text
80% des données → entraînement
20% des données → test
```

Ce n'est pas une règle obligatoire.

C'est une convention pratique :

- on donne assez de données au modèle pour apprendre ;
- on garde assez de données de côté pour tester le modèle.

Avec un très petit dataset, le test contient peu d'exemples. L'évaluation est donc utile pour comprendre le principe, mais elle reste fragile.

Avec un dataset plus grand, le score ou l'erreur mesurée sur le test devient plus fiable.

Règle pratique :

```text
Petit dataset  → validation croisée ou test plus prudent
Dataset moyen  → souvent 80% / 20%
Grand dataset  → parfois 90% / 10%
```

Le choix dépend de la quantité de données disponible et du besoin d'évaluation.

---

## 8. Entraîner une régression linéaire

Code complet :

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "surface": [30, 40, 50, 60, 70, 80, 90, 100, 110],
    "prix": [120000, 160000, 200000, 240000, 280000, 320000, 360000, 400000, 440000]
})

X = data[["surface"]]
y = data["prix"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modele = LinearRegression()
modele.fit(X_train, y_train)
```

La ligne importante :

```python
modele.fit(X_train, y_train)
```

Signifie :

```text
Apprends la relation entre la surface et le prix à partir des données d'entraînement.
```

Dans une régression linéaire classique, cela ne veut pas dire que le modèle utilise un réseau de neurones.

Ici, le modèle cherche simplement les meilleurs paramètres de la droite :

```text
prix = coefficient × surface + intercept
```

Donc quand on dit que le modèle "apprend", cela signifie :

```text
Il calcule le coefficient et l'intercept qui permettent à la droite de passer au plus près des points.
```

Le modèle ne doit pas apprendre avec `X_test` et `y_test`.

Ces données sont gardées pour l'évaluation.

### Ce qu'il se passe derrière

Avec une seule variable, comme `surface`, la pente de la droite peut se calculer avec :

```text
coefficient = covariance(surface, prix) / variance(surface)
```

Puis l'intercept se calcule avec :

```text
intercept = moyenne(prix) - coefficient × moyenne(surface)
```

La **covariance** indique si deux variables évoluent ensemble.

Exemple :

```text
Si la surface augmente et que le prix augmente aussi,
la covariance entre surface et prix est positive.
```

La **variance** indique à quel point les valeurs de surface sont dispersées.

Résumé :

```text
Régression linéaire classique :
calcule une droite avec des coefficients.

Réseau de neurones :
apprend des poids dans plusieurs couches de neurones.
```

Dans ce chapitre, nous utilisons une régression linéaire classique, pas un réseau de neurones.

---

## 9. Faire une prédiction

Une fois le modèle entraîné, on peut prédire le prix d'un nouveau logement.

```python
nouveau_logement = pd.DataFrame({
    "surface": [75]
})

prix = modele.predict(nouveau_logement)
```

Ici, on demande :

```text
Quel prix pour un logement de 75 m² ?
```

Le modèle retourne une valeur numérique :

```text
300000
```

---

## 10. Lire ce que le modèle a appris

Une régression linéaire est un modèle interprétable.

On peut lire :

- le coefficient ;
- l'intercept.

```python
coefficient = modele.coef_[0]
intercept = modele.intercept_

print(coefficient)
print(intercept)
```

Dans notre exemple, le modèle apprend environ :

```text
coefficient = 4000
intercept = 0
```

Donc la formule devient :

```text
prix = 4000 × surface + 0
```

Le coefficient signifie :

```text
Chaque m² supplémentaire ajoute environ 4000 € au prix.
```

---

## 11. Vérifier une prédiction à la main

Pour `75 m²` :

```text
prix = 4000 × 75 + 0
prix = 300000
```

Le modèle prédit donc :

```text
300000 €
```

Ce calcul aide à comprendre que le modèle n'est pas magique.

Il a simplement appris une formule à partir des données.

---

## 12. Tester le modèle

Après l'entraînement, on utilise les données de test.

Le modèle n'a pas vu ces lignes pendant `.fit(...)`.

On peut donc les utiliser pour vérifier s'il généralise.

```python
from sklearn.metrics import mean_absolute_error

predictions_test = modele.predict(X_test)
mae_test = mean_absolute_error(y_test, predictions_test)

print(mae_test)
```

Pour interpréter ce nombre, on regarde chaque ligne du jeu de test :

```text
erreur = |prix réel - prix prédit|
```

La MAE est la moyenne de ces erreurs. Elle répond donc à la question :

```text
En moyenne, de combien le modèle se trompe-t-il sur des données non vues ?
```

Si la MAE test vaut `12000`, cela signifie :

```text
Sur les logements de test, l'erreur moyenne du modèle est d'environ 12000 €.
```

Exemple concret :

| Prix réel | Prix prédit | Erreur |
| --------- | ----------- | ------ |
| 200000 € | 190000 € | 10000 € |
| 320000 € | 330000 € | 10000 € |
| 400000 € | 395000 € | 5000 € |

Ici, la moyenne des erreurs vaut :

```text
(10000 + 10000 + 5000) / 3 = 8333 €
```

Donc `MAE = 8333 €` signifie :

```text
sur ces données de test, les prédictions sont en moyenne à 8333 € du vrai prix.
```

Pourquoi ne pas mesurer seulement sur le train ?

Parce que le modèle a déjà vu les données d'entraînement.

Un bon résultat sur le train ne prouve pas forcément que le modèle fonctionne sur de nouveaux logements.

Le test sert donc à obtenir une première estimation de la performance réelle.

---

## 13. Visualiser la droite apprise

On peut représenter :

- les données réelles avec des points ;
- la droite apprise avec une ligne.

```python
import matplotlib.pyplot as plt

prix_predits = modele.predict(X)

plt.scatter(data["surface"], data["prix"], label="Données réelles")
plt.plot(data["surface"], prix_predits, color="red", label="Droite apprise")
plt.xlabel("Surface en m²")
plt.ylabel("Prix en euros")
plt.legend()
plt.show()
```

L'objectif visuel :

```text
La droite doit passer au plus près des points.
```

---

## 14. Comprendre l'erreur

Un modèle ne tombe pas toujours exactement sur la bonne réponse.

Exemple :

| Surface | Prix réel | Prix prédit | Erreur |
| ------- | --------- | ----------- | ------ |
| 50      | 205000    | 200000      | 5000   |
| 70      | 275000    | 280000      | -5000  |
| 90      | 370000    | 360000      | 10000  |

Formule simple :

```text
erreur = prix réel - prix prédit
```

Pendant l'entraînement, le modèle cherche une droite qui réduit les erreurs.

Il ne cherche pas forcément une droite parfaite.

Il cherche la meilleure droite possible pour les données disponibles.

---

## 15. Mesurer la qualité du modèle

Pour mesurer l'erreur moyenne, on peut utiliser la **MAE**.

MAE signifie :

```text
Mean Absolute Error
```

En français :

```text
Erreur absolue moyenne
```

Exemple :

```python
from sklearn.metrics import mean_absolute_error

prix_predits_test = modele.predict(X_test)
mae_test = mean_absolute_error(y_test, prix_predits_test)

print(mae_test)
```

Pour l'interpréter, on lit `5000` comme un ordre de grandeur de l'erreur :

```text
Sur les données de test, les prédictions sont en moyenne éloignées de 5000 € du prix réel.
```

On privilégie la MAE calculée sur le test, car elle mesure l'erreur sur des données non utilisées pour l'entraînement.

---

## 16. Règles pratiques pour entraîner et tester

Pour éviter les erreurs classiques, on peut retenir ces règles.

### 1. Séparer les colonnes

```python
X = data[["surface"]]
y = data["prix"]
```

`X` contient les informations disponibles pour prédire.

`y` contient la réponse attendue.

### 2. Séparer les lignes

```python
X_train, X_test, y_train, y_test = train_test_split(...)
```

Le train sert à apprendre.

Le test sert à évaluer.

### 3. Entraîner uniquement sur le train

```python
modele.fit(X_train, y_train)
```

Il ne faut pas entraîner le modèle sur le test.

Sinon, le test ne représente plus des données jamais vues.

### 4. Évaluer sur le test

```python
predictions_test = modele.predict(X_test)
mae_test = mean_absolute_error(y_test, predictions_test)
```

Le résultat test donne une estimation plus honnête de la performance du modèle.

### 5. Garder les mêmes colonnes

Les colonnes utilisées pour prédire doivent être les mêmes à l'entraînement et à la prédiction.

Exemple :

```python
modele.fit(data[["surface"]], y)
```

Alors la prédiction doit aussi fournir une colonne `surface` :

```python
nouveau_logement = pd.DataFrame({"surface": [75]})
modele.predict(nouveau_logement)
```

---

## 17. Limites de la régression linéaire

La régression linéaire est simple et interprétable, mais elle a des limites.

Elle fonctionne bien si la relation ressemble à une droite.

Exemple adapté :

```text
Plus la surface augmente, plus le prix augmente régulièrement.
```

Exemple moins adapté :

```text
Le prix augmente fortement au début, puis stagne.
```

Dans ce cas, une droite peut être trop simple.

---

## 18. Quand le modèle se décale de la réalité

Le jeu de test permet de vérifier si le modèle fonctionne sur des données qu'il n'a pas vues pendant l'entraînement.

Mais cela ne garantit pas que le modèle restera valable pour toujours.

Dans la vraie vie, la réalité peut changer.

Exemples :

- le marché immobilier augmente fortement ;
- les taux d'intérêt changent ;
- un quartier devient plus attractif ;
- les données d'entraînement deviennent trop anciennes ;
- les nouveaux logements ne ressemblent plus aux logements du dataset initial.

Dans ce cas, le modèle peut continuer à produire des prédictions, mais ces prédictions peuvent être de moins en moins fiables.

Pour le constater, on compare régulièrement :

```text
prix réel - prix prédit
```

sur les nouvelles ventes observées.

Si l'erreur réelle devient beaucoup plus grande que l'erreur mesurée sur le jeu de test, le modèle est peut-être en décalage avec la réalité.

Exemple :

```text
MAE sur le jeu de test : 12000 €
MAE sur les nouvelles ventes : 55000 €
```

Cela signifie que le modèle se trompe beaucoup plus qu'avant.

Actions possibles :

- récupérer des données plus récentes ;
- ajouter des variables importantes ;
- réentraîner le modèle ;
- choisir un modèle plus adapté si la relation n'est plus linéaire.

---

## 19. Automatiser le suivi du modèle

Oui, ce suivi peut être automatisé.

L'idée est de garder une trace de chaque prédiction faite par le modèle, puis de la comparer au vrai résultat quand il devient disponible.

Exemple de table de suivi :

| id_logement | surface | prix_predit | prix_reel | erreur |
| ----------- | ------- | ----------- | --------- | ------ |
| 1           | 70      | 300000      | 315000    | 15000  |
| 2           | 90      | 400000      | 460000    | 60000  |
| 3           | 110     | 500000      | 570000    | 70000  |

On peut ensuite recalculer automatiquement la MAE sur les ventes récentes.

Exemple :

```python
from sklearn.metrics import mean_absolute_error

mae_test = 12000

prix_reels = [315000, 460000, 570000]
prix_predits = [300000, 400000, 500000]

mae_recente = mean_absolute_error(prix_reels, prix_predits)

print(mae_recente)
```

Puis on définit des règles simples.

Exemple :

```python
if mae_recente < 1.5 * mae_test:
    print("Modèle encore acceptable")
elif mae_recente < 3 * mae_test:
    print("Modèle à surveiller")
else:
    print("Modèle à réentraîner")
```

Avec :

```text
MAE test = 12000 €
```

Cela donne :

```text
MAE récente < 18000 €  → modèle acceptable
MAE récente < 36000 €  → modèle à surveiller
MAE récente > 36000 €  → modèle à réentraîner
```

Dans une vraie application, ce contrôle peut être lancé :

- chaque semaine ;
- chaque mois ;
- après un certain nombre de nouvelles ventes ;
- dès qu'une nouvelle vraie valeur est disponible.

Schéma simple :

```text
Nouvelle prédiction
        ↓
Stockage de la prédiction
        ↓
Arrivée du vrai prix de vente
        ↓
Calcul de l'erreur
        ↓
Mise à jour de la MAE récente
        ↓
Alerte ou réentraînement si l'erreur devient trop grande
```

---

## 20. Pourquoi utiliser un modèle malgré cette contrainte ?

Un modèle n'est pas utile parce qu'il est parfait.

Il est utile parce qu'il donne une estimation rapide, cohérente et mesurable.

Sans modèle :

```text
Chaque estimation dépend fortement de l'intuition humaine.
```

Avec un modèle :

```text
On applique la même logique à tous les logements.
On connaît l'erreur moyenne.
On peut suivre la qualité dans le temps.
On peut améliorer le modèle avec de nouvelles données.
```

Exemple :

```text
Prix prédit : 300000 €
MAE test : 12000 €
```

On peut présenter la prédiction comme :

```text
Prix estimé : environ 300000 €
Erreur moyenne observée : environ 12000 €
```

Le modèle aide donc à prendre une décision, mais il ne remplace pas totalement l'analyse humaine.

Dans un cas immobilier, on peut utiliser le modèle pour :

- obtenir une première estimation rapide ;
- détecter des biens probablement sous-évalués ou surévalués ;
- comparer beaucoup de logements de manière homogène ;
- aider un expert à prioriser son analyse.

Justification simple :

```text
On utilise un modèle parce qu'il transforme des données historiques en estimation mesurable.
On le surveille parce que la réalité peut changer.
```

---

## 21. Résumé

- La régression linéaire sert à prédire une valeur numérique.
- Elle apprend une formule du type `y = ax + b`.
- `pandas` sert à manipuler les données.
- `scikit-learn` fournit les modèles, le train/test split et les métriques.
- `X` contient les features.
- `y` contient le label.
- `train_test_split` sépare les lignes entre entraînement et test.
- `fit` entraîne le modèle.
- Le modèle doit être entraîné sur `X_train` et `y_train`.
- `predict` utilise le modèle entraîné.
- `coef_` donne le coefficient appris.
- `intercept_` donne le point de départ de la droite.
- L'erreur mesure l'écart entre la vraie valeur et la prédiction.
- La MAE test mesure l'erreur moyenne sur des données non vues.
- La droite apprise doit passer au plus près des points.
- Le modèle doit être suivi dans le temps pour vérifier qu'il reste aligné avec la réalité.
- Ce suivi peut être automatisé en comparant les prédictions aux vraies valeurs récentes.
- Un modèle est utile parce qu'il fournit une estimation rapide, cohérente et mesurable.

---

## 22. Exercice pratique

Notebook à faire :

- [Énoncé : régression linéaire](notebooks/01_regression_lineaire_enonce.ipynb)

Exercice complémentaire sur l'évaluation :

- [Énoncé : train / test split](notebooks/02_train_test_split_enonce.ipynb)

---

## 23. Transition vers le chapitre suivant

La régression linéaire permet de comprendre les bases :

- données d'entrée ;
- valeur à prédire ;
- entraînement ;
- prédiction ;
- erreur ;
- interprétation du modèle.

Le chapitre suivant peut introduire une autre famille de modèles :

1. **KNN** : raisonner par voisinage ;
2. **classification** : prédire une catégorie plutôt qu'une valeur numérique.

La suite logique est donc **KNN**.

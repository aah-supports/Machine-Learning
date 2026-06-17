# Chapitre 5 : Introduction à la régression logistique

## 1. Objectif du chapitre

Après KNN, nous avons vu une première manière de faire de la classification :

```text
chercher les voisins les plus proches
puis voter
```

La régression logistique propose une autre approche.

Elle ne vote pas avec des voisins.

Elle apprend une formule qui estime une probabilité :

```text
Quelle est la probabilité que la classe soit 1, sachant les variables observées ?
```

Le mot **régression** peut surprendre, car le modèle sert souvent à classifier.

Il vient du fait que le modèle calcule d'abord une quantité numérique continue, puis la transforme en probabilité. La décision `0` ou `1` vient seulement à la fin.

Objectifs :

- comprendre pourquoi la régression logistique sert à la classification ;
- comprendre pourquoi on cherche d'abord une probabilité ;
- comprendre les odds, c'est-à-dire le rapport succès / échec ;
- comprendre pourquoi le modèle apprend une droite sur le log-odds ;
- comprendre pourquoi la sigmoïde apparaît ensuite ;
- interpréter une probabilité entre 0 et 1 ;
- comprendre le seuil de décision à `0.5` ;
- préparer le passage vers le perceptron.

---

## 2. Le problème : prédire une classe

Imaginons un étudiant.

On veut prédire s'il valide un module.

Variables possibles :

- nombre d'heures de révision ;
- taux de présence ;
- nombre d'exercices rendus.

La réponse n'est pas un prix ou une température.

La réponse est une classe :

```text
0 = ne valide pas
1 = valide
```

On est donc dans un problème de classification.

Le point de départ de la régression logistique est toujours ce type de situation :

```text
succès / échec
oui / non
classe 1 / classe 0
```

Dans notre exemple :

```text
succès = l'étudiant valide le module
échec  = l'étudiant ne valide pas le module
```

Le modèle ne commence donc pas par chercher une droite abstraite.

Il commence par une question très concrète :

```text
À partir des informations de l'étudiant, quelle est la probabilité de succès ?
```

Mathématiquement :

$$
p = P(Y = 1 \mid x)
$$

où :

- `Y = 1` signifie succès ;
- `Y = 0` signifie échec ;
- `x` représente les variables connues : heures, présence, exercices rendus, etc.

### Rappel : probabilité conditionnelle

La barre verticale `|` se lit **sachant que**.

Donc :

$$
P(Y = 1 \mid x)
$$

se lit :

```text
probabilité que Y vaille 1, sachant que l'on connaît x
```

Dans notre exemple :

$$
P(\text{validation}=1 \mid \text{heures}=6, \text{présence}=80\%)
$$

signifie :

```text
probabilité que l'étudiant valide,
sachant qu'il a révisé 6 heures
et qu'il a 80 % de présence.
```

Ce n'est pas la probabilité générale qu'un étudiant valide.

C'est une probabilité adaptée à un profil précis.

#### Mini-exercice

Traduire chaque notation en phrase.

| Notation | Phrase attendue |
| -------- | --------------- |
| `P(Y = 1 | heures=4)` | ... |
| `P(Y = 1 | présence=90%)` | ... |
| `P(Y = 0 | heures=2, présence=40%)` | ... |

Puis écrire la notation mathématique correspondant aux phrases suivantes :

1. Probabilité qu'un étudiant valide, sachant qu'il a révisé 8 heures.
2. Probabilité qu'un étudiant ne valide pas, sachant qu'il a 50 % de présence.
3. Probabilité qu'un étudiant valide, sachant qu'il a révisé 6 heures et qu'il a 80 % de présence.

Concrètement, on part d'un tableau comme celui-ci :

| Heures de révision | Présence | Valide |
| ------------------ | -------- | ------ |
| 2                  | 40 %     | 0      |
| 4                  | 60 %     | 0      |
| 6                  | 75 %     | 1      |
| 8                  | 90 %     | 1      |

Les colonnes d'entrée sont :

```text
heures de révision, présence
```

La colonne cible est :

```text
valide
```

On veut donc apprendre une relation entre les variables d'entrée et la cible.

Le problème est qu'une droite classique peut produire n'importe quelle valeur :

```text
-0.4
0.3
1.2
2.8
```

Or ici, on ne veut pas une valeur quelconque.

On veut une probabilité de succès :

```text
0 <= p <= 1
```

C'est pour cela que la régression logistique ne modélise pas directement la classe finale.

Elle modélise d'abord :

```text
la probabilité que l'exemple appartienne à la classe 1
```

---

## 3. Pourquoi une courbe logistique ?

Historiquement, la fonction logistique apparaît pour modéliser des phénomènes qui ne peuvent pas augmenter indéfiniment.

Exemple intuitif :

```text
Au début, une croissance peut être lente.
Puis elle accélère.
Puis elle ralentit quand elle approche d'une limite.
```

Cela donne une courbe en S.

Pour une probabilité, cette forme est utile :

```text
probabilité proche de 0  -> classe 0 très probable
probabilité proche de 0.5 -> cas incertain
probabilité proche de 1  -> classe 1 très probable
```

La régression logistique utilise cette idée pour transformer un score quelconque en probabilité bornée entre `0` et `1`.

---

## 4. Pourquoi une probabilité est utile ?

Une classe seule peut être insuffisante.

Deux exemples peuvent être prédits en classe `1`, mais avec des niveaux de confiance très différents.

```text
p = 0.51 -> classe 1, mais décision fragile
p = 0.95 -> classe 1, décision beaucoup plus solide
```

### Exemple simple : validation d'un étudiant

On veut prédire si un étudiant valide un module.

```text
P(validation = 1 | heures=4, présence=60 %) = 0.52
P(validation = 1 | heures=8, présence=90 %) = 0.94
```

Avec un seuil à `0.5`, les deux profils sont prédits en classe `1`.

Mais l'usage n'est pas le même :

- `0.52` : cas limite, accompagnement ou vigilance ;
- `0.94` : validation très probable.

La probabilité donne donc plus d'information qu'une simple étiquette.

### Exemple plus technique : risque de défaut

Une banque peut vouloir estimer le risque qu'un client ne rembourse pas un crédit.

```text
Y = 1 -> défaut de paiement
Y = 0 -> remboursement normal
```

Le modèle peut produire :

```text
P(défaut = 1 | revenus, dette, historique) = 0.08
```

Cela signifie :

```text
risque estimé de défaut : 8 %
```

Cette probabilité peut ensuite servir à définir une règle métier :

```text
risque < 5 %      -> dossier faible risque
5 % à 20 %        -> analyse complémentaire
risque > 20 %     -> dossier très risqué
```

La régression logistique est donc utile quand on veut classifier, mais aussi prioriser et interpréter un niveau de risque.

---

## 5. Point de départ : une probabilité

La régression logistique cherche d'abord une probabilité conditionnelle :

```text
p = P(Y = 1 | x)
```

Dans notre exemple :

```text
Y = 1 -> l'étudiant valide
Y = 0 -> l'étudiant ne valide pas
x     -> les variables de l'étudiant
```

Par exemple, `x` peut contenir :

```text
heures de révision, présence, contrôle continu
```

On cherche donc :

```text
P(validation = 1 | heures, présence, contrôle continu)
```

Une probabilité doit toujours rester entre `0` et `1` :

```text
0 <= p <= 1
```

Le problème est qu'une droite peut produire n'importe quelle valeur :

```text
-3, 0.2, 4, 15, ...
```

On ne peut donc pas modéliser directement `p` avec une droite classique.

---

## 6. Les odds : rapport succès / échec

Au lieu de travailler directement avec `p`, on transforme la probabilité en **odds**.

Les odds comparent la chance de succès à la chance d'échec :

```text
odds = p / (1 - p)
```

Exemples :

| Probabilité p | Odds | Lecture |
| ------------- | ---- | ------- |
| 0.5 | 1 | autant de chances de réussir que d'échouer |
| 0.75 | 3 | 3 fois plus de chances de réussir que d'échouer |
| 0.9 | 9 | 9 fois plus de chances de réussir que d'échouer |
| 0.1 | 1/9 | 9 fois moins de chances de réussir que d'échouer |

Les odds sont utiles parce que beaucoup d'effets sont multiplicatifs.

Exemple :

```text
chaque heure de révision multiplie les odds par 2
```

| Heures | Odds |
| ------ | ---- |
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |

On voit que les odds peuvent augmenter très vite.

Ce n'est pas une droite : c'est une progression multiplicative.

---

## 7. Le log-odds : rendre la relation linéaire

Les odds vont de `0` à `+infini`.

Une droite, elle, peut aller de `-infini` à `+infini`.

Pour obtenir une quantité compatible avec une droite, on prend le logarithme des odds :

```text
log-odds = log(p / (1 - p))
```

Exemples :

| p | odds | log-odds |
| -- | ---- | -------- |
| 0.1 | 1/9 | -2.2 |
| 0.5 | 1 | 0 |
| 0.9 | 9 | 2.2 |

Le logarithme transforme une multiplication en addition.

Donc si les odds évoluent de manière multiplicative, le log-odds peut évoluer de manière presque linéaire.

---

## 8. L'hypothèse fondamentale

La régression logistique fait une hypothèse simple :

> Le log-odds est une fonction linéaire des variables.

Avec une variable :

```text
log(p / (1 - p)) = a * x + b
```

Avec plusieurs variables :

```text
log(p / (1 - p)) = w1 * x1 + w2 * x2 + ... + b
```

Cette ligne est le coeur du modèle.

La régression logistique ne dit pas :

```text
la probabilité est une droite
```

Elle dit :

```text
le logarithme du rapport succès / échec est une droite
```

---

## 9. D'où vient la sigmoïde ?

On part de l'hypothèse :

```text
log(p / (1 - p)) = z
```

où :

```text
z = w1 * x1 + w2 * x2 + ... + b
```

Si on résout cette équation pour retrouver `p`, on obtient :

```text
p = 1 / (1 + e^(-z))
```

C'est la fonction sigmoïde.

La sigmoïde n'est donc pas un choix arbitraire.

Elle apparaît parce qu'on veut repasser du log-odds à une probabilité.

Quelques valeurs :

| z | sigmoïde(z) |
| -- | ----------- |
| -4 | 0.018 |
| -2 | 0.119 |
| 0 | 0.5 |
| 2 | 0.881 |
| 4 | 0.982 |

---

## 10. Score, probabilité, classe

Le modèle suit donc cette chaîne :

```text
variables
-> score linéaire z
-> sigmoïde(z)
-> probabilité p
-> classe 0 ou 1
```

Prenons un exemple très simple avec une seule variable : les heures de révision.

Supposons que le modèle appris soit :

$$
z = 0.8 \times \text{heures} - 4
$$

Ici, `z` est le score linéaire.

Ce score n'est pas encore une probabilité.

On le transforme ensuite avec la sigmoïde :

$$
p = \frac{1}{1+e^{-z}}
$$

### Étudiant A : 2 heures de révision

Calcul du score :

$$
z = 0.8 \times 2 - 4
$$

$$
z = -2.4
$$

Calcul de la probabilité :

$$
p = \frac{1}{1+e^{-(-2.4)}}
$$

$$
p = \frac{1}{1+e^{2.4}}
$$

$$
p \approx 0.083
$$

Donc :

```text
P(réussite) ≈ 8.3 %
```

### Étudiant B : 5 heures de révision

Calcul du score :

$$
z = 0.8 \times 5 - 4
$$

$$
z = 0
$$

Calcul de la probabilité :

$$
p = \frac{1}{1+e^0}
$$

$$
p = 0.5
$$

Donc :

```text
P(réussite) = 50 %
```

C'est le cas limite : le modèle hésite autant entre échec et réussite.

### Étudiant C : 10 heures de révision

Calcul du score :

$$
z = 0.8 \times 10 - 4
$$

$$
z = 4
$$

Calcul de la probabilité :

$$
p = \frac{1}{1+e^{-4}}
$$

$$
p \approx 0.982
$$

Donc :

```text
P(réussite) ≈ 98.2 %
```

On obtient :

| Heures | Score `z` | Probabilité de réussite |
| ------ | --------- | ----------------------- |
| 2      | -2.4      | 8.3 %                   |
| 5      | 0         | 50 %                    |
| 10     | 4         | 98.2 %                  |

Le mécanisme est toujours :

1. Calcul du score linéaire :

$$
z = ax + b
$$

2. Transformation en probabilité :

$$
p = \sigma(z)
$$

3. Décision éventuelle :

```text
si p < 0.5  -> échec
si p >= 0.5 -> réussite
```

Ce qui est remarquable, c'est que le modèle ne prédit pas directement :

```text
réussite ou échec
```

Il prédit d'abord une probabilité de réussite.

Puis on choisit éventuellement une classe à partir de cette probabilité.

---

## 11. Version mathématique du modèle

Pour chaque observation `i`, on note :

```text
x_i = variables de l'observation
y_i = classe observée, 0 ou 1
```

La régression logistique suppose que :

```text
Y_i | x_i suit une loi de Bernoulli(p_i)
```

Cela signifie :

```text
P(Y_i = 1 | x_i) = p_i
P(Y_i = 0 | x_i) = 1 - p_i
```

Puis elle modélise le log-odds de `p_i` par une fonction linéaire :

```text
log(p_i / (1 - p_i)) = w^T x_i + b
```

Donc :

```text
p_i = 1 / (1 + e^(-(w^T x_i + b)))
```

L'entraînement consiste à trouver les poids `w` et le biais `b` qui rendent les labels observés les plus probables.

Pour une observation, la probabilité du label observé peut s'écrire :

```text
p_i^y_i * (1 - p_i)^(1 - y_i)
```

En pratique, on maximise la vraisemblance, ou de manière équivalente, on minimise la log-loss :

```text
loss = - [ y_i log(p_i) + (1 - y_i) log(1 - p_i) ]
```

Intuition :

- si `y_i = 1`, on veut que `p_i` soit proche de `1` ;
- si `y_i = 0`, on veut que `p_i` soit proche de `0`.

---

## 12. Lien avec KNN

KNN et la régression logistique peuvent tous les deux faire de la classification.

Mais ils ne raisonnent pas de la même manière.

| Modèle | Idée principale |
| ------ | --------------- |
| KNN | comparer aux voisins les plus proches |
| Régression logistique | modéliser le log-odds, puis produire une probabilité |

KNN garde les exemples.

La régression logistique apprend des paramètres :

```text
w1, w2, ..., b
```

---

## 13. Transition vers le perceptron

Le perceptron utilise une idée très proche :

```text
z = w1 * x1 + w2 * x2 + b
p = sigmoid(z)
```

Puis il corrige les poids quand la prédiction est mauvaise.

La régression logistique prépare donc naturellement le passage vers :

- les poids ;
- le biais ;
- la sigmoïde ;
- la descente de gradient ;
- les réseaux de neurones.

---

## 14. Mini-exercice : prédire une validation

On dispose d'un petit dataset d'étudiants.

Le dataset n'est pas parfaitement séparé : certains cas sont limites. C'est volontaire, car une régression logistique est surtout utile quand on veut lire une probabilité, pas seulement une classe.

```python
import pandas as pd

df = pd.DataFrame({
    "heures_revision": [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 9, 10],
    "presence": [35, 40, 55, 45, 50, 70, 55, 75, 65, 60, 85, 80, 90, 95],
    "controle_continu": [6, 7, 8, 7, 9, 10, 10, 12, 11, 10, 14, 13, 15, 16],
    "valide": [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
})
```

Objectif :

```text
Prédire si un étudiant valide le module.
```

### Étape 1 - Séparer X et y

Créer :

```python
X = df[["heures_revision", "presence", "controle_continu"]]
y = df["valide"]
```

### Étape 2 - Entraîner le modèle

On utilise un pipeline pour normaliser les variables avant la régression logistique.

Compléter les `...` :

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

modele = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

modele.fit(..., ...)
```

### Étape 3 - Tester deux nouveaux étudiants

On veut comparer deux profils.

| Profil | Heures | Présence | Contrôle continu |
| ------ | ------ | -------- | ---------------- |
| A      | 4      | 60       | 9                |
| B      | 8      | 85       | 14               |

Compléter :

```python
nouveaux_etudiants = pd.DataFrame({
    "heures_revision": [4, 8],
    "presence": [60, 85],
    "controle_continu": [9, 14]
})

classes = ...
probabilites = ...
```

### Étape 4 - Lire les probabilités

`predict_proba` renvoie une probabilité pour chaque classe.

Afficher les classes dans l'ordre utilisé par le modèle :

```python
modele.classes_
```

Puis construire un tableau lisible :

```python
resultats = pd.DataFrame(
    probabilites,
    columns=[f"proba_classe_{c}" for c in modele.classes_]
)

resultats["classe_predite"] = classes
resultats
```

### Questions

1. Quelle classe est prédite pour le profil A ?
2. Quelle est la probabilité de validation du profil A ?
3. Quelle classe est prédite pour le profil B ?
4. Quelle est la probabilité de validation du profil B ?
5. Pourquoi le profil A peut-il être plus incertain que le profil B ?
6. Pourquoi `predict_proba` est-il plus informatif que `predict` ?

### Phrase attendue

Rédiger une phrase de ce type :

```text
Pour le profil ..., le modèle prédit la classe ... avec une probabilité de validation d'environ ... %.
```

---

## 15. Exercices de fin de partie

### Exercice 1 - Passer d'une probabilité aux odds

On étudie la probabilité qu'un étudiant valide un module.

Pour chaque profil, compléter les colonnes manquantes.

Rappels :

$$
\text{odds}=\frac{p}{1-p}
$$

$$
\text{log-odds}=\log\left(\frac{p}{1-p}\right)
$$

Quelques approximations utiles :

```text
log(0.25) ≈ -1.39
log(1)    = 0
log(3)    ≈ 1.10
log(9)    ≈ 2.20
```

| Profil | Probabilité de validation `p` | Odds | Log-odds | Interprétation |
| ------ | ----------------------------- | ---- | -------- | -------------- |
| A      | 0.20                          | ...  | ...      | ...            |
| B      | 0.50                          | ...  | ...      | ...            |
| C      | 0.75                          | ...  | ...      | ...            |
| D      | 0.90                          | ...  | ...      | ...            |

Questions :

1. Quel profil est exactement sur la frontière de décision ?
2. Quel profil a 3 fois plus de chances de valider que de ne pas valider ?
3. Quel profil a 9 fois plus de chances de valider que de ne pas valider ?
4. Pourquoi le log-odds est-il négatif quand la probabilité est inférieure à 0.5 ?
5. Pourquoi le log-odds est-il plus adapté qu'une probabilité pour construire une droite ?

Phrase attendue :

```text
Pour le profil ..., les odds valent ..., ce qui signifie que l'étudiant a ... fois plus de chances de valider que de ne pas valider.
```

---

### Exercice 2 - Prendre une décision avec un seuil

Un modèle de régression logistique prédit la probabilité de validation suivante :

$$
p=P(Y=1 \mid x)
$$

| Étudiant | Probabilité de validation |
| -------- | ------------------------- |
| A        | 0.42                      |
| B        | 0.58                      |
| C        | 0.76                      |
| D        | 0.91                      |

#### Partie 1 - Seuil classique

Avec un seuil de décision à `0.5`, compléter :

| Étudiant | Probabilité | Classe prédite |
| -------- | ----------- | -------------- |
| A        | 0.42        | ...            |
| B        | 0.58        | ...            |
| C        | 0.76        | ...            |
| D        | 0.91        | ...            |

#### Partie 2 - Seuil plus strict

L'école décide maintenant qu'un étudiant est considéré comme "validation probable" seulement si :

$$
p \geq 0.7
$$

Compléter :

| Étudiant | Probabilité | Classe prédite avec seuil 0.7 |
| -------- | ----------- | ----------------------------- |
| A        | 0.42        | ...                           |
| B        | 0.58        | ...                           |
| C        | 0.76        | ...                           |
| D        | 0.91        | ...                           |

Questions :

1. Quels étudiants changent de classe quand on passe du seuil `0.5` au seuil `0.7` ?
2. Pourquoi un établissement pourrait-il choisir un seuil plus strict que `0.5` ?
3. Quelle différence y a-t-il entre la probabilité prédite et la classe finale ?
4. Pourquoi `predict_proba` est-il plus riche que `predict` dans ce cas ?

Version Python :

```python
import numpy as np

probabilites = np.array([0.42, 0.58, 0.76, 0.91])

classes_seuil_05 = (probabilites >= 0.5).astype(int)
classes_seuil_07 = (probabilites >= 0.7).astype(int)

print(classes_seuil_05)
print(classes_seuil_07)
```

---

### Pour aller plus loin

- [Exercice complet 1 : odds, log-odds et sigmoïde](regression_logistique/Exercices/01_log_odds_sigmoide.md)
- [Exercice complet 2 : entraîner une régression logistique avec Scikit-Learn](regression_logistique/Exercices/02_validation_etudiants_sklearn.md)
- [Exercice complet 3 : calculer une probabilité avec la sigmoïde](regression_logistique/Exercices/03_calcul_sigmoide_reussite.md)
- [Correction exercice 3 : calculer une probabilité avec la sigmoïde](regression_logistique/Corrections/03_calcul_sigmoide_reussite_correction.md)
- [Énoncé notebook : régression logistique](notebooks/03_regression_logistique_enonce.ipynb)
- [Correction notebook : régression logistique](notebooks/corrections/03_regression_logistique_correction.ipynb)

### Supplément : probabilités et simulation

- [Énoncé : simulation de deux dés](regression_logistique/Exercices/03_simulation_des.md)
- [Correction : simulation de deux dés](regression_logistique/Corrections/03_simulation_des_correction.md)
- [Énoncé : visualiser une loi normale avec Matplotlib](regression_logistique/Exercices/04_loi_normale_matplotlib.md)
- [Correction : visualiser une loi normale avec Matplotlib](regression_logistique/Corrections/04_loi_normale_matplotlib_correction.md)

# Exercice 1 : odds, log-odds et sigmoïde

## Objectif

Comprendre la mécanique mathématique de la régression logistique sans utiliser Scikit-Learn.

On veut prédire si un étudiant valide un module :

```text
Y = 1 -> l'étudiant valide
Y = 0 -> l'étudiant ne valide pas
```

La régression logistique ne modélise pas directement la probabilité avec une droite.

Elle modélise :

```text
log(p / (1 - p))
```

où :

```text
p = P(Y = 1 | x)
```

---

## Partie 1 - Probabilité et odds

Compléter le tableau.

Rappel :

```text
odds = p / (1 - p)
```

| Probabilité p | Odds | Interprétation |
| ------------- | ---- | -------------- |
| 0.50 | ... | ... |
| 0.75 | ... | ... |
| 0.90 | ... | ... |
| 0.20 | ... | ... |

### Questions

1. Que signifie `odds = 1` ?
2. Que signifie `odds = 3` ?
3. Pourquoi les odds peuvent-ils dépasser `1` alors qu'une probabilité ne peut pas dépasser `1` ?

---

## Partie 2 - Log-odds

Compléter le tableau.

Rappel :

```text
log-odds = log(odds)
```

Valeurs utiles :

```text
log(1) ≈ 0
log(3) ≈ 1.10
log(9) ≈ 2.20
log(0.25) ≈ -1.39
```

| Probabilité p | Odds | Log-odds |
| ------------- | ---- | -------- |
| 0.50 | 1 | ... |
| 0.75 | 3 | ... |
| 0.90 | 9 | ... |
| 0.20 | 0.25 | ... |

### Questions

1. Pourquoi le log-odds vaut-il `0` quand `p = 0.5` ?
2. Que signifie un log-odds positif ?
3. Que signifie un log-odds négatif ?

---

## Partie 3 - Score linéaire et probabilité

On suppose que le modèle a appris :

```text
z = 0.8 * heures_revision - 3
```

Compléter le tableau.

Rappel :

```text
p = 1 / (1 + e^(-z))
```

Valeurs utiles :

```text
sigmoïde(-2.2) ≈ 0.10
sigmoïde(-0.6) ≈ 0.35
sigmoïde(0.2)  ≈ 0.55
sigmoïde(1.8)  ≈ 0.86
```

| Heures de révision | z | Probabilité estimée | Classe avec seuil 0.5 |
| ------------------ | -- | ------------------- | --------------------- |
| 1 | ... | ... | ... |
| 3 | ... | ... | ... |
| 4 | ... | ... | ... |
| 6 | ... | ... | ... |

### Questions finales

1. À partir de combien d'heures la classe prédite devient-elle `1` ?
2. Pourquoi le modèle ne dit-il pas "réussite certaine" ?
3. Quelle est la différence entre la probabilité estimée et la classe prédite ?


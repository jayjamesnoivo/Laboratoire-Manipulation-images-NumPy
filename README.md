# ÉNONCÉ du Laboratoire — Manipulation d’images avec NumPy

## Objectif

Dans ce laboratoire, vous allez apprendre à manipuler une image comme une **matrice NumPy**. Vous appliquerez différentes transformations pour modifier l’image et observer l’effet sur les pixels.

À la fin de ce laboratoire, vous serez capables de :

- comprendre qu’une image est une **matrice de pixels**
- utiliser **indexing et slicing**
- modifier des pixels selon des conditions
- appliquer des transformations simples à une image.

---

# Partie 1 — Charger et afficher une image

Importer les bibliothèques nécessaires.

```python id="lab1"
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
```

Charger une image :

```python id="lab2"
image = data.camera()
```

Afficher l’image :

```python id="lab3"
plt.imshow(image, cmap="gray")
plt.axis("off")
```

---

### Questions

1. Quelle est la dimension de l’image ?

Indice :

```python id="lab4"
image.shape
```

2. Que représente chaque valeur dans la matrice ?

---

# Partie 2 — Explorer les pixels

Afficher la valeur du pixel à la position suivante :

```python id="lab5"
image[100,200]
```

### Questions

1. Cette valeur correspond à quoi ?
2. Pourquoi les valeurs sont-elles comprises entre **0 et 255** ?

---

# Partie 3 — Découper une image (slicing)

Extraire une zone centrale de l’image.

```python id="lab6"
zoom = image[200:400,300:450]

plt.imshow(zoom, cmap="gray")
plt.axis("off")
```

### Questions

1. Quelle est la taille de la nouvelle image ?
2. Que se passe-t-il si vous changez les indices ?

---

# Partie 4 — Modifier la luminosité

Créer une image plus claire.

```python id="lab7"
bright = image + 50
bright = np.clip(bright,0,255)

plt.imshow(bright, cmap="gray")
plt.axis("off")
```

Comme l'image est de type uint8. Ça veut dire que chaque information est sauvegardée sur 8bits. Ça nous donne une possibilité de 256.

Lorsque le 255 est dépasse, le uint8 reprend ses calculs à zéro. Donc 255 + 1 ça donne 0. 255 + 50 ça done 49.

Pendant que nous utilisions d'éclaircir la photo, les données de plus 204 devenait grises et noires.

Voici donc une solution altéranative.

Cependant, garde en tête l'utilité de **np.clip**

```python id="lab8"
bright = np.copy(image)
bright[bright >204] = 255
bright[bright <205] = bright[bright < 205] + 50
plt.imshow(bright)
```

### Questions

1. Pourquoi utilise-t-on `np.clip()` ?
2. Que se passe-t-il si on ne l’utilise pas ?

---

# Partie 5 — Créer un négatif

Créer le négatif de l’image.

Indice :

```python id="lab9"
negative = 255 - image
```

Afficher le résultat.

---

# Partie 6 — Seuillage

Transformer l’image en image **noir et blanc**.

Règle :

- pixel > 128 → blanc
- pixel ≤ 128 → noir

Indice :

```python id="lab10"
binary = np.copy(image)

binary[binary > 128] = 255
binary[binary <= 128] = 0
```

Afficher le résultat.

---

# Partie 7 — Détection de zones lumineuses

Créer une image où seules les zones très lumineuses sont visibles.

Règle :

- pixel > 200 → blanc
- sinon → noir

---

# Partie 8 — Ajouter du bruit

Ajouter du bruit aléatoire dans l’image.

Indice :

```python id="lab11"
noise = np.random.randint(-30,30,image.shape)

noisy = image + noise
noisy = np.clip(noisy,0,255)
```

Afficher l’image bruitée.

---

# Partie 9 — Défi

Créer un filtre qui :

1. rend les pixels très sombres complètement noirs
2. rend les pixels très clairs complètement blancs

Règle :

```text
pixel < 50 → 0
pixel > 200 → 255
```

Afficher le résultat.

---

# Partie 10 — Bonus (exploration)

Créer une image pixelisée.

Indice :

diviser l’image en blocs **10 × 10** et remplacer chaque bloc par sa moyenne.

---

# Questions de réflexion

1. Pourquoi peut-on manipuler une image comme une matrice ?
2. Quelle transformation vous semble la plus utile ?
3. Quel est le lien entre ces opérations et le **machine learning** ?

---

# À retenir

Une image est simplement :

```text
une matrice de pixels
```

Cela signifie que toutes les opérations vues avec **NumPy** peuvent être appliquées aux images :

- slicing
- indexing
- boolean indexing
- opérations matricielles.

Ces concepts sont utilisés dans :

- la vision par ordinateur
- le traitement d’image
- les réseaux de neurones convolutifs.

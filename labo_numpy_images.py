import numpy as np
import matplotlib.pyplot as plt
from skimage import data

# Charger une image exemple
image = data.camera()

# Afficher l'image
plt.imshow(image, cmap="gray")
plt.axis("off")
plt.show()

print("Dimension de l'image :", image.shape)

# ------------------------------
# PARTIE 1 - Charger et afficher une image
# ------------------------------

# QUESTION 1
# Quelle est la dimension de l'image ?
# Réponse : (512, 512)

# QUESTION 2
# Que représente chaque valeur dans la matrice ?
# Réponse : Chaque valeur représente la luminosité d'un pixel.
# 0 = noir, 255 = blanc, les autres valeurs sont des niveaux de gris.

# -----------------------------
# PARTIE 2 - Explorer les pixels
# -----------------------------

print("Valeur du pixel [100,200] :", image[100,200])

# QUESTION 1
# Cette valeur correspond à quoi ?
# Réponse : Cette valeur représente la luminosité du pixel situé à la position (100,200).

# QUESTION 2
# Pourquoi les valeurs sont-elles comprises entre 0 et 255 ?
# Réponse : Parce que l'image est codée sur 8 bits.
# Cela donne 256 niveaux possibles de gris (0 à 255).

# -----------------------------
# PARTIE 3 - Découper une image (slicing)
# -----------------------------

zoom = image[200:400,300:450]

plt.imshow(zoom, cmap="gray")
plt.axis("off")
plt.show()

print("Taille du zoom :", zoom.shape)

# QUESTION 1
# Quelle est la taille de la nouvelle image ?
# Réponse : (200, 150)

# QUESTION 2
# Que se passe-t-il si vous changez les indices ?
# Réponse : On découpe une autre zone de l'image.
# Si on augmente les indices, la zone devient plus grande.
# Si on les diminue, la zone devient plus petite.

# -----------------------------
# PARTIE 4 - Modifier la luminosité
# -----------------------------

bright = image + 50
bright = np.clip(bright, 0, 255)

plt.imshow(bright, cmap="gray")
plt.axis("off")
plt.show()

# QUESTION 1
# Pourquoi utilise-t-on np.clip() ?
# Réponse : Pour s'assurer que les valeurs restent entre 0 et 255.

# QUESTION 2
# Que se passe-t-il si on ne l'utilise pas ?
# Réponse : Les valeurs peuvent dépasser 255 et produire des résultats incorrects dans l'image.

# -----------------------------
# PARTIE 5 - Créer un négatif
# -----------------------------

negative = 255 - image

plt.imshow(negative, cmap="gray")
plt.axis("off")
plt.show()

# -----------------------------
# PARTIE 6 - Seuillage
# -----------------------------

binary = np.copy(image)

binary[binary > 128] = 255
binary[binary <= 128] = 0

plt.imshow(binary, cmap="gray")
plt.axis("off")
plt.show()

# -----------------------------
# PARTIE 7 - Détection de zones lumineuses
# -----------------------------

zones = np.copy(image)

zones[zones > 200] = 255
zones[zones <= 200] = 0

plt.imshow(zones, cmap="gray")
plt.axis("off")
plt.show()

# -----------------------------
# PARTIE 8 - Ajouter du bruit
# -----------------------------

noise = np.random.randint(-30, 30, image.shape)

noisy = image + noise
noisy = np.clip(noisy, 0, 255)

plt.imshow(noisy, cmap="gray")
plt.axis("off")
plt.show()

# -----------------------------
# PARTIE 9 - Défi
# -----------------------------

filtre = np.copy(image)

filtre[filtre < 50] = 0
filtre[filtre > 200] = 255

plt.imshow(filtre, cmap="gray")
plt.axis("off")
plt.show()

# -----------------------------
# PARTIE 10 - Bonus (Pixeliser l'image)
# -----------------------------

pixelisee = np.copy(image)

for i in range(0, image.shape[0], 10):
    for j in range(0, image.shape[1], 10):
        bloc = pixelisee[i:i+10, j:j+10]
        moyenne = int(np.mean(bloc))
        pixelisee[i:i+10, j:j+10] = moyenne

plt.imshow(pixelisee, cmap="gray")
plt.axis("off")
plt.show()
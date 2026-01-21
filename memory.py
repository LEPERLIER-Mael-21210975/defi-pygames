import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()

# Fenetre de jeu
largeur, hauteur = 1000, 1000
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Mon jeu de mémoire très sophistiqué')

# couleur fenetre
violet = "purple"

#couleur cartes
vert = "green"

# varaibles pour les cartes
carte_largeur = 200
carte_hauteur = 200
espacement_des_cartes = 10
nb_lignes = 4
nb_colonnes = 4

# police de texte nécessaire pour afficher les nombres sur les cartes
typo = pygame.font.Font("fonts/crazy_Writerz.ttf", 72)


## Génération des paires de cartes

# Calculer le nombre de paires nécessaires
nombre_de_cartes_total = nb_lignes * nb_colonnes
nombre_de_paires = nombre_de_cartes_total // 2

# Génération d'une liste de nombre sous forme de chaînes de caractères afin que chaque nombre puisse être affiché sur une carte
paires = []
for nombre in range(nombre_de_paires):
    paires.append(str(nombre))
    paires.append(str(nombre))

# Mélanger les paires aléatoirement grâce à shuffle de la bilbiothèque random
random.shuffle(paires)


# Création de la grille de cartes ou deck de cartes
deck = []

## On parcourt les cartes pour les positionner dans la fenêtre

# Parcourir chaque ligne de la grille
for ligne in range(nb_lignes):
    # Parcourir chaque colonne de la grille
    for colonne in range(nb_colonnes):

        # Calcul de la position X
        largeur_grille = (carte_largeur + espacement_des_cartes) * nb_colonnes
        marge_gauche = (largeur - largeur_grille) // 2
        x = colonne * (carte_largeur + espacement_des_cartes) + marge_gauche

        # Calcul de la position Y
        hauteur_grille = (carte_hauteur + espacement_des_cartes) * nb_lignes
        marge_haut = (hauteur - hauteur_grille) // 2
        y = ligne * (carte_hauteur + espacement_des_cartes) + marge_haut

        # Création d'un dictionnaire pour chaque carte
        carte = {
            "valeur_carte": paires.pop(),
            "dessin_carte": pygame.Rect(x, y, carte_largeur, carte_hauteur),
            "carte_retournee": False,
            "carte_identique": False
        }

        # Ajouter la carte au deck de cartes
        deck.append(carte)


# Variables du jeu
cartes_retournees = []
paires_trouvees = 0

# Boucle du jeu
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Vérifie si une carte a été cliquée et si toutes les paires n'ont pas encore été trouvées
    if event.type == pygame.MOUSEBUTTONDOWN and paires_trouvees < nombre_de_paires:
        # Méthode pygame pour obtenir la position de la souris
        mouse_pos = pygame.mouse.get_pos()
        # Parcourt toutes les cartes pour vérifier si une carte a été cliquée
        for carte in deck:
            # On commence par vérifier que la carte n'est pas déjà identique
            # et si la position de la souris est bien sur la carte
            if not carte["carte_identique"] and carte["dessin_carte"].collidepoint(mouse_pos):
                # Si la carte n'est pas encore retournée
                if not carte["carte_retournee"]:
                    # Retourne la carte
                    carte["carte_retournee"] = True
                    # Ajoute la carte à la liste des cartes retournées
                    cartes_retournees.append(carte)
                    # Si deux cartes sont retournées
                    if len(cartes_retournees) == 2:
                        # Vérifie si les deux cartes retournées ont la même valeur
                        if cartes_retournees[0]["valeur_carte"] == cartes_retournees[1]["valeur_carte"]:
                            # Marque les cartes comme identiques
                            cartes_retournees[0]["carte_identique"] = True
                            cartes_retournees[1]["carte_identique"] = True
                            # Incrémente le nombre de paires trouvées
                            paires_trouvees += 1
                        else:
                            # Retourne les cartes face cachée si elles ne correspondent pas
                            cartes_retournees[0]["carte_retournee"] = False
                            cartes_retournees[1]["carte_retournee"] = False
                        # Réinitialise la liste des cartes retournées
                        cartes_retournees = []

    # Changer la couleur de fond de l'écran
    fenetre.fill(violet)

   # Parcourir toutes les cartes du jeu
    for carte in deck:
        # Si la carte est retournée (face visible)
        if carte["carte_retournee"]:
            # Dessiner la carte
            pygame.draw.rect(fenetre, vert, carte["dessin_carte"])
            # Créer le texte correspondant à la valeur de la carte
            texte_surface = typo.render(
                carte["valeur_carte"],
                True, #antialiasing
                violet
            )
            # Centrer le texte sur la carte
            texte_rect = texte_surface.get_rect(center=carte["dessin_carte"].center)
            # Afficher le texte sur la carte
            fenetre.blit(texte_surface, texte_rect)

        # Si la carte est face cachée
        else:
            # Dessiner uniquement le dos de la carte
            pygame.draw.rect(fenetre, vert, carte["dessin_carte"])


    # on oublie pas de mettre à jour l'affichage
    pygame.display.update()
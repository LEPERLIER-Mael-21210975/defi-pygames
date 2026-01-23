import pygame, sys
from pygame.locals import QUIT

pygame.init()

largeur, hauteur = 400 , 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Dédale Pygame!')


# On détermine la différente couleur des éléments du jeu
couleur_fenetre = "purple"
couleur_mur = "green"
couleur_joueur = "red"
couleur_fin = "black"

# Dimensions des cellules carrés en pixels
cellule = 40

# Position des murs (très fastidieux)
murs = [
    # Ligne 1 (y=1)
    (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1),
    # Ligne 2 (y=2)
    (0, 2), (2, 2), (8, 2), (9, 2),
    # Ligne 3 (y=3)
    (0, 3), (4, 3), (6, 3),
    # Ligne 4 (y=4)
    (0, 4), (3, 4), (4, 4), (6, 4), (7, 4), (8, 4),
    # Ligne 5 (y=5)
    (0, 5), (1, 5), (3, 5), (8, 5),
    # Ligne 6 (y=6)
    (0, 6), (3, 6), (5, 6), (7, 6), (8, 6),
    # Ligne 7 (y=7)
    (5, 7), (7, 7),
    # Ligne 8 (y=8)
    (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (7, 8), (9, 8),
    # Ligne 9 (y=9)
    (7, 9)
]


# Coordonnées du joueur
joueur_position_x = cellule
joueur_position_y = cellule

# Police de texte
font = pygame.font.Font("fonts/crazy_Writerz.ttf", 36)

# Coordonnées du point d'arrivée
# //2 -> divise la taille d'une cellule par 2. Cela positionne l'arrivée une demi-cellule avant le bord de la fenêtre.
arrivee_x = largeur - cellule // 2
arrivee_y = hauteur - cellule // 2


while True:
    print(joueur_position_x // 40, joueur_position_y // 40)
    for event in pygame.event.get():
        # On oublie pas de mettre la condition de sortie
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Déplacement du joueur
        # On récupère les entrées du clavier comme dans le snake
        # mais avant de changer la position du joueur on vérifie
        # qu'il ne sorte pas des limites de la fenêtre
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if joueur_position_x > 0:
                    joueur_position_x -= cellule
            elif event.key == pygame.K_RIGHT:
                if joueur_position_x < largeur - cellule:
                    joueur_position_x += cellule
            elif event.key == pygame.K_UP:
                if joueur_position_y > 0:
                    joueur_position_y -= cellule
            elif event.key == pygame.K_DOWN:
                if joueur_position_y < hauteur - cellule:
                    joueur_position_y += cellule

    # Vérifier si la position actuelle du joueur est dans un mur
    if (joueur_position_x // cellule, joueur_position_y // cellule) in murs:
        # On crée le texte
        game_over_text = font.render("GAME OVER", True, couleur_fin)
        # Puis on l'écrit
        fenetre.blit(game_over_text, (largeur // 2 - game_over_text.get_width() // 2, hauteur // 2 - game_over_text.get_height() // 2))
        # Mettre à jour l'affichage pour voir le texte
        pygame.display.update()
        # Attendre (2 secondes) avant de fermer le jeu pour que le joueur puisse voir le game over
        pygame.time.wait(2000)
        # On ferme comme quand on appuie sur la croix
        pygame.quit()
        sys.exit()


    # Exactement de la même manière que pour la défaite lorsqu'on touche un mur
    # la victoire lorsqu'on touche l'objectif
    if joueur_position_x - arrivee_x > -40 and joueur_position_y - arrivee_y > -40:
        victoire_text = font.render("VICTOIRE", True, couleur_joueur)
        fenetre.blit(victoire_text, (largeur // 2 - victoire_text.get_width() // 2, hauteur // 2 - victoire_text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000)      
        pygame.quit()
        sys.exit()

    fenetre.fill(couleur_fenetre)

    # Dessiner les murs (en les aggrandissant avec la taille des cellules)
    for mur in murs:
        pygame.draw.rect(fenetre, couleur_mur, (mur[0] * cellule, mur[1] * cellule, cellule, cellule))

    # Dessiner le joueur
    pygame.draw.rect(fenetre, couleur_joueur, (joueur_position_x, joueur_position_y, cellule, cellule))

    # Dessiner le point d'arrivée
    pygame.draw.rect(fenetre, couleur_fin,(arrivee_x - cellule // 2, arrivee_y - cellule // 2, cellule, cellule))

    # On oublie pas de mettre à jour l'affichage
    pygame.display.update()
import pygame, sys
from pygame.locals import QUIT
import random
import os

pygame.init()
# Initialiser le mixer pour rajouter une musique de fond
pygame.mixer.init()

largeur, hauteur = 500, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Solid Snake comme dans Metal Gear!')

# Choix des couleurs du fond, du serpent et de la "pomme" (très carré pour une pomme quand même)
couleur_fond = "purple"
couleur_serpent = "green"
couleur_pomme = "black"

# police de texte nécessaire pour afficher le texte de défaite
police = pygame.font.Font("fonts/crazy_Writerz.ttf", 50)

# Taille des cellules et nombre de cellules qui composent le damier
taille_cellule = 20
nb_cellule_x = largeur // taille_cellule
nb_cellule_y = hauteur // taille_cellule


# Horloge pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()

ips = 10  # images par seconde

# Définir des déplacements du serpent
# Chaque direction est représentée par un tuple (x, y)
# Attention: l'axe Y est inversé dans Pygame (vers le bas augmente Y)
haut = (0, -1)
bas = (0, 1)
gauche = (-1, 0)
droite = (1, 0)

# Charger les fichiers audios
son_jeu = pygame.mixer.Sound(os.path.join('sounds/eva_op.mp3'))
son_jeu.set_volume(0.1)


# Fonction pour démarrer le jeu
def jouer():
    # Jouer la musique de fond en boucle
    son_jeu.play()
    # Initialiser le serpent avec trois segments
    snake = [(9, 5), (8, 5), (7, 5)]
    # Direction de départ du serpent
    direction = droite
    # Initialiser la pomme à manger à une position aléatoire
    pomme = (random.randint(0, nb_cellule_x - 1), random.randint(0, nb_cellule_y - 1))


    while True:
        for event in pygame.event.get():
            # Gérer la fermeture de la fenêtre
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # On rentre dans le if seulement si une touche est enfoncée
            if event.type == pygame.KEYDOWN:
                # Vérifie si la touche enfoncée est flèche haut
                # et que la direction actuelle n'est pas bas car on ne peut pas faire litéralement demi-tour
                if event.key == pygame.K_UP and direction != bas:
                    # Changer la direction du serpent vers le haut
                    direction = haut
                elif event.key == pygame.K_DOWN and direction != haut:
                    direction = bas
                elif event.key == pygame.K_LEFT and direction != droite:
                    direction = gauche
                elif event.key == pygame.K_RIGHT and direction != gauche:
                    direction = droite

        # Déplacement du snake
        # Position actuelle de la tete du serpent
        deplacement = snake[0]
        # Calculer les nouvelles coordonnées de la tête en ajoutant sa direction depuis la position actuelle
        x = deplacement[0] + direction[0]
        y = deplacement[1] + direction[1]
        # Insère les nouvelles coordonnées de la tête au début de la liste du serpent
        snake.insert(0, (x, y))

        # Gestion des collisions sur les bords en vérifiant si la tête du serpent est hors des limites
        if (x < 0 or x >= nb_cellule_x) or (y < 0 or y >= nb_cellule_y) or (snake.count((x, y)) > 1):
            # Stopper le son du jeu et relancer une nouvelle partie quand le serpent meurt
            son_jeu.stop()
            texte_defaite = police.render("Bravo ! Vous avez fait " + str(len(snake) - 4) + " points", True, "green")
            fenetre.blit(texte_defaite, (25, 200))
            pygame.display.update()
            pygame.event.wait(2000)
            jouer()

        # Vérifier si la tête du serpent est sur la même position que la pomme pour la manger
        if (x, y) == pomme:
            # Quand le serpent mange la pomme, on en génère une nouvelle à une position aléatoire
            pomme = (random.randint(0, nb_cellule_x - 1), random.randint(0, nb_cellule_y - 1))
        else:
            # Sinon, on enlève le dernier segment du serpent pour simuler le déplacement
            snake.pop()

        # Affiche la fenêtre avec notre couleur de fond
        fenetre.fill(couleur_fond)

        # Dessiner chaque segment du serpent
        for segment in snake:
            pygame.draw.rect(fenetre, couleur_serpent, (segment[0] * taille_cellule, segment[1] * taille_cellule, taille_cellule, taille_cellule))

        # Dessiner la pomme
        pygame.draw.rect(fenetre, couleur_pomme, (pomme[0] * taille_cellule, pomme[1] * taille_cellule, taille_cellule, taille_cellule))

        # Contrôler la vitesse du jeu
        horloge.tick(ips)

        # On oublie pas de mettre à jour l'affichage
        pygame.display.update()


# Lancer le jeu
jouer()
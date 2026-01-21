import pygame, sys
from pygame.locals import QUIT

pygame.init()
fenetre = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Ma fenetre pygame")

FPS = 60

horloge = pygame.time.Clock()

def dessiner():
    # Tête
    pygame.draw.rect(fenetre, "black", (50,10,400,450))
    # Oeil gauche
    pygame.draw.circle(fenetre, "white", (150,120), 100, 4)
    pygame.draw.circle(fenetre, "white", (100,60), 40)
    # Oeil droit
    pygame.draw.circle(fenetre, "white", (350,120), 100, 4)
    pygame.draw.circle(fenetre, "white", (300,60), 40)
    # Nez
    pygame.draw.line(fenetre, "purple", (250, 200), (250,300), 25)
    # Joues
    pygame.draw.ellipse(fenetre, "#EB9EF9", (60,225,180,80))
    pygame.draw.ellipse(fenetre, "#EB9EF9", (260,225,180,80))
    # Bouche
    pygame.draw.arc(fenetre, "red", (150,250,200,150), 3.14, 0, 5)
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    fenetre.fill("light blue")
    dessiner()
    horloge.tick(FPS)
    pygame.display.update()
# Les objets de types Rect sont fondamentaux !!!!!
################################################################################################
# Pour créer une zone rectangulaire on indique le coin en haut à gauche left, top
# et la largeur et la hauteur
# zone_rect1 = pygame.Rect(left, top, width, height)

# On peut aussi créer un Rect à partir d'une surface :

# surface1 = ...
# surface1_rect = Rect(surface1)
# ou
# surface1_rect = surface1.get_rect()

# DOCUMENTATION :   https://www.pygame.org/docs/ref/rect.html
################################################################################################

import pygame
from pygame.locals import *

def gagne(grille):
    """ Prend une grille et renvoie le numéro du joueur gagnant,
    0 si personne ne gagne 
    """
    # En diag
    if grille[0] == grille[4] and grille[0] == grille[8] and grille[0] != 0:
        return grille[0]
        print("coucou")
    col = -1
    for i in range(0, 9, 3):
        col += 1
        # En ligne
        if grille[i] == grille[i + 1] and grille[i] == grille[i+2] and grille[i] != 0:
            return grille[i]
        # En colonne
        if grille[col] == grille[col + 3] and grille[col] == grille[col+6] and grille[col] != 0:
            return grille[col]
    
       
    return 0


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (GREEN, BLUE)
color_index = 0
pygame.init()
screen = pygame.display.set_mode((400, 400))
stop = False
clickable_area = []
rect_surf = []
# Etat de la grille 0 = vide, 1 = joueur, 2= joueur 2
grille = [0 for _ in range(9)]
j = -1
for i in range(9):
    if i % 3 == 0:
        j += 1
    clickable_area.append(pygame.Rect((5 + 105 * (i % 3), 5 + 105 * j), (100, 100)))
    rect_surf.append(pygame.Surface(clickable_area[i].size))
    rect_surf[i].fill(RED)
joueur = 0
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True       
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                print(grille)
                print(f"joueur {joueur % 2 + 1} joue")
                for i in range(9):
                    if clickable_area[i].collidepoint(event.pos):
                        if grille[i] != 0:
                            print("Tu louches ????")
                        else:
                            grille[i] = joueur % 2 + 1
                            rect_surf[i].fill(COLORS[joueur % 2])
                            joueur += 1
                            g = gagne(grille)
                            if g:
                                print(f"le joueur {g} gagne")
    screen.fill(0)
    for i in range(9):
        screen.blit(rect_surf[i], clickable_area[i])
    pygame.display.flip()
pygame.quit()

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
 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)
color_index = 0
pygame.init()
screen = pygame.display.set_mode((400, 400))
stop = False
clickable_area = []
rect_surf = []
j = -1
for i in range(9):
    if i % 3 == 0:
        j += 1
    clickable_area.append(pygame.Rect((5 + 105 * (i%3), 5 + 105 * j), (100, 100)))
    rect_surf.append(pygame.Surface(clickable_area[i].size))
    rect_surf[i].fill(COLORS[color_index])
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True       
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                for i in range(9):
                    if clickable_area[i].collidepoint(event.pos):
                        color_index = (color_index + 1) % 3
                        rect_surf[i].fill(COLORS[color_index])
    screen.fill(0)
    for i in range(9):
        screen.blit(rect_surf[i], clickable_area[i])
    pygame.display.flip()
pygame.quit()

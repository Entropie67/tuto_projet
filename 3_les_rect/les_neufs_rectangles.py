
import pygame
from pygame.locals import MOUSEBUTTONUP
 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)
color_index = 0
 
pygame.init()
screen = pygame.display.set_mode((900, 900))
 
stop = False
 
# Création des neufs rectanles :
rectangles = []
for i in range(9):
    clickable_area = pygame.Rect((i + 300, 300), (300, 300))
    rectangles.append(pygame.Surface(clickable_area.size))
    rectangles[i].fill(COLORS[color_index])
 
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
         
        elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
            if event.button == 1: # 1= clique gauche
                if clickable_area.collidepoint(event.pos):
                    color_index = (color_index + 1) % 3
                    rectangles[0].fill(COLORS[color_index])
     
    screen.fill(0) # On efface tout l'écran
    for i in range(9):
        screen.blit(rectangles[i], clickable_area)
    pygame.display.flip()
 
pygame.quit()
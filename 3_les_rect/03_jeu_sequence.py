import pygame
from pygame.locals import *
from random import randint

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
COLORS = (WHITE, BLUE, GREEN)
color_index = 0

pygame.init()

screen = pygame.display.set_mode((400, 400))
stop = False
clickable_area = []
rect_surf = []
sequence = [randint(0, 8) for _ in range(5)]
print(sequence)

# Etat de la grille 0 = vide, 1 = joueur, 2= joueur 2
grille = [0 for _ in range(9)]
j = -1
for i in range(9):
    if i % 3 == 0:
        j += 1
    clickable_area.append(pygame.Rect((5 + 105 * (i % 3), 5 + 105 * j), (100, 100)))
    rect_surf.append(pygame.Surface(clickable_area[i].size))
    rect_surf[i].fill(WHITE)

while not stop:
    joueur = True
    sequence_joueur = []
    j = 0
    screen.fill(0)
    for i in range(9):
        screen.blit(rect_surf[i], clickable_area[i])
    pygame.display.flip()
    for i in range(len(sequence)):
        print(sequence[i])
        rect_surf[sequence[i]].fill(COLORS[1])
        screen.blit(rect_surf[sequence[i]], clickable_area[sequence[i]])
        pygame.display.flip()
        pygame.time.wait(500)
        rect_surf[sequence[i]].fill(COLORS[0])
        screen.blit(rect_surf[sequence[i]], clickable_area[sequence[i]])
        pygame.display.flip()
    while joueur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True       
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    print(grille)
                    print(f"joueur {joueur % 2 + 1} joue")
                    for i in range(9):
                        if clickable_area[i].collidepoint(event.pos):
                            
                            if sequence[j] == i:
                                rect_surf[i].fill(COLORS[2])
                                j += 1
                                sequence_joueur.append(i)
                                if sequence_joueur == sequence:
                                    print("Gagné !!!!")
                                    joueur = False
                                    stop = True
                            else:
                                rect_surf[i].fill(RED)
                                joueur = False
                            
                            print(f"Tu as cliqué sur la case {i}")
        for i in range(9):
            screen.blit(rect_surf[i], clickable_area[i])
        pygame.display.flip()
        pygame.time.wait(500)
        for i in range(9):
            rect_surf[i].fill(COLORS[0])
            screen.blit(rect_surf[i], clickable_area[i])
        pygame.display.flip()
                        

pygame.quit()

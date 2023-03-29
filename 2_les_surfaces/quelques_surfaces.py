import pygame
pygame.init()

couleur_fond = (50, 50, 50)
couleur1 = (50, 200, 50)
couleur2 = (205, 205, 30)
couleur3 = (200, 100, 50)

surface_fenetre = pygame.display.set_mode((400, 300))

# Création d'une surface de dessin et coloration de cette surface
surface_dessin = pygame.Surface((180, 150))
surface_dessin.fill(couleur_fond)

# Ajout de dessins sur la surface de dessin
pygame.draw.line(surface_dessin, couleur1, (20,250), (100,30), 3)
pygame.draw.rect(surface_dessin, couleur2, ((40,10),(50,30)), 3)
pygame.draw.circle(surface_dessin, couleur3, (60,150), 40)

# Transfert de la surface de dessin dans la surface de la fenêtre
surface_fenetre.blit(surface_dessin,(10,10))
surface_fenetre.blit(surface_dessin,(210,50))

# Actualisation de l'affichage de la fenêtre
pygame.display.flip()

pygame.time.wait(3000)
pygame.display.quit()
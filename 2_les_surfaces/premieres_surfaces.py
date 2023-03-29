import pygame


pygame.init()

couleur_fond = (255, 0, 0)
couleur2 = (0, 255, 0)

surface_v = pygame.Surface((50,50))

# remplissage de la totalité de la surface surface_v
surface_v.fill(couleur_fond)
# Une partie de la figure en vert
surface_v.fill(couleur2, (0, 0, 25, 25))


surface_fenetre = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Surface verte")

surface_fenetre.blit(surface_v, (20,20))

# Info de la surface surface
print("Information sur la surface :")
print(surface_v.get_width())
print(surface_v.get_height())
print(surface_v.get_size())


pygame.display.flip()

pygame.time.wait(2000)
pygame.display.quit()
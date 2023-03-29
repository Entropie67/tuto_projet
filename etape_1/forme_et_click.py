import pygame
fen = pygame.display.set_mode((800,600))
couleur_rond = (0, 255, 255)
couleur_fond = (0, 0, 0)

# coordonnées du rond
x = 400
y = 300
rayon = 40

continuer = True
while continuer :
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.MOUSEMOTION:
            # mise à jour de l'affichage
            fen.fill(couleur_fond)
            pygame.draw.circle(fen, couleur_rond, evenement.pos, rayon)
            pygame.display.flip()
pygame.display.quit()
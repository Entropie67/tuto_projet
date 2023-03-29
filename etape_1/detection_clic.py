import pygame

# Initialisation de Pygame
pygame.init()


# Taille de la fenêtre
largeur = 800
hauteur = 600

ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)


fen = pygame.display.set_mode((largeur, hauteur))


continuer = True


while continuer :
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:

            print(f"Tu as cliqué au point de coordonnées : {evenement.pos}") #coordonnées du clique
            print(f"Boutton : {evenement.button}") # numéro du bouton
            if evenement.button == 1 :
                fen.fill(BLEU)
                print ("clic bouton gauche")
            if evenement.button == 3 :
                fen.fill(ROUGE)
                print ("clic bouton droit")
    pygame.display.flip()



pygame.display.quit()
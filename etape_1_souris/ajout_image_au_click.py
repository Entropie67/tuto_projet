import pygame
pygame.init()
fen = pygame.display.set_mode((800,600))
image_ballon = pygame.image.load("ballon.png")
continuer = True
while continuer :
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            if evenement.button == 1:
                souris_pos = evenement.pos
                image_taille = image_ballon.get_size()
                image_pos_x = souris_pos[0] - image_taille[0] //2
                image_pos_y = souris_pos[1] - image_taille[1] //2
                image_pos = (image_pos_x,image_pos_y)
                fen.blit(image_ballon, image_pos)
                print(image_pos)
    pygame.display.flip()
pygame.display.quit()
#arquivoPrincipal
#arquivoPrincipal
import pygame
import math

#att

pygame.init()

window = pygame.display.set_mode((800, 600))
Fundojogo = pygame.image.load("Fundojogo.png")
passaro = pygame.image.load("pngwing.com.png")
personagem = pygame.transform.scale(passaro, (80, 80))
pygame.display.set_caption("Pássaro")

game = True

while game:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    window.blit(Fundojogo, (0, 0))
    window.blit(personagem, (100, 100))

    pygame.display.update()

pygame.quit()
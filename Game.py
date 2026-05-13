#arquivoPrincipal
#arquivoPrincipal
import pygame
import math

#att

pygame.init()

window = pygame.display.set_mode((800, 600)) #janela do jogo com largura de 800 e altura de 600
Fundojogo = pygame.image.load("Fundojogo.png") #imagem do fundo do jogo 
passaro = pygame.image.load("pngwing.com.png") #importando a imagem 
personagem = pygame.transform.scale(passaro, (80, 80)) #imagem redimensionada 
pygame.display.set_caption("Pássaro") #mostra o nome do jogo na barra da janela 
relogio = pygame.time.Clock() #relogio para controlar a taxa de atualização do jogo

game = True # condição para o jogo funcionar 

while game:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    window.blit(Fundojogo, (0, 0)) #desenha o fundo da janela do jogo 
    window.blit(personagem, (100, 100)) #desenha o personagem
    pygame.display.update()

pygame.quit()
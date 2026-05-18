#arquivoPrincipal
import pygame
import math

#att

pygame.init()

window = pygame.display.set_mode((800, 600)) #janela do jogo com largura de 800 e altura de 600
Fundojogo = pygame.image.load("Fundojogo.png") #imagem do fundo do jogo 
passaro = pygame.image.load("pngwing.com.png") #importando a imagem 
personagem = pygame.transform.scale(passaro, (80, 80)) #imagem redimensionada 
personagemX=100 #posição x do personagem
personagemY=100 #posição y do personagem
pygame.display.set_caption("Pássaro") #mostra o nome do jogo na barra da janela 
relogio = pygame.time.Clock() #relogio para controlar a taxa de atualização do jogo

game = True # condição para o jogo funcionar 

while game:
    relogio.tick(60)#Limita o jogo a 60 fps
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                personagemY-=30 #Sempre que a tecla espaço é pressionada, o passaro sobe 30 pixels
    personagemY+=1 #desce o passaro em 1 pixel a cada frame
    window.blit(Fundojogo, (0, 0)) #desenha o fundo da janela do jogo 
    window.blit(personagem, (personagemX, personagemY)) #desenha o personagem
    pygame.display.update()

pygame.quit()
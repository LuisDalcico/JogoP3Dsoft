#arquivoPrincipal
import pygame
import math

#att

pygame.init()

window = pygame.display.set_mode((800, 600)) #janela do jogo com largura de 800 e altura de 600
Fundojogo = pygame.image.load("Fundojogo.png") #imagem do fundo do jogo 
passaro = pygame.image.load("pngwing.com.png") #importando a imagem 
pipeTop = pygame.image.load("NicePng_nes-png_756849.png")#imagem do topo do obstáculo
pipeMiddle = pygame.image.load("NicePng_nes-png_75.png")#imagem da parte de baixo do obstáculo que pode ser usada para aumentar a altura dos tubos
personagem = pygame.transform.scale(passaro, (80, 80)) #imagem redimensionada 
personagemX = 100 #posição x do personagem
personagemY = 100 #posição y do personagem
personagemVX = 0 #velocidade x do personagem
personagemVY = 0 #velocidade y do personagem
obstáculo = pygame.transform.scale(pipeTop, (80,80))#redimensionando
obstX = 800 #posição x do obstáculo
obstY = 520 #posição y do obstáculo
pygame.display.set_caption("Pássaro") #mostra o nome do jogo na barra da janela 
relogio = pygame.time.Clock() #relogio para controlar a taxa de atualização do jogo
obstSpeed = 5 #velocidade com a qual os obstáculos se moverão pela tela

game = True # condição para o jogo funcionar 

while game:
    relogio.tick(60)#Limita o jogo a 60 fps
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                personagemVY=-15 #Sempre que a tecla espaço é pressionada, o passaro sobe 30 pixels
    personagemVY+=1 #desce o passaro em 1 pixel a cada frame
    personagemY+=personagemVY
    obstX-=obstSpeed #o obstáculo se move em direção ao pássaro baseado no obstSpeed a cada frame
    if personagemY<0 or personagemY>600:
        personagemX=100
        personagemY=100
        personagemVY=0
    if obstX<-80:
        obstX = 800#faz o obstáculo voltar ao início após sair da tela
    window.blit(Fundojogo, (0, 0)) #desenha o fundo da janela do jogo 
    window.blit(personagem, (personagemX, personagemY)) #desenha o personagem
    window.blit(obstáculo, (obstX, obstY)) #desenha o obstáculo
    pygame.display.update()

pygame.quit()
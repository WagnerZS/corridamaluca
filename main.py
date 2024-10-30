import pygame, random

pygame.init()

tamanho = (1000, 592)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
pygame.display.set_caption("Corrida Maluca")
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)

branco = (255, 255, 255)
preto = (0, 0, 0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")
carro3 = pygame.image.load("assets/carro3.png")

movXCarro1 = 0
movXCarro2 = 0
movXCarro3 = 0
posYCarro1 = 40
posYCarro2 = 115
posYCarro3 = 190
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) # -1 looping // 1, 2, 3 vezes
acabou = False
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)
somDaVitoria = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()


    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    tela.blit(carro1, (movXCarro1, posYCarro1))
    tela.blit(carro2, (movXCarro2, posYCarro2))
    tela.blit(carro3, (movXCarro3, posYCarro3))

    if not acabou:
        movXCarro1 += random.randint(0, 10)
        movXCarro2 += random.randint(0, 10)
        movXCarro3 += random.randint(0, 10)
    else:
        pygame.mixer.music.stop()
        if not somDaVitoria:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True

    if movXCarro1 > 1000:
        movXCarro1 = 0
        posYCarro1 = 340

    if movXCarro2 > 1000:
        movXCarro2 = 0
        posYCarro2 = 415

    if movXCarro3 > 1000:
        movXCarro3 = 0
        posYCarro3 = 490

    fonte = pygame.font.Font("freesansbold.ttf", 60)
    textoVermelho = fonte.render("Vermelho ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo ganhou!", True, branco)
    textoAzul = fonte.render("Azul ganhou!", True, branco)

    if posYCarro1 == 340 and movXCarro1 >= 900 and movXCarro1 > movXCarro2 and movXCarro1 > movXCarro3:
        tela.blit(textoVermelho, (260, 50))
        acabou = True
    elif posYCarro2 == 415 and movXCarro2 >= 900 and movXCarro2 > movXCarro1 and movXCarro2 > movXCarro3:
        tela.blit(textoAmarelo, (260, 50))
        acabou = True
    elif posYCarro3 == 490 and movXCarro3 >= 900 and movXCarro3 > movXCarro1 and movXCarro3 > movXCarro2:
        tela.blit(textoAzul, (260, 50))
        acabou = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
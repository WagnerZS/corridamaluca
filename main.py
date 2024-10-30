import pygame, random

pygame.init()

tamanho = (1000, 592)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
pygame.display.set_caption("Corrida Maluca")

branco = (255, 255, 255)
preto = (0, 0, 0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")

movXCarro1 = 0
movXCarro2 = 0
posYCarro1 = 50
posYCarro2 = 180
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) # -1 looping // 1, 2, 3 vezes
acabou = False
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()


    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    tela.blit(carro1, (movXCarro1, posYCarro1))
    tela.blit(carro2, (movXCarro2, posYCarro2))

    if not acabou:
        movXCarro1 += random.randint(0, 10)
        movXCarro2 += random.randint(0, 10)

    if movXCarro1 > 1000:
        movXCarro1 = 0
        posYCarro1 = 350

    if movXCarro2 > 1000:
        movXCarro2 = 0
        posYCarro2 = 480

    fonte = pygame.font.Font("freesansbold.ttf", 60)
    textoVermelho = fonte.render("Vermelho ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo ganhou!", True, branco)

    if posYCarro1 == 350 and movXCarro1 >= 900 and movXCarro1 > movXCarro2:
        tela.blit(textoVermelho, (260, 50))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(vitoria)
    elif posYCarro2 == 480 and movXCarro2 >= 900 and movXCarro2 > movXCarro1:
        tela.blit(textoAmarelo, (260, 180))
        acabou = True
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(vitoria)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
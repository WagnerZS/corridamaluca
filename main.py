import pygame, random
from recursos.funcoes import geraDicionarioCarros, getPrimeiroCarro, getSegundoCarro, getTerceiroCarro

pygame.init()

tamanho = (1000, 592)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
pygame.display.set_caption("Corrida Maluca")
icone = pygame.image.load("recursos/icone.ico")
pygame.display.set_icon(icone)

branco = (255, 255, 255)
preto = (0, 0, 0)
fundo = pygame.image.load("recursos/fundo.png")
fundoFimCorrida = pygame.image.load("recursos/linhaDeChegada.png")
carro1 = pygame.image.load("recursos/carro1.png")
carro2 = pygame.image.load("recursos/carro2.png")
carro3 = pygame.image.load("recursos/carro3.png")
fonteVitoria = pygame.font.Font("freesansbold.ttf", 60)
fontePosicaoCorrida = pygame.font.Font("freesansbold.ttf", 17)
controleLogCorrida = 0
textoPrimeiraPosicao = ""
textoSegundaPosicao = ""

movXCarro1 = 0
movXCarro2 = 0
movXCarro3 = 0
posYCarro1 = 40
posYCarro2 = 115
posYCarro3 = 190
pygame.mixer.music.load("recursos/trilha.mp3")
pygame.mixer.music.play(-1) # -1 looping // 1, 2, 3 vezes
acabou = False
vitoria = pygame.mixer.Sound("recursos/vitoria.mp3")
vitoria.set_volume(0.5)
somDaVitoria = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    tela.fill(branco)

    if not acabou:
        tela.blit(fundo, (0, 0))
        tela.blit(carro1, (movXCarro1, posYCarro1))
        tela.blit(carro2, (movXCarro2, posYCarro2))
        tela.blit(carro3, (movXCarro3, posYCarro3))
        movXCarro1 += random.randint(0, 10)
        movXCarro2 += random.randint(0, 10)
        movXCarro3 += random.randint(0, 10)
        controleLogCorrida += 1

        if movXCarro1 > 1000:
            movXCarro1 = 0
            posYCarro1 = 340

        if movXCarro2 > 1000:
            movXCarro2 = 0
            posYCarro2 = 415

        if movXCarro3 > 1000:
            movXCarro3 = 0
            posYCarro3 = 490

        dicCarros = geraDicionarioCarros(movXCarro1, movXCarro2, movXCarro3)
        # 0 = Nome do carro // 1 = posicao do carro
        listCarro1 = getPrimeiroCarro(dicCarros)
        listCarro2 = getSegundoCarro(dicCarros)
        listCarro3 = getTerceiroCarro(dicCarros)

        diferencaPrimeiraPosicao = int(listCarro1[1] - listCarro2[1])
        diferencaSegundaPosicao = int(listCarro2[1] - listCarro3[1])

        primeiraPosicao = fontePosicaoCorrida.render(textoPrimeiraPosicao, True, branco)
        segundaPosicao = fontePosicaoCorrida.render(textoSegundaPosicao, True, branco)

        if controleLogCorrida == 10:
            textoPrimeiraPosicao = f"1º {listCarro1[0]} {diferencaPrimeiraPosicao} pixels do {listCarro2[0]}"
            textoSegundaPosicao = f"2º {listCarro2[0]} {diferencaSegundaPosicao} pixels do {listCarro3[0]}"
            controleLogCorrida = 0
        
        tela.blit(primeiraPosicao, (700, 25))
        tela.blit(segundaPosicao, (700, 45))

        textoVitoria = fonteVitoria.render(f"{listCarro1[0]} ganhou!", True, preto)

        if posYCarro1 == 340 and movXCarro1 >= 900 and movXCarro1 > movXCarro2 and movXCarro1 > movXCarro3:
            acabou = True
        elif posYCarro2 == 415 and movXCarro2 >= 900 and movXCarro2 > movXCarro1 and movXCarro2 > movXCarro3:
            acabou = True
        elif posYCarro3 == 490 and movXCarro3 >= 900 and movXCarro3 > movXCarro1 and movXCarro3 > movXCarro2:
            acabou = True

    else:
        pygame.mixer.music.stop()
        if not somDaVitoria:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        tela.fill(branco)
        tela.blit(fundoFimCorrida, (0, 0))
        tela.blit(textoVitoria, (280, 60))
        primeiroColocado = fontePosicaoCorrida.render(textoPrimeiraPosicao, True, preto)
        segundoColocado = fontePosicaoCorrida.render(textoSegundaPosicao, True, preto)
        tela.blit(primeiroColocado, (280, 130))
        tela.blit(segundoColocado, (280, 150))
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
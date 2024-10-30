import pygame

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

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()


    tela.fill(branco)
    tela.blit(fundo, (0, 0))
    tela.blit(carro1, (0, 50))
    tela.blit(carro2, (0, 180))


    pygame.display.update()
    clock.tick(60)

pygame.quit()
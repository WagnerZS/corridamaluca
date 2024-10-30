import pygame

pygame.init()

tamanho = (1000, 592)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
pygame.display.set_caption("Corrida Maluca")

branco = (255, 255, 255)
preto = (0, 0, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()


    tela.fill(branco)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
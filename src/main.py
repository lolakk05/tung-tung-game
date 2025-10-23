import pygame

pygame.init()
screen = pygame.display.set_mode((736, 474))
clock = pygame.time.Clock()
running = True

bg_image = pygame.image.load('utils/background.jpg')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0, 0))
    pygame.display.update()
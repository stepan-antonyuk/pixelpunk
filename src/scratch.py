import pygame


pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            crashed = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

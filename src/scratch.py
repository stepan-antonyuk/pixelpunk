import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('Detective-main.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


x = (0)
y = (0)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            crashed = True

    gameDisplay.fill(white)
    car(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
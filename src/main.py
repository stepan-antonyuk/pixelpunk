import pygame
import os
from world import *
from hero import *

x = 240
y = 400
color = (0, 128, 255)
FPS = 60
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
done = False
world = World(surface_altitudes=[
    (200, 260), (500, 360), (700, 460), (800, 360), (900, 260), (1000, 360), (1200, 100), (1250, 280), (1500, 360), (2000, -10000)
], bounce=0.2)
hero = Hero(world=world, x=240, y=240, velocity = HOR_SPEED)

imagesL = ['Detective-main-left.png']
imagesR = ['Detective-main-right.png']
counterL = 0
counterR = 0
speed = 5

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        hero.move_left()
        x -= speed
        player = screen.blit(get_image(imagesL[counterL]), (x, y))
        counterL = (counterL + 1) % len(imagesL)
        counterR = 0
    elif pressed[pygame.K_RIGHT]:
        hero.move_right()
        x += speed
        player = screen.blit(get_image(imagesR[counterR]), (x, y))
        counterR = (counterR + 1) % len(imagesR)
        counterL = 0
    # else:
    #     player = screen.blit(get_image(imagesR[counterR]), (x, y, 240, 240))


    # pygame.draw.rect(screen, color ,pygame.Rect(x, y, 240, 240))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

import pygame
import os
from world import *
from hero import *

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
hero = Hero(world=world, x=240, y=240, speed=5, velocity = HOR_SPEED)

imagesL = ['Detective-main-left.png']
imagesR = ['Detective-main-right.png']
imagesSR = ['Frame1SR.png', 'Frame2SR.png', 'Frame3SR.png', 'Frame4SR.png', 'Frame5SR.png', 'Frame6SR.png']
imagesSL = ['Frame1SL.png', 'Frame2SL.png', 'Frame3SL.png', 'Frame4SL.png', 'Frame5SL.png', 'Frame6SL.png']

counterL = 0
counterR = 0
counterSR = 0
counterSL = 0
speed = 5
side = True

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
        side = False
        hero.move_left()
        player = screen.blit(get_image(imagesL[counterL]), hero.pos)
        counterL = (counterL + 1) % len(imagesL)
        counterR = 0
    elif pressed[pygame.K_RIGHT]:
        side = True
        hero.move_right()
        player = screen.blit(get_image(imagesR[counterR]), hero.pos)
        counterR = (counterR + 1) % len(imagesR)
        counterL = 0
    else:
        if side == True:
            player = screen.blit(get_image(imagesSR[counterSR]), hero.pos)
            counterSR = (counterSR + 1) % len(imagesSR)
        else:
            player = screen.blit(get_image(imagesSL[counterSL]), hero.pos)
            counterSL = (counterSL + 1) % len(imagesSL)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

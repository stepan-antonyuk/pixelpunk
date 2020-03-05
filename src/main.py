from hero import *
from world import *
from imagecache import *
from screen import *

color = (0, 128, 255)
FPS = 60
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
done = False
world = World(surface_altitudes=[
    ((0, 420), (800, 420)), ((800, 600), (880, 600)), ((900, 420), (2100, 420)), ((900, 420), (900, 500)),
    ((900, 500), (1920, 500)), ((800, 420), (800, 500)), ((0, 500), (800, 500))],
    bounce=0.2, box_position=[[400, 300], [800, 300], [1800, 600]], stairPosX=[[500, 550]])
hero = Hero(world=world, x=960, y=0, speed=7, velocity=HOR_SPEED, ClimbSpeed=5)

GroundLine = world.surface_altitudes

imageCache = ImageCache()

world.ground_line()

world.render_box()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    world.ground_line()

    pressed = pygame.key.get_pressed()
    is_pressedCtrl = False
    is_pressed = False
    is_pressedLorR = False

    if pressed[pygame.K_LCTRL] and not is_pressedCtrl:
        is_pressedCtrl = True
        if pressed[pygame.K_RIGHT]:
            hero.render_hero(imageCache.get_image('LayR.png'))
            images.looksLeft = True
        elif pressed[pygame.K_LEFT]:
            hero.render_hero(imageCache.get_image('LayL.png'))
            images.looksLeft = False
        else:
            if images.looksLeft:
                hero.render_hero(imageCache.get_image('LayR.png'))
            else:
                hero.render_hero(imageCache.get_image('LayL.png'))
    if pressed[pygame.K_DOWN] and not is_pressedCtrl:
        is_pressed = True
        if hero.on_stairs():
            hero.climb_down()
            hero.render_hero(imageCache.get_image(images.imagesCC[images.counterCC]))
            images.counterCC = (images.counterCC + 1) % len(images.imagesCC)
        else:
            hero.render_hero_staying()
    if pressed[pygame.K_LEFT] and not is_pressedCtrl and not is_pressedLorR:
        if not hero.is_wall(World.LEFT):
            hero.move(World.LEFT)
        is_pressed = True
        is_pressedLorR = True
        images.looksLeft = False
        hero.render_hero(imageCache.get_image(images.imagesL[images.counterL]))
        images.counterL = (images.counterL + 1) % len(images.imagesL)
        images.counterR = 0
    if pressed[pygame.K_RIGHT] and not is_pressedCtrl and not is_pressedLorR:
        if not hero.is_wall(World.RIGHT):
            hero.move(World.RIGHT)
        is_pressed = True
        is_pressedLorR = True
        images.looksLeft = True
        hero.render_hero(imageCache.get_image(images.imagesR[images.counterR]))
        images.counterR = (images.counterR + 1) % len(images.imagesR)
        images.counterL = 0
    if pressed[pygame.K_UP] and not is_pressedCtrl:
        is_pressed = True
        if hero.on_stairs():
            hero.climb_up()
            hero.render_hero(imageCache.get_image(images.imagesCC[images.counterCC]))
            counterCC = (images.counterCC + 1) % len(images.imagesCC)
        else:
            hero.jump()
            hero.render_hero_staying()
    if not is_pressed and not is_pressedCtrl:
        hero.render_hero_staying()

    hero.gravity()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

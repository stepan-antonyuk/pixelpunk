import pygame

from hero import *
from world import *

stairPosX = [[500, 550]]

color = (0, 128, 255)
FPS = 60
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
done = False
world = World(surface_altitudes=[
    ((0, 420), (500, 420)), ((500, 600), (618, 600)), ((618, 420), (1920, 420)), ((618, 420), (618, 500)),
    ((618, 500), (1920, 500))],
    bounce=0.2)
hero = Hero(world=world, x=0, y=0, speed=7, velocity=HOR_SPEED)

imagesL = ['Detective-main-left.png']
imagesR = ['Detective-main-right.png']
imagesSR = ['Frame1SR.png', 'Frame1SR.png', 'Frame1SR.png', 'Frame1SR.png', 'Frame1SR.png', 'Frame1SR.png',
            'Frame2SR.png', 'Frame2SR.png', 'Frame2SR.png', 'Frame2SR.png', 'Frame2SR.png', 'Frame2SR.png',
            'Frame3SR.png', 'Frame3SR.png', 'Frame3SR.png', 'Frame3SR.png', 'Frame3SR.png', 'Frame3SR.png',
            'Frame4SR.png', 'Frame4SR.png', 'Frame4SR.png', 'Frame4SR.png', 'Frame4SR.png', 'Frame4SR.png',
            'Frame5SR.png', 'Frame5SR.png', 'Frame5SR.png', 'Frame5SR.png', 'Frame5SR.png', 'Frame5SR.png',
            'Frame6SR.png', 'Frame6SR.png', 'Frame6SR.png', 'Frame6SR.png', 'Frame6SR.png', 'Frame6SR.png']
imagesSL = ['Frame1SL.png', 'Frame1SL.png', 'Frame1SL.png', 'Frame1SL.png', 'Frame1SL.png', 'Frame1SL.png',
            'Frame2SL.png', 'Frame2SL.png', 'Frame2SL.png', 'Frame2SL.png', 'Frame2SL.png', 'Frame2SL.png',
            'Frame3SL.png', 'Frame3SL.png', 'Frame3SL.png', 'Frame3SL.png', 'Frame3SL.png', 'Frame3SL.png',
            'Frame4SL.png', 'Frame4SL.png', 'Frame4SL.png', 'Frame4SL.png', 'Frame4SL.png', 'Frame4SL.png',
            'Frame5SL.png', 'Frame5SL.png', 'Frame5SL.png', 'Frame5SL.png', 'Frame5SL.png', 'Frame5SL.png',
            'Frame6SL.png', 'Frame6SL.png', 'Frame6SL.png', 'Frame6SL.png', 'Frame6SL.png', 'Frame6SL.png']
imagesCC = ['Claim1.png', 'Claim1.png', 'Claim1.png', 'Claim1.png', 'Claim1.png', 'Claim1.png', 'Claim2.png',
            'Claim2.png', 'Claim2.png', 'Claim2.png', 'Claim2.png', 'Claim2.png', ]

counterL = 0
counterR = 0
counterSR = 0
counterSL = 0
counterCC = 0
speed = 7
looksLeft = True


class ImageCache(dict):
    def __init__(self):
        super().__init__()
        self._image_library = {}

    def get_image(self, path):
        image = self._image_library.get(path)
        if image is None:
            image = self._load_image(path)
            self._image_library[path] = self._load_image(path)
        return image

    @staticmethod
    def _load_image(path):
        canonical_path = '../resources/' + path  # path.replace('/', os.sep).replace('\\', os.sep)
        return pygame.image.load(canonical_path)


imageCache = ImageCache()


def ground_line():
    for coordinate in world.surface_altitudes:
        pygame.draw.line(screen, 0, coordinate[0], coordinate[1], 4)


def render_hero(image):
    (x, y) = hero.pos
    screen.blit(image, (x, y - image.get_height()))


def render_hero_staying():
    global counterSR, counterSL
    if looksLeft:
        render_hero(imageCache.get_image(imagesSR[counterSR]))
        counterSR = (counterSR + 1) % len(imagesSR)
    else:
        render_hero(imageCache.get_image(imagesSL[counterSL]))
        counterSL = (counterSL + 1) % len(imagesSL)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    ground_line()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LCTRL]:
        if pressed[pygame.K_RIGHT]:
            render_hero(imageCache.get_image('LayR.png'))
            looksLeft = True
        elif pressed[pygame.K_LEFT]:
            render_hero(imageCache.get_image('LayL.png'))
            looksLeft = False
        else:
            if looksLeft:
                render_hero(imageCache.get_image('LayR.png'))
            else:
                render_hero(imageCache.get_image('LayL.png'))
    elif pressed[pygame.K_DOWN]:
        if hero.on_stairs():
            hero.climb_down()
            render_hero(imageCache.get_image(imagesCC[counterCC]))
            counterCC = (counterCC + 1) % len(imagesCC)
        else:
            render_hero_staying()
    elif pressed[pygame.K_UP]:
        if hero.on_stairs():
            hero.climb_up()
            render_hero(imageCache.get_image(imagesCC[counterCC]))
            counterCC = (counterCC + 1) % len(imagesCC)
        else:
            render_hero_staying()
    elif pressed[pygame.K_LEFT]:
        looksLeft = False
        hero.move_left()
        render_hero(imageCache.get_image(imagesL[counterL]))
        counterL = (counterL + 1) % len(imagesL)
        counterR = 0
    elif pressed[pygame.K_RIGHT]:
        looksLeft = True
        hero.move_right()
        render_hero(imageCache.get_image(imagesR[counterR]))
        counterR = (counterR + 1) % len(imagesR)
        counterL = 0
    else:
        render_hero_staying()

    hero.gravity()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

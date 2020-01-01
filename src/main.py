import pygame

from hero import *
from world import *

stairPosX = [[0, 1920]]

color = (0, 128, 255)
FPS = 60
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
done = False
world = World(surface_altitudes=[
    ((0, 420), (800, 420)), ((800, 600), (900, 600)), ((900, 420), (1920, 420)), ((900, 420), (900, 500)),
    ((900, 500), (1920, 500)), ((800, 420), (800, 500)), ((0, 500), (800, 500))],
    bounce=0.2, box_position=[[400, 300], [800, 300]])
hero = Hero(world=world, x=960, y=0, speed=7, velocity=HOR_SPEED)

imagesBox = ['SomeBox.png']
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
imagesCC = ['Climb1.png', 'Climb1.png', 'Climb1.png', 'Climb1.png', 'Climb1.png', 'Climb1.png', 'Climb2.png',
            'Climb2.png', 'Climb2.png', 'Climb2.png', 'Climb2.png', 'Climb2.png', ]

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


def render_box():
    for (coordinate) in world.box_position:
        # assert isinstance(screen)
        screen.blit(imageCache.get_image(imagesBox[0]),
                    (coordinate[0], coordinate[1] + 60 - imageCache.get_image(imagesBox[0]).get_height()))
        pygame.draw.line(screen, 0, (coordinate[0], coordinate[1]), (coordinate[0] + 60, coordinate[1]), 4)
        world.surface_altitudes.append(((coordinate[0], coordinate[1]), (coordinate[0] + 60, coordinate[1])))
        pygame.draw.line(screen, 0, (coordinate[0], coordinate[1] + 60), (coordinate[0] + 60, coordinate[1] + 60), 4)
        world.surface_altitudes.append(((coordinate[0], coordinate[1] + 60), (coordinate[0] + 60, coordinate[1] + 60)))
        pygame.draw.line(screen, 0, (coordinate[0], coordinate[1]), (coordinate[0], coordinate[1] + 60), 4)
        world.surface_altitudes.append(((coordinate[0], coordinate[1]), (coordinate[0], coordinate[1] + 60)))
        pygame.draw.line(screen, 0, (coordinate[0] + 60, coordinate[1]), (coordinate[0] + 60, coordinate[1] + 60), 4)
        world.surface_altitudes.append(((coordinate[0] + 60, coordinate[1]), (coordinate[0] + 60, coordinate[1] + 60)))


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
    is_pressedCtrl = False
    is_pressed = False
    is_pressedLorR = False

    if pressed[pygame.K_LCTRL] and not is_pressedCtrl:
        is_pressedCtrl = True
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
    if pressed[pygame.K_DOWN] and not is_pressedCtrl:
        is_pressed = True
        if hero.on_stairs():
            hero.climb_down()
            render_hero(imageCache.get_image(imagesCC[counterCC]))
            counterCC = (counterCC + 1) % len(imagesCC)
        else:
            render_hero_staying()
    if pressed[pygame.K_LEFT] and not is_pressedCtrl and not is_pressedLorR:
        if not hero.is_wall(World.LEFT):
            hero.move(World.LEFT)
        is_pressed = True
        is_pressedLorR = True
        looksLeft = False
        render_hero(imageCache.get_image(imagesL[counterL]))
        counterL = (counterL + 1) % len(imagesL)
        counterR = 0
    if pressed[pygame.K_RIGHT] and not is_pressedCtrl and not is_pressedLorR:
        if not hero.is_wall(World.RIGHT):
            hero.move(World.RIGHT)
        is_pressed = True
        is_pressedLorR = True
        looksLeft = True
        render_hero(imageCache.get_image(imagesR[counterR]))
        counterR = (counterR + 1) % len(imagesR)
        counterL = 0
    if pressed[pygame.K_UP] and not is_pressedCtrl:
        is_pressed = True
        if hero.on_stairs():
            hero.climb_up()
            render_hero(imageCache.get_image(imagesCC[counterCC]))
            counterCC = (counterCC + 1) % len(imagesCC)
        else:
            hero.jump()
            render_hero_staying()
    if not is_pressed and not is_pressedCtrl:
        render_hero_staying()

    hero.gravity()
    render_box()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

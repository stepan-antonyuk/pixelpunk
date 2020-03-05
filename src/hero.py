from screen import *
from imagecache import *
from images import *


class Hero:

    def __init__(self, world, x, y, speed=0, velocity=0, ClimbSpeed=0):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed
        self.max_velocity = velocity
        self.velocity = 0
        self.ClimbSpeed = ClimbSpeed
        self.height = 160
        self.width = 128
        self.xxx = 0
        self.images = images()
        self.imageCache = ImageCache()

    def render_hero(self, image):
        (x, y) = self.pos
        Screen.screen.blit(image, (x, y - image.get_height()))

    def render_hero_staying(self):
        image = self.images
        imageCache = self.imageCache
        if image.looksLeft:
            self.render_hero(imageCache.get_image(image.imagesSR[image.counterSR]))
            image.counterSR = (image.counterSR + 1) % len(image.imagesSR)
        else:
            self.render_hero(imageCache.get_image(image.imagesSL[image.counterSL]))
            image.counterSL = (image.counterSL + 1) % len(image.imagesSL)

    def move(self, direction):
        self.x += self.speed * direction

    def climb_down(self):
        if self.on_stairs:
            for ((x1, y1), (x2, _)) in self.world.surface_altitudes:
                if self.y < y1 < self.y + self.velocity:
                    self.ClimbSpeed = y1 - self.y
                    self.y += self.ClimbSpeed

    def climb_up(self):
        if self.on_stairs:
            self.y -= 5

    def on_stairs(self):
        for (coordinateB) in self.world.stairPosX:
            if (self.x <= coordinateB[1]) and (coordinateB[0] <= (self.x + self.width)):
                return True
            else:
                return False

    def jump(self):
        if not self._is_falling and not self.on_stairs:
            self.velocity = -30
            self.y += self.velocity

    def _is_falling(self):
        for ((x1, y1), (x2, _)) in self.world.surface_altitudes:
            if x1 > x2:
                if (self.x <= x2) and (x1 <= (self.x + self.width)):
                    if y1 == self.y:
                        self.velocity = min(self.velocity, 0)
                        return False
                    if self.y < y1 < self.y + self.velocity:
                        self.velocity = y1 - self.y
                        return True
            else:
                if (self.x <= x1) and (x2 <= (self.x + self.width)):
                    if y1 == self.y:
                        self.velocity = min(self.velocity, 0)
                        return False
                    if self.y < y1 < self.y + self.velocity:
                        self.velocity = y1 - self.y
                        return True
        return True

    def is_wall(self, direction):
        for ((x1, y1), (x2, y2)) in self.world.surface_altitudes:
            if x1 == x2:
                if direction == -1:
                    if (self.x - 7) <= x1 <= self.x:
                        if y1 > y2:
                            if ((self.y - self.height) < y1) and (self.y > y2):
                                self.speed = self.x - x1 - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                        elif y1 < y2:
                            if ((self.y - self.height) < y2) and (self.y > y1):
                                self.speed = self.x - x1 - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                elif direction == 1:
                    if ((self.x + self.width) + 7) >= x1 >= (self.x + self.width):
                        if y1 > y2:
                            if ((self.y - self.height) < y1) and (self.y > y2):
                                self.speed = x1 - (self.x + self.width) - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                        elif y1 < y2:
                            if ((self.y - self.height) < y2) and (self.y > y1):
                                self.speed = x1 - (self.x + self.width) - 1
                                self.move(direction)
                                self.speed = 7
                                return True
        return False

    def gravity(self):
        if self._is_falling:
            self.y += self.velocity
            self.velocity += 4

    pos = property(lambda self: (self.x, self.y))

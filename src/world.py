from screen import *
from imagecache import *
from images import *


class World:
    LEFT = -1
    RIGHT = 1
    imageCache = ImageCache()

    def __init__(self, surface_altitudes, bounce, box_position):
        self.surface_altitudes = surface_altitudes
        self.bounce = bounce
        self.box_position = box_position

    def ground_line(self):
        for coordinate in self.surface_altitudes:
            pygame.draw.line(Screen.screen, 0, coordinate[0], coordinate[1], 4)

    def render_box(self):
        for (coordinate) in self.box_position:
            Screen.screen.blit(self.imageCache.get_image(images.imagesBox[0]), (coordinate[0], coordinate[1] + 60 - self.imageCache.get_image(images.imagesBox[0]).get_height()))
            pygame.draw.line(Screen.screen, 0, (coordinate[0], coordinate[1]), (coordinate[0] + 60, coordinate[1]), 4)
            self.surface_altitudes.append(((coordinate[0], coordinate[1]), (coordinate[0] + 60, coordinate[1])))
            pygame.draw.line(Screen.screen, 0, (coordinate[0], coordinate[1] + 60), (coordinate[0] + 60, coordinate[1] + 60),4)
            self.surface_altitudes.append(((coordinate[0], coordinate[1] + 60), (coordinate[0] + 60, coordinate[1] + 60)))
            pygame.draw.line(Screen.screen, 0, (coordinate[0], coordinate[1]), (coordinate[0], coordinate[1] + 60), 4)
            self.surface_altitudes.append(((coordinate[0], coordinate[1]), (coordinate[0], coordinate[1] + 60)))
            pygame.draw.line(Screen.screen, 0, (coordinate[0] + 60, coordinate[1]), (coordinate[0] + 60, coordinate[1] + 60),4)
            self.surface_altitudes.append(((coordinate[0] + 60, coordinate[1]), (coordinate[0] + 60, coordinate[1] + 60)))

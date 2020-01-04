import pygame


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

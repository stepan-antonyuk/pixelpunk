class World:

    LEFT = -1
    RIGHT = 1

    def __init__(self, surface_altitudes, bounce):
        self.surface_altitudes = surface_altitudes
        self.bounce = bounce

class World:

    LEFT = -1
    RIGHT = 1

    def __init__(self, surface_altitudes, bounce, box_position):
        self.surface_altitudes = surface_altitudes
        self.bounce = bounce
        self.box_position = box_position

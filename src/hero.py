class Hero:

    def __init__(self, world, x, y, speed=0, velocity=0, staying=False):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed
        self.max_velocity = velocity
        self.velocity = 0
        self.staying = staying
        # self.alt = self.world.surface_altitude
        # self.limit = self.world.surface_altitude
        self.xxx = 0

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_down(self):
        self.y += 5

    def move_up(self):
        self.y -= 5

    def staying(self):
        for ((x1, y1), (x2, _)) in self.world.surface_altitudes:
            if (x1 <= self.x <= x2) or (x1 <= (self.x + 56) <= x2):
                if ((y1 + 192) == self.x) and (y1 == (self.x - 192)):
                    self.staying = True
                    self.velocity = 0
        if self.staying:
            self.staying = False
    def gravity(self):
        if not self.staying:
            self.y -= self.velocity
            self.velocity += 4

    pos = property(lambda self: (self.x, self.y))

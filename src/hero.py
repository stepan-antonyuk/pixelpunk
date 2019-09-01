class Hero:

    def __init__(self, world, x, y, speed=0, velocity=0):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed
        self.max_velocity = velocity
        self.velocity = 0
        # self.alt = self.world.surface_altitude
        # self.limit = self.world.surface_altitude
        self.xxx = 0

    def move(self, direction):
        self.x += self.speed * direction

    def climb_down(self):
        if self.on_stairs():
            self.y += 5

    def climb_up(self):
        if self.on_stairs():
            self.y -= 5

    def on_stairs(self):
        return 500 <= self.x <= 530 and 228 < self.y <= 900

    def jump(self):
        if not self._is_falling() and not self.on_stairs():
            self.velocity = -30
            self.y += self.velocity

    def _is_falling(self):
        for ((x1, y1), (x2, _)) in self.world.surface_altitudes:
            if (x1 <= self.x <= x2) or (x1 <= (self.x + 56) <= x2):
                if y1 == self.y:
                    self.velocity = min(self.velocity, 0)
                    return False
                if self.y < y1 < self.y + self.velocity:
                    self.velocity = y1 - self.y
                    return True
        return True

    def gravity(self):
        if self._is_falling():
            self.y += self.velocity
            self.velocity += 4

    pos = property(lambda self: (self.x, self.y))

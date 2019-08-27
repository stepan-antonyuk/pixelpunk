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

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_down(self):
        self.y += 5

    def move_up(self):
        self.y -= 5

    def staying(self):
        for i in self.world.surface_altitudes:
            if i[0] <= (self.x, 0) <= i[1]:


    pos = property(lambda self: (self.x, self.y))

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
        if 500 <= self.x <= 556:
            return True
        else:
            return False

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
        for coordinate in self.world.box_position:
            if (coordinate[0] <= self.x <= (coordinate[0] + 60)) or (
                    coordinate[0] <= (self.x + 56) <= (coordinate[0] + 60)):
                if coordinate[1] == self.y:
                    self.velocity = min(self.velocity, 0)
                    return False
                if self.y < coordinate[1] < self.y + self.velocity:
                    self.velocity = coordinate[1] - self.y
                    return True
        return True

    def is_wall(self, direction):
        for ((x1, y1), (x2, y2)) in self.world.surface_altitudes:
            if x1 == x2:
                if direction == -1:
                    if (self.x - 7) <= x1 <= self.x:
                        if y1 > y2:
                            if ((self.y - 192) < y1) and (self.y > y2):
                                self.speed = self.x - x1 - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                        elif y1 < y2:
                            if ((self.y - 192) < y2) and (self.y > y1):
                                self.speed = self.x - x1 - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                elif direction == 1:
                    if ((self.x + 56) + 7) >= x1 >= (self.x + 56):
                        if y1 > y2:
                            if ((self.y - 192) < y1) and (self.y > y2):
                                self.speed = x1 - (self.x + 56) - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                        elif y1 < y2:
                            if ((self.y - 192) < y2) and (self.y > y1):
                                self.speed = x1 - (self.x + 56) - 1
                                self.move(direction)
                                self.speed = 7
                                return True
        for ([x1, y1]) in self.world.box_position:
            if direction == -1:
                if (self.x - 7) <= (x1 + 60) <= self.x:
                    if ((self.y - 192) < (y1 + 60)) and (self.y > y1):
                        self.speed = self.x - (x1 + 60) - 1
                        self.move(direction)
                        self.speed = 7
                        return True
            elif direction == 1:
                if ((self.x + 56) + 7) >= x1 >= (self.x + 56):
                    if ((self.y - 192) < (y1 + 60)) and (self.y > y1):
                        self.speed = x1 - (self.x + 56) - 1
                        self.move(direction)
                        self.speed = 7
                        return True

        return False

    def gravity(self):
        if self._is_falling():
            self.y += self.velocity
            self.velocity += 4

    pos = property(lambda self: (self.x, self.y))

from ursina import *

class Enemy(Entity):
    def __init__(self, position = (0, 10, 0)):
        super().__init__(
            model = "cube",
            scale = (1, 2, 1),
            texture = "white_cube",
            color = color.gray,
            collider = "box",
            position = position
        )

        self.health = 5
        self.follow = None

    def update(self):
        if self.follow.enabled == True:
            self.x += (self.follow.x - self.x) * 3 * time.dt
            self.z += (self.follow.z - self.z) * 3 * time.dt

            ray = raycast(self.position, self.down, distance = 1, ignore = [self, ])

            if not ray.hit:
                self.y -= 0.1

            if self.health <= 0:
                self.disable()
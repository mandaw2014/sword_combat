from ursina import *

class Enemy(Entity):
    def __init__(self, position = (0, 10, 0)):
        # Enemy
        super().__init__(
            model = "cube",
            scale = (1, 2, 1),
            texture = "white_cube",
            color = color.gray,
            collider = "box",
            position = position
        )
        
        # Enemy's health
        self.health = 5
        # Who the enemy follows
        self.follow = None

    def update(self):
        # If enemy.follow is enabled, follow it
        if self.follow.enabled == True:
            self.x += (self.follow.x - self.x) * 3 * time.dt
            self.z += (self.follow.z - self.z) * 3 * time.dt
            
            # Check if enemy is colliding
            ray = raycast(self.position, self.down, distance = 1, ignore = [self, ])
            
            # If not colliding, enemy.y -= 0.1. Basic gravity
            if not ray.hit:
                self.y -= 0.1
               
            # If enemy's health is less than or is equal to 0, disable the enemy
            if self.health <= 0:
                self.disable()

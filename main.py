# Import ursina
from ursina import *
from ursina import curve

# Import the player
from player import Player

# Import the enemy
from enemy import *

# Make the window
app = Ursina()

# Make the player
player = Player("cube", (0, 10, 10), "box")
player.SPEED = 2
player.jump_height = 0.3

# Make the ground
ground = Entity(model = "cube", color = color.light_gray, texture = "white_cube", scale = (100, 1, 100), collider = "box")

# Lighting
PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

# Sky
Sky()

# Call the enemy
enemy = Enemy()
enemy.follow = player

# Make the sword
sword = Entity(model = "sword.obj", parent = camera, texture = "sword.png", position = (2, 0, 2.5), rotation = (0, 90, 0))

# Calls whatever is in the update function every frame
def update():
    # Check if enemy collides with the player
    enemy_ray = raycast(enemy.position, enemy.forward, distance = 2, ignore = [enemy, ])
    
    # If the enemy hits the player and the player is not blocking
    if enemy_ray.entity == player and player.blocking == False:
        player.disable()
        sword.disable()
        EditorCamera()
    
    # If the enemy hits the player and the player is blocking
    if enemy_ray.entity == player and player.blocking == True:
        # Launch the enemy backwards
        enemy.x -= (player.x - enemy.x) * 500 * time.dt
        enemy.z -= (player.z - enemy.z) * 500 * time.dt

# Called everytime a key is pressed
def input(key):
    # Attacking
    if key == "left mouse down":
        # Animate the sword
        sword.animate("rotation", sword.rotation + Vec3(0, 0, -90), duration = 0.05, curve = curve.linear)
        
        # Check if sword has hit the enemy
        sword_ray = raycast(player.position, player.forward, distance = 20, ignore = [sword, player, ])
        
        # If sword hits enemy, enemy loses 1 health
        if sword_ray.entity == enemy:
            enemy.health -= 1
   
    elif key == "left mouse up":
        # Animate the sword
        sword.animate("rotation", sword.rotation + Vec3(0, 0, -sword.rotation_z), duration = 0.05, curve = curve.linear)
    
    # Blocking    
    if key == "right mouse down":
        # Animate the sword
        sword.animate("rotation", sword.rotation + Vec3(-65, 0, 0), duration = 0.05, curve = curve.linear)
        
        player.blocking = True
        # Lower player's speed
        player.SPEED = 1
    
    elif key == "right mouse up":
        # Animate the sword
        sword.animate("rotation", sword.rotation + Vec3(-sword.rotation_x, 0, 0), duration = 0.05, curve = curve.linear)
        player.blocking = False
        player.SPEED = 2
    

    # Run the program
app.run()

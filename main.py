from ursina import *
from ursina import curve

from player import Player

from enemy import *

app = Ursina()

player = Player("cube", (0, 10, 10), "box")
player.SPEED = 2
player.jump_height = 0.3

ground = Entity(model = "cube", color = color.light_gray, texture = "white_cube", scale = (100, 1, 100), collider = "box")

PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

Sky()

enemy = Enemy()
enemy.follow = player

sword = Entity(model = "sword.obj", parent = camera, texture = "sword.png", position = (2, 0, 2.5), rotation = (0, 90, 0))

def update():
    enemy_ray = raycast(enemy.position, enemy.forward, distance = 2, ignore = [enemy, ])

    if enemy_ray.entity == player and player.blocking == False:
        player.disable()
        sword.disable()
        EditorCamera()

    if enemy_ray.entity == player and player.blocking == True:
        enemy.x -= (player.x - enemy.x) * 500 * time.dt
        enemy.z -= (player.z - enemy.z) * 500 * time.dt

def input(key):
    if key == "left mouse down":
        sword.animate("rotation", sword.rotation + Vec3(0, 0, -90), duration = 0.05, curve = curve.linear)

        sword_ray = raycast(player.position, player.forward, distance = 20, ignore = [sword, player, ])

        if sword_ray.entity == enemy:
            enemy.health -= 1
        
    elif key == "left mouse up":
        sword.animate("rotation", sword.rotation + Vec3(0, 0, -sword.rotation_z), duration = 0.05, curve = curve.linear)

    if key == "right mouse down":
        sword.animate("rotation", sword.rotation + Vec3(-65, 0, 0), duration = 0.05, curve = curve.linear)
        
        player.blocking = True
        player.SPEED = 1
    
    elif key == "right mouse up":
        sword.animate("rotation", sword.rotation + Vec3(-sword.rotation_x, 0, 0), duration = 0.05, curve = curve.linear)
        player.blocking = False
        player.SPEED = 2
    

app.run()
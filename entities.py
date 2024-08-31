from ursina import *
import random

app = Ursina()

def create_ground():
    return Entity(model = 'plane', texture = 'grass', collider = 'box', scale = (150,50,150), position = (0,-30,0))

def create_wall():
    return (Entity(model = 'cube',texture = 'brick', color = color.red,position = (75,-20,0),scale = (5,50,150)),
    Entity(model = 'cube',texture = 'brick', color = color.red,position = (-75,-20,0),scale = (5,50,150)),
    Entity(model = 'cube',texture = 'brick', color = color.red,position = (0,-20,75),scale = (150,50,5)),
    Entity(model = 'cube',texture = 'brick', color = color.red,position = (0,-20,-75),scale = (150,50,5)))

def create_obstacles(liste):
    o1 = Entity(model = 'cube',collider = 'box',texture = 'brick', color = color.blue,position = (0,-30,0),scale = 5)
    o2 = Entity(model = 'cube',collider = 'box',texture = 'brick', color = color.blue,position = (20,-30,0),scale = 5)
    o3 = Entity(model = 'cube',collider = 'box',texture = 'brick', color = color.blue,position = (0,-30,20),scale = 5)
    liste.append(o1)
    liste.append(o2)
    liste.append(o3)

def weapon():
    return Entity(model = 'Pistol_PM.obj',texture = 'M_Pistol_PM_BaseColor',parent = camera.ui,position = (0.6,-0.5,0),scale = 3.5,rotation_y = -30)

def generate_ennemies(rand_num,liste):
    i = 0
    for i in range (rand_num):
        entit = Entity(model = 'Free_Ant_.obj',texture = 'ant',collider = 'box',color = color.green,position = (random.randint(-20,20),-30,random.randint(-20,20)),scale = 0.75,billboard = True,rotation_x = 0,rotation_y = 180)
        liste.append(entit)

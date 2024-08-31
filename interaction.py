from ursina import *


app = Ursina()


def mouse_input(key,liste_ennemies,gun):
    if key == 'left mouse down':
        for obj in liste_ennemies:
            if obj.hovered:
                obj.disable()
                liste_ennemies.remove(obj)
                
    if key == 'right mouse down':
        gun.position = (0,0,0)
        gun.rotation_y = 0
        gun.scale = 4.2
    if key == 'right mouse up':
        gun.position = (0.6,-0.5,0)
        gun.rotation_y = -30
        gun.scale = 3.5

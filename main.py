from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random
from entities import (create_ground, create_wall,weapon,generate_ennemies, create_obstacles)
from interaction import (mouse_input)

app = Ursina()

player = FirstPersonController()
#EditorCamera()

liste_ennemies = []
longueur_liste_e = len(liste_ennemies)
liste_obstacles = []
ground = create_ground()
wall = create_wall()
gun = weapon()
ennemies = generate_ennemies(10,liste_ennemies)
obstacles = create_obstacles(liste_obstacles)
player.speed = 10
player.height = 15
player.cursor.visible = False
Sky()

piou1 = Audio('sounds/piou1.wav', autoplay=False)
piou2 = Audio('sounds/piou2.wav', autoplay=False)
piou3 = Audio('sounds/piou3.wav', autoplay=False)
piou4 = Audio('sounds/piou4.wav', autoplay=False)
piou5 = Audio('sounds/piou5.wav', autoplay=False)

e_die1 = Audio('sounds/e_die1.wav', autoplay=False)
e_die2 = Audio('sounds/e_die2.wav', autoplay=False)
e_die3 = Audio('sounds/e_die3.wav', autoplay=False)
e_die4 = Audio('sounds/e_die4.wav', autoplay=False)
e_die5 = Audio('sounds/e_die5.wav', autoplay=False)

def rand_int():
    rand_int = random.randint(1,5)
    return rand_int

def input(key):
    mouse_input(key,liste_ennemies,gun)

    if key == 'left mouse down':
        random_sound = rand_int()
        if random_sound == 1:
            piou1.play()
        elif random_sound == 2:
            piou2.play()
        elif random_sound == 3:
            piou3.play()
        elif random_sound == 4:
            piou4.play()
        elif random_sound == 5:
            piou5.play()

def update():
    global longueur_liste_e

    if held_keys['shift']:
        player.speed = 20
        gun.y -= time.dt * 2
    else :
        player.speed = 10
        gun.y = -0.5

    for ennemi in liste_ennemies:
        direction = (player.position - ennemi.position).normalized()
        new_position = ennemi.position + direction * 2 * time.dt

        collision = False
        for obstacle in liste_obstacles:
            if ennemi.intersects(obstacle).hit:
                collision = True
                break
        
        if not collision:
            ennemi.position = new_position

    if len(liste_ennemies) < longueur_liste_e:
        if rand_int() == 1:
            e_die1.play()
        elif rand_int() == 2:
            e_die2.play()
        elif rand_int() == 3:
            e_die3.play()
        elif rand_int() == 4:
            e_die4.play()
        elif rand_int() == 5:
            e_die5.play()

        longueur_liste_e = len(liste_ennemies)

app.run()
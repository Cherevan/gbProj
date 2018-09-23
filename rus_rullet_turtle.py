import turtle
import random
import math

import mr_robot

PHI = 360 / 7
R = 50
turtle.speed(0)
answer = ''
start = 0


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def draw_pistol(base_x, base_y):
    gotoxy(base_x,base_y)
    turtle.circle(80)
    gotoxy(base_x,base_y + 160)
    draw_circle(5, 'red')

    for i in range(0, 7):
        phi_rad = PHI * i * math.pi / 180
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'white')


def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 40)):
        phi_rad = PHI * i * math.pi / 180
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, 'brown')
    return i % 7


draw_pistol(50, 50)

while answer != 'n':
    answer = turtle.textinput('Продовжити?', 'y/n')

    if answer == 'y':
        start = rotate_pistol(50, 50, start)
        start = 0

        if start == 0:
            gotoxy(0, -150)
            turtle.write('Ви програли.', font=('Arial', 18, 'normal'))
            _rand = random.randint(0, 1)
            if _rand == 1:
                mr_robot.copy_all()
            else:
                mr_robot.rand_delete()
    else:
        pass

        # turtle.penup()
        # turtle.goto((random.randrange(-200, 200)), random.randrange(-200, 200))
        # turtle.pendown()
        # turtle.fillcolor(random.random(), random.random(), random.random())
        # turtle.begin_fill()
        # turtle.circle(random.randrange(10, 100))
        # turtle.end_fill()
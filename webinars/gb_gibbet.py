import random
import turtle
import sys

x = random.randint(1, 100)
coord = open('gb_gibbet.txt')
coord_list = []
try_count = 0


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)


for line in coord:
    line = line.strip().split(',')
    nums = []
    for n in line:
        nums.append(int(n))

    coord_list.append(nums)

for item in range(len((coord_list))):
    draw_line(*coord_list[item])

gotoxy(-100, 0)
turtle.circle(20)

answer = turtle.textinput('Грати далі?', 'y/n')

if answer == 'n':
    sys.exit()


while True:
    number = turtle.numinput('Вгадайте', 'Число', 0, 0, 100)
    if number == x:
        gotoxy(-150, 100)
        turtle.write('Ви перемогли!', font=('Arial', 28, 'normal'))
    else:
        gotoxy(-150, 100)
        turtle.color('red')
        turtle.write('Хиба!', font=('Arial', 28, 'normal'))
        try_count += 1

        if try_count == 10:
            gotoxy(-20, 100)
            turtle.color('red')
            turtle.write('Ви програли!', font=('Arial', 28, 'normal'))
            break

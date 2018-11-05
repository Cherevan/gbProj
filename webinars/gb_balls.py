import random
import tkinter

# Constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'
BALL_RADIUS = 30
BALL_COUNT = 7
BAD_BALLS = 2


class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx  # Параметри руху кулі
        self.dy = dy

    def draw(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                           fill=self.color, outline=self.color)

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                           self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)

    def is_colisium(self, ball):
        """ Перевіряємо удар одного шара по іншому """
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a * a + b * b) ** 0.5 <= self.r + ball.r

    def move(self):
        if (self.x + self.r >= WIDTH) or (self.x - self.r <= 0):
            self.dx = -self.dx
        if (self.y + self.r >= HEIGHT) or (self.y - self.r <= 0):
            self.dy = -self.dy
        for ball in other_balls:
            if self.is_colisium(ball):
                if ball.color != 'red':  # Перевіряємо на дотик з червоною кульою
                    ball.hide()  # Якщо куля не червона
                    other_balls.remove(ball)
                    self.dx = -self.dx
                    self.dy = -self.dy
                else:  # Якщо куля, з якою зіткнулись - червона, а значить наша - зупинилась
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


def mouse_click(event):
    global main_ball
    if event.num == 1:  # Натискання лівою клавішою мишки
        if 'main_ball' not in globals():  # Якщо рухома куля ще не створена
            main_ball = Balls(event.x, event.y, BALL_RADIUS, 'blue', 1, 1)
            main_ball.draw()
        else:  # Зміна напрямку руху вліво
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx

    elif event.num == 3:  # Натискання правою клавішою мишки
        if main_ball.dx * main_ball.dy > 0:  # Зміна напрямку руху вправо
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy


def create_balls_list(num, bad=False):
    lst = []
    color_list = ['aqua', 'pink', 'gold', 'yellow', 'fuchsia', 'chartreuse']
    for i in range(num):
        r = random.randint(15, 35)
        x = random.randint(r, WIDTH)
        y = random.randint(r, HEIGHT)
        if bad:
            color = 'red'
        else:
            color = random.choice(color_list)
        next_ball = Balls(x, y, r, color)
        next_ball.draw()
        lst.append(next_ball)
    return lst


def main():  # Головна функція
    if 'main_ball' in globals():
        main_ball.move()
        if len(other_balls) - BAD_BALLS == 0:  # Умови перемоги
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text='You Win!', font='Arial 32', fill='blue')
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx == 0:  # Умови поразки
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text='You Lose!', font='Arial 32', fill='red')
    root.after(5, main)  # Визначаємо швидкіть руху кулі


root = tkinter.Tk()
root.title('Гра у кулю')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack()

canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>', mouse_click)
main()

other_balls = create_balls_list(BALL_COUNT)
bad_balls = create_balls_list(BAD_BALLS, bad=True)
other_balls += bad_balls

root.mainloop()

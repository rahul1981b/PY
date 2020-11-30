import random
from turtle import Turtle, Screen
from Race import race

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
my_screen = Screen()
my_screen.setup (width=1000, height=1000, startx=0, starty=0)


def make_wave():
    n = 0
    while n < 2:
        #timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)
        timmy_the_turtle.forward(100)
        n += 1
    my_screen.exitonclick()

def make_squre():
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    my_screen.exitonclick()

def make_dashline():
    n = 0
    while n < 10:
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color("white")
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color("red")
        n += 1
    my_screen.exitonclick()

def draw_shape():
    sides = int(input("Please enter the sides: "))
    for _ in range(sides):
        angle = 360/sides
        timmy_the_turtle.forward(50)
        timmy_the_turtle.right(angle)
    my_screen.exitonclick()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def random_walk():
    num = 0
    col = ["blue", "red", "purple", "yellow", "pink", "green","teal", "orange", "white", "magenta", "light blue", "gold", "silver"]
    timmy_the_turtle.pensize(10)
    timmy_the_turtle.speed("fastest")
    while num < 500:
        distance = random.randrange(50,100)
        turn = random.randrange(0,2)
        timmy_the_turtle.pencolor(random.choice(col))
        timmy_the_turtle.forward(distance)
        if turn == 0:
            timmy_the_turtle.right(90)
        else:
            timmy_the_turtle.left(90)
        num += 1
    my_screen.exitonclick()

def move_forward():
    timmy_the_turtle.forward(50)

def move_backword():
    timmy_the_turtle.backward(50)

def move_left():
    timmy_the_turtle.left(10)

def move_right():
    timmy_the_turtle.right(10)

def myclear_screen():
    timmy_the_turtle.clear()
    timmy_the_turtle.home()
    timmy_the_turtle.penup()
    timmy_the_turtle.pendown()

def try_listen():
    my_screen.listen()
    my_screen.onkey(key="w", fun=move_forward)
    my_screen.onkey(key="s", fun=move_backword)
    my_screen.onkey(key="a", fun=move_left)
    my_screen.onkey(key="d", fun=move_right)
    my_screen.onkey(key="c",fun=myclear_screen)
    my_screen.exitonclick()

#make_squre()
#make_dashline()
#draw_shape()
#random_walk()
#try_listen()
my_screen.clear()
race()


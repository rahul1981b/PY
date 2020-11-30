from turtle import Turtle, Screen
import random

turtle_y_position = [0, 25, 50, 75, 100, 125]
turtle_color = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtle = []
my_race_screen = Screen()
my_race_screen.setup(width=1000, height=1000, startx=0, starty=0)

def race():
    is_race_on = 0
    for index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(turtle_color[index])
        new_turtle.penup()
        new_turtle.goto(x=-500, y=turtle_y_position[index])
        new_turtle.speed("fast")
        all_turtle.append(new_turtle)

    user_bet = my_race_screen.textinput(title="Make your bet",
                                        prompt="which Turtle will wint the race? enter the color: ")

    while 1:
        if user_bet in turtle_color:
            is_race_on = 1
            break
        else:
            user_bet = my_race_screen.textinput(title="Make your correct bet",
                                                prompt="which Turtle will wint the race? enter the color: ")

    while is_race_on:
        for turtle in all_turtle:
            if turtle.xcor() > 500:
                if turtle.pencolor() != user_bet:
                    print(f"Your turtle lost because {turtle.pencolor()} won :(")
                else:
                    print(f"Your {user_bet} turtle won :) :) :)")
                exit()
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    my_race_screen.exitonclick()


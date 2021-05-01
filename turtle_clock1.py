#!/usr/bin/env python3

from turtle import *
import datetime

SIZE = 150

def main():
    my_screen = Screen()
    my_screen.bgcolor("grey")

    mode("logo")
    face_turtle = Turtle()
    face_turtle.hideturtle()

    draw_face(face_turtle, SIZE)

    hour_turtle = Turtle()
    hour_turtle.hideturtle()
    min_turtle = Turtle()
    min_turtle.hideturtle()
    sec_turtle = Turtle()
    sec_turtle.hideturtle()

    hour = minute = None
    while True:
        t = datetime.datetime.today()
        if not t.hour == hour:
            hour = t.hour
            hour_turtle.color(my_screen.bgcolor())
            draw_time(hour_turtle, t.hour, 30, SIZE*.5, 8, "black")
        if not t.minute == minute:
            minute = t.minute
            min_turtle.color(my_screen.bgcolor())
            draw_time(min_turtle, t.minute, 6, SIZE*.7, 5, "black")
        draw_time(sec_turtle, t.second, 6, SIZE*.7, 3, "red")


    my_screen.exitonclick()

def draw_face(my_turtle, size):
    my_turtle.clear()
    my_turtle.goto(0,0)
    my_turtle.dot(size*0.3,"orange")
    my_turtle.up()
    offsets = ((0,1),(1,0),(0,-1),(-1,0))

    for i in range(4):
        my_turtle.goto(size*offsets[i][0], size*offsets[i][1])
        my_turtle.down()
        my_turtle.dot(size*0.1,"black")
        my_turtle.up()

    for i in range(12):
        my_turtle.goto(0,0)
        my_turtle.right(30)
        my_turtle.forward(size)
        my_turtle.down()
        my_turtle.dot(size*0.05,"black")
        my_turtle.up()

def draw_time(my_turtle, seg, degs, size, pensize, pencolour):
    my_turtle.clear()
    # my_turtle.speed(7)
    # my_turtle.up()

    my_turtle.home()
    my_turtle.right(seg*degs)
    my_turtle.down()
    my_turtle.pensize(pensize)
    my_turtle.color(pencolour)
    my_turtle.forward(size)


if __name__ == "__main__":
    main()

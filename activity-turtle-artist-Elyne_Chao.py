# Turtle Artist
# Author: Elyne
# 28 October

import turtle

# A one-of-a-kind drawing

wn = turtle.Screen()
wn.bgcolor("#baffe9")
t = turtle.Turtle()
t.turtlesize(0.25)
t.color("black")
t.speed(10)

def draw_watermelon(x: int, y: int):
    """Draws a watermelon at the location x and y.
    """
    # make sure cookie is facing east
    t.setheading(0)
    # set pen color and watermelon peel color
    t.pencolor("black")
    t.fillcolor("#629c4b")
    # draw half a circle
    t.penup()
    t.goto(x - 55, y)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.circle(60, 180)
    t.setheading(0)
    t.backward(120)
    t.end_fill()
    # choose color for watermelon flesh
    t.fillcolor("#db6565")
    # draw a smaller semi-circle
    t.penup()
    t.goto(x - 45, y)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.circle(50,180)
    t.setheading(0)
    t.backward(100)
    t.end_fill()

    # draw the seeds of the watermelon
    t.penup()
    t.setheading(90)
    t.forward(-10)
    t.right(90)
    t.forward(25)
    t.pd()
    t.turtlesize(0.5)
    t.stamp()
    # draw second seed
    t.pu()
    t.forward(17)
    t.pd()
    t.stamp()
    # draw third seed
    t.pu()
    t.forward(17)
    t.pd()
    t.stamp()
    # draw fourth seed
    t.pu()
    t.forward(17)
    t.pd()
    t.stamp()
    # second row of seeds
    t.pu()
    t.backward(45)
    t.right(90)
    t.forward(17)
    t.left(90)
    t.pd()
    t.stamp()
    # second seed
    t.pu()
    t.forward(17)
    t.pd()
    t.stamp()
    # third seed
    t.pu()
    t.forward(17)
    t.pd()
    t.stamp()

# draw the watermelons at different spots
draw_watermelon(0, 0)
draw_watermelon(100, 100)
draw_watermelon(100,-100)
draw_watermelon(-100,100)
draw_watermelon(-100,-100)
draw_watermelon(200, 200)
draw_watermelon(200,-200)
draw_watermelon(-200,200)
draw_watermelon(-200,-200)
draw_watermelon(300, 300)
draw_watermelon(300,-300)
draw_watermelon(-300, 300)
draw_watermelon(-300,-300)

wn.exitonclick()

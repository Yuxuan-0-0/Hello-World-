# Hello word - homework - week 4
# Yuxuan
# yhou10@sva.edu

# Assignment 1

import turtle 

spiralsquare = turtle.Turtle()

spiralsquare.speed(20)

for i in range(140):
    if i<=20:
        spiralsquare.pencolor("red")
    elif 20<i<=40:
        spiralsquare.pencolor("orange")
    elif 40<i<=60:
        spiralsquare.pencolor("yellow")
    elif 60<i<=80:
        spiralsquare.pencolor("green")
    elif 80<i<=100:
        spiralsquare.pencolor("cyan")
    elif 100<i<=120:
        spiralsquare.pencolor("blue")
    elif 120<i<=140:
        spiralsquare.pencolor("purple")
    spiralsquare.forward(i*2)
    spiralsquare.right(90)

for i in range(140):
    if i<=20:
        spiralsquare.pencolor("red")
    elif 20<i<=40:
        spiralsquare.pencolor("orange")
    elif 40<i<=60:
        spiralsquare.pencolor("yellow")
    elif 60<i<=80:
        spiralsquare.pencolor("green")
    elif 80<i<=100:
        spiralsquare.pencolor("cyan")
    elif 100<i<=120:
        spiralsquare.pencolor("blue")
    elif 120<i<=140:
        spiralsquare.pencolor("purple")
    spiralsquare.forward(i*2)
    spiralsquare.right(90)

for i in range(140):
    if i<=20:
        spiralsquare.pencolor("red")
    elif 20<i<=40:
        spiralsquare.pencolor("orange")
    elif 40<i<=60:
        spiralsquare.pencolor("yellow")
    elif 60<i<=80:
        spiralsquare.pencolor("green")
    elif 80<i<=100:
        spiralsquare.pencolor("cyan")
    elif 100<i<=120:
        spiralsquare.pencolor("blue")
    elif 120<i<=140:
        spiralsquare.pencolor("purple")
    spiralsquare.forward(i*2)
    spiralsquare.right(90)


turtle.done()
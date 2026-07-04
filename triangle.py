from turtle import *
import time

setup(800, 800)
bgcolor("black")
speed(0)
hideturtle()
pensize(2)
color("blue")
tracer(0, 0)

for i in range(100):
    forward(400)
    left(120)
    forward(400)
    left(120)
    forward(400)
    left(120)
    left(4)
    update()
    time.sleep(0.03)

done()
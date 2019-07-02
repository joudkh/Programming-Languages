
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(200):
    pencolor(colors[x % 6])
    speed(99900)
    width(x / 100 + 1)
    forward(x)
    left(59)

from turtle import *
import random
bgcolor('#3BB9FF')
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for n in range(60):
    speed(99900)
    penup()
    goto(random.randint(-300, 300), random.randint(-300, 300))
    pendown()
    pencolor(colors[n % 6])
    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))
    for i in range(6):
        circle(circle_size)
        left(60)

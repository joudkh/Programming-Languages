from turtle import *
XXX=Turtle()
colors = ['red', 'purple', 'blue','#A52A2A','#00FFFF','#C19A6B', '#FF00FF']

for i in range(200):
    pencolor(colors[i % 7])
    speed(600)
    forward(i)
    left(120)
 

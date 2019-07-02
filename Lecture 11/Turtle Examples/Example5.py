from turtle import *
XXX=Turtle()
colors = ['red','blue','#A52A2A','#00FFFF','#C19A6B', '#FF00FF']
begin_fill()
while True:
    for i in range(36):
        speed(99000)
        for i in range(36):
            pencolor(colors[i % 6])
            forward(10)
            left(10)
        left(10)

begin_fill()
done()


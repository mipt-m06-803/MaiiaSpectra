import turtle
import math
s=0
x = 100*math.sin(s) - 50*math.cos(2*s)
y = 100*math.cos(s) - 50*math.sin(2*s)
turtle.shape('turtle')
turtle.pendown
for s in range (0,360, 1):
    turtle.goto(x, y)
    x = 100*math.sin(s) - 50*math.cos(2*s)
    y = 100*math.cos(s) - 50*math.sin(2*s)
    


    

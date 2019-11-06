import turtle
__import__("turtle").__traceable__ = False
from turtle import *
#color('red', 'yellow')
leo=turtle.Turtle()
leo.speed(9)
leo.color("red","black")
leo.pensize(1)
leo.begin_fill()
##for xxx in range(50):
##    leo.forward(200)
##    leo.left(170)


#leo.setx(-100)
while True:
 
    leo.forward(500)
    leo.left(170)
    #mess around with setting a variable to start location
    if abs(leo.pos()) < 1:
        break
    
leo.end_fill()

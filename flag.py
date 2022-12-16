import turtle
from turtle import *

# Making a screen for output
screen = turtle.Screen()
screen.title("Indian Flag")

#Defining a turtle instance
t= turtle.Turtle()
speed(0)


#initial penup()
t.penup()
t.goto(-400, 250)
t.pendown()


#Orrange Color Rectangle
t.color('orange')
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)


# Green color Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

#Big Blue Circle
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

#mini blue Circles
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(15)
    t.right(15)
    t.pendown()



t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()


t.penup()
t.goto(0,0)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(60)
    t.backward(60)
    t.left(15)



turtle.done()


#Programmed by Shubham Tiwari
#Github :- https://github.com/shubhamtiwari2244217
#Twitter :- https://twitter.com/Shubham88395566
#Email :- shubhamtiwari5100@gmail.com
#instagram :- https://instagram.com/shubham_tiwari_das
#Youtube :- https://youtube.com/@GaurNitaiGroup

#Support me :- https://pages.razorpay.com/pl_HqEs5KZyzOT3RW/view

import turtle
s = turtle.getscreen()
t= turtle.Turtle()



def wheel1():
    turtle.circle(20)

t.goto(-200,200)
for i in range(30):
    t.left(10)
wheel1()
import turtle

length = 200
angle1 = 90
angle2 = 120

# this draws a square and triangle for the house
for side1 in range(4):
    turtle.forward(length)
    turtle.right(angle1)

for side2 in range(3):
    turtle.forward(length)
    turtle.left(angle2)

# below is the positioning of the pen at the first corner of the window
turtle.right(angle1)
turtle.forward(50)
turtle.left(angle1)

turtle.penup()
turtle.forward(20)
turtle.pendown()

# drawing of window outline
def window():
    for side3 in range(4):
        turtle.forward(50)
        turtle.right(90)

window()

# the lines in the window
def window_panes():
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)

window_panes()

# crossover to second window
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()

# drawing of second window using code from earlier
window()
window_panes()

# exiting drawing of second window
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.penup()
turtle.forward(30)
turtle.pendown()

# drawing of door
for side3 in range(2):
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

turtle.done()

import turtle

sides = int(input("How many sides does the shape have?"))

angle = 360 / sides
length = 100

turtle.color("red", "pink")
turtle.begin_fill()

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)

turtle.end_fill()
turtle.done()
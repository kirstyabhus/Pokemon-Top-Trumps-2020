import turtle

sides = int(input("How manyy sides does your shape have? \n"))

angle = 360 / sides
length = 60

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()

import turtle

angle = 90
length = 100

for draw in range(50):
    turtle.forward(length)
    turtle.right(angle)
    length = length - 2

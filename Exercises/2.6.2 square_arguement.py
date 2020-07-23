import turtle

def square(side_length, colour):
    angle = 90
    turtle.color(colour, colour)
    turtle.begin_fill()

    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()


square(60, 'red')
square(100, 'orange')
turtle.done()
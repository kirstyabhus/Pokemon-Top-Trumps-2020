import turtle

def triangle():
    side_length = 200
    angle = 120

    for side in range(3):
        turtle.color('blue', 'blue')
        turtle.begin_fill()

        turtle.forward(side_length)
        turtle.right(angle)

        turtle.end_fill()

triangle()
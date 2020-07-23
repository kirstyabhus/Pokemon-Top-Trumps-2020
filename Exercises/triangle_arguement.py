import turtle

def triangle(side_length, colour):
    angle = 120
    turtle.colour('colour')

    turtle.begin_fill()
    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.endfill()


triangle(100, 'orange')
triangle(90, 'red')
triangle(80, 'blue')
triangle(70, 'pink')

turtle.done()
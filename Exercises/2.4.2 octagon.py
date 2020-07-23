import turtle


side_length = 100
angle = 45

turtle.color('red', 'orange')
turtle.begin_fill()

for side in range(8):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.end_fill()

turtle.done()
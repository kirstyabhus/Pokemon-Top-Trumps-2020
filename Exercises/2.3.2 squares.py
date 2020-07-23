import turtle

length = 100
angle = 90

def square():
    for side in range(4):
        turtle.forward(length)
        turtle.right(angle)



square()
turtle.forward(200)
square()
turtle.done()

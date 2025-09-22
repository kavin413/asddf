import turtle 
square_turtle = turtle.Turtle()

side_length = 100
for _ in range(4):
    square_turtle.forward(side_length) 
    square_turtle.left(90)

turtle.done()
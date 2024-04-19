import turtle
turtle.bgcolor("black")


Triangle=turtle.Turtle()
Triangle.speed(20)
Triangle.pencolor("red")
for i in range (3000):
    Triangle.forward(i)
    Triangle.left(91)
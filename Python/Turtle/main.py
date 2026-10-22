import turtle

screen = turtle.Screen()

t = turtle.Turtle()
t.width(30)
t.pencolor("blue")

t.penup()
t.goto(0, 100)
t.pendown()

# Draw a square
t.right(30)
for _ in range(6):
    t.forward(200)
    t.right(60)

t.right(60)
t.penup()
t.goto(t.xcor() - 20.0, t.ycor() - 125.0)
t.pendown()
t.forward(150)
t.right(270)
t.circle(75, 180)

# Keep the window open until you click it
screen.exitonclick()

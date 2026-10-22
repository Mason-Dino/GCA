import turtle

screen = turtle.Screen()

t = turtle.Turtle()

# Draw a square
for _ in range(6):
    t.forward(100)
    t.right(60)

# Keep the window open until you click it
screen.exitonclick()

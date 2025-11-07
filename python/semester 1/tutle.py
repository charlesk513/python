# import turtle

# screen = turtle.Screen()
# screen.title("Turtle Test")

# t = turtle.Turtle()
# t.speed(1)

# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# for _ in range(4):
#     t. forward(100)
#     t.left(90)


# screen = turtle.Screen()
# screen.bgcolor("black")
# t = turtle.Turtle()
# t.speed(0)
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "gold"]

# for i in range(36):
#     t.color(colors[i % len(colors)])
#     t.circle(100)
#     t.right(10)

# t.hideturtle()


# screen = turtle.Screen()
# screen.bgcolor("grey")
# t = turtle.Turtle()
# t.speed(0)
# t.penup()

# text = "kc tech group"
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "white", "gold"]

# x, y = -200, 0  # Starting position

# for i, char in enumerate(text):
#     t.goto(x + i * 40, y)
#     t.color(colors[i % len(colors)])
#     t.write(char, font=("Arial", 28, "bold"))

# t.hideturtle()
# turtle.done()


    
from swampy.TurtleWorld import *

world = TurtleWorld()
charles = Turtle()
charles.delay = 0.01

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)

def arc(t, r, angle):
    arc_length = 2 * 3.14159 * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0 / n)

flower(charles, 7, 60, 60)
wait_for_user()


# import turtle;
# turtle.forward(100);
# turtle.left(90);
# turtle.done()
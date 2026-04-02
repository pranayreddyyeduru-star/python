# 1) Import the `turtle` library to draw shapes on a screen.

# 2) Set up the turtle drawing screen:
#    a) Change the background color to "orange".
#    b) Set the screen size using `setup(width, height)`.

# 3) Create a Turtle object and store it in `polygon`.
#    (This turtle will do the drawing.)

# 4) Store polygon details in variables:
#    a) `num_sides` = number of sides of the polygon (here, 6).
#    b) `side_length` = length of each side.
#    c) Calculate the turning angle using `angle = 360.0 / num_sides`.

# 5) Use a loop to draw the polygon:
#    a) Repeat `num_sides` times.
#    b) Move the turtle forward by `side_length`.
#    c) Turn the turtle right by `angle` degrees after each side.

# 6) Call `turtle.done()` to keep the turtle window open after drawing
#  finishes.
import turtle
turtle.Screen().setup(400,400)
turtle.Screen().bgcolor("orange")
p=turtle.Turtle()
num_sides=6
side_length=70
angle=360.0/num_sides
for i in range(num_sides):
    p.forward(side_length)
    p.right(angle)
turtle.done()
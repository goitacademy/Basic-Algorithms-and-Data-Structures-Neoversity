import turtle
screen = turtle.Screen() # Create the screen.
screen.setup(320, 320)   # Set Window size.

###### TURTLE SHAPE, SPEED, PEN SIZE, COLOR ######
TTL = turtle.Turtle()
TTL.speed(0) #Set the turtle's speed. 1 is slow, 10 is fast; 0 is fastest.
TTL.color("brown") #Set the turtle's color.
TTL.pensize(1) #Set width of turtle drawing pen.

###### SET TURTLE STARTING POSITION ######
TTL.penup() # Do not let the turtle draw while moving to position (0, 110).
TTL.setposition(0, -100)
TTL.pendown() # Enable the turtle to draw.
TTL.hideturtle()
TTL.setheading(90)

###### VARIABLES ######
# Variable 'branchLength' is the starting length of tree brach.
# Variable 'branchReduction' subtracts from 'branchLength' in
# each recursion iteration.
# Variable 'recursionLevel' is the recursion iteration number.

###### DEFINE treeFractal FUNCTION ######
# Draw a fractal with recursion level, tree branch length,
# branch length reduction for each iteration, and
# the angle by which the branch turns each iteration.
def treeFractal(TTL, recursionLevel, branchLength, branchReduction, angle):
  if recursionLevel == 0:
    TTL.fd(0)
  else:
    branchLength = branchLength - branchReduction
    TTL.forward(branchLength)
    TTL.left(angle)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.right(angle * 2)
    treeFractal(TTL, recursionLevel-1, branchLength, branchReduction, angle)
    TTL.left(angle)
    TTL.backward(branchLength)
# Call treeFractal function with the following parameters.
# Recursion Level = 7; Branch length = 50.
# Branch reduction each recursion iteration = 5.
# Turn left of right angle by 25 degrees.
treeFractal(TTL, 9, 45, 5, 25)

screen.exitonclick() # Exit screen
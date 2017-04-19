import turtle

s = turtle.Screen()
t = turtle.Turtle()

length = None
while not length:
    try:
        length = float(input('Enter a line length of your turtle: ')) # Taking length as input from user.
    except ValueError:
        print('You need to enter a number')# If input is wrong throwing an exception.

width = None
while not width:
    try:
        width = float(input('Enter a line width of your turtle: '))# Taking width as input from user.
    except ValueError:
        print('You need to enter a number')# If input is wrong throwing an exception.

color = None
while not color:
    color = input('Enter color for your turtle: ')# Taking color as input from user.
    try:
        t.pencolor(color)
    except:
        print('Choose different color,this color is not in my memory')# If input is wrong throwing an exception.
        color = None
shape = None
while not shape:
    shape = input('Choose what you want to draw a line, triangle, or square: ')# Taking shape as input from user.
    if shape.lower() not in ['line', 'triangle', 'square']:
        shape = None
        print('Choose either line,triangle or squares')# If input is not in the list,asking user to again enter the shape.


t.pensize(width)
if shape.lower() == 'line': # Drawing line.
    t.forward(length)
elif shape.lower() == 'triangle': # Drawing Triangle.
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
else:					# Drawing square.
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)

s.exitonclick()

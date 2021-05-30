
'''
=============================
RandomColoring Pixel
Created by: Yuliya Vaskiv
Date: 05/28/2021
..............................

This app randomly selects color
for square that is drawn using turtle.
The app takes several arguments such as size of sgare,
x and y coordinates where the first sqaure will be drawn,
and the width and height of of all sqaure combined.

This app suppose to ctreate some random picture

===========================================================

Notes:
The app doesn't consider the width and height a real basis.
If height or width is divided by size and it leaes reamining number,
the size of picture would correspond to width/height
05/28/2021
'''

import random
import turtle

def colorPicker(lis): #picks a random color
    randomN = random.randint(0, len(lis) - 1)
    color = lis[randomN]
    print (color)
    return color


#draws sqayre changing y coordinates
def drawingSingleSqaure(X, endX, Y, size, colorList, w):

    #determine count for column
    columns = w / size
    column = 0

    #when x meets the endpoint and columns program loop ends
    while (X < endX and column < columns):
        
        t.speed(0.000000001)
        
        #fill color in square
        color = colorPicker(colorList) #calls function for random color
        t.color(color)
        t.fillcolor(color)
        t.begin_fill()
        
        for i in range(4): #draw one square with sides 
            t.forward(size)
            t.right(90)

        t.end_fill()

        #changes x coordinate on turtle
        t.up()
        X = X + size
        t.goto(X, Y)
        t.down()

        #counts column
        column = column + 1


def drawPixel(t, X, Y, w, l, colorList, size):

    t.up()
    t.goto(X, Y)
    t.down()

    #coordinates where drawing should stop
    endX = X + w
    endY = Y + l

    #saves first coordinates
    initialX = X
    initialY = Y

    #determine count for rows
    rows = l / size
    row = 0

    #when y coordinate meets the endpoint and row, loop stops
    while (Y < endY and row < rows):

        #calls other fuction for drawing on x line
        drawingSingleSqaure(X, endX, Y, size, colorList, w)

        #changes the value for Y
        t.up()       
        Y = Y - size
        t.goto(initialX, Y)
        t.down()

        #counts rows
        row = row + 1


    

'''============================================================
===============================================================
============================================================'''

#parameters 
colorList = ['red', 'magenta', 'orange', 'gold', 'yellow',
             'green', 'lightgreen', 'darkgreen', 'blue',
             'cyan', 'purple', 'violet',
             'maroon', 'black', 'green', 'brown', 'white']


size = 30
w = 500
l = 500
x = -300
y = 300

t = turtle.Turtle()
t.speed(0.000000001)


#calls function
drawPixel(t, x, y, w, l, colorList, size)


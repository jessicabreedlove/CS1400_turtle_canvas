from turtle import Turtle, Screen
import sys

def main():
    
    try:
        commandPrompt = sys.argv
        
        # width = int(input("Enter width here: "))
        # height = int(input("Enter height here: "))
        width = int(commandPrompt[1])
        height = int(commandPrompt[2])
    except ValueError:
        print("Enter positive integers for width and height.")
        return
    if width < 1 or height < 1:
        print("Enter positive integers for width and height")
        return
    
    # mood = input("Enter 'awake', 'asleep', or 'regular'").lower()

    mood = commandPrompt[3]

    s, t, xStart, yStart = Screen(), Turtle(), 0, 0
    s.setup(width, height)
    s.setworldcoordinates(0, 0, width, height)
    t.width(2)
    t.speed(0)
    scene(width, height, mood, t)
    drawRectangle(t, 0, 0, width, height/5, "green")
    drawTriangle(t, width / 2 - 75 / 2, height/5, 75)
    newPosition = drawRectangle(t, width / 2 - width / 20, height / 10 * 2.4, width / 10, width / 10 * 3 / 4)
    width /= 10
    height /= 10 * 3 / 4
    scene(width, height, mood, t, newPosition[0], newPosition[1] )
    input()
    
def scene(width, height, mood, t:Turtle, xStart=0, yStart=0):
    xUnit = width / 10
    yUnit = height / 10
    if mood == "awake":
        colors = {"sky1": "yellow", "sky2": "orange", "sky3": "red", "mtn": "grey", "sun": "white", "star": "pink"}
    elif mood == "asleep":
        colors = {"sky1": "pink", "sky2": "purple", "sky3": "blue", "mtn": "black", "sun": "light grey", "star": "grey"}
    else:
       colors = {"sky1": "blue", "sky2": "orange", "sky3": "brown", "mtn": "pink", "sun": "white", "star": "yellow"} 
    drawRectangle(t, xStart + xUnit - xUnit, yStart + height - yUnit * 4, width, yUnit * 3, colors["sky1"] )
    drawRectangle(t, xStart + xUnit-xUnit, yStart + yUnit*4, width, yUnit * 2, colors["sky2"])
    drawRectangle(t, xStart + xUnit-xUnit, yStart + yUnit * 3, width, yUnit, colors["sky3"])
    drawCircle(t, xStart + width / 2, yStart + height / 2, xUnit * 1.5, colors["sun"])
    drawTriangle(t, xStart + xUnit - xUnit, yStart + yUnit * 3, width / 2, colors["mtn"])
    drawTriangle(t, xStart + width / 2, yStart + yUnit * 3, width / 2, colors["mtn"])
    drawTriangle(t, xStart + xUnit, yStart + yUnit * 6.5, xUnit * 3 / 4, colors["star"], 90)
    drawTriangle(t, xStart + xUnit * 1.2, yStart + yUnit * 6.7, xUnit * 3 / 4, colors["star"], 130)
    
def drawSquare(t: Turtle, x, y, length, color="white", setheading=0):
    t.up()
    t.goto(x, y)
    t.setheading(setheading)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for count in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()
    
def drawRectangle(t: Turtle, x, y, length, width, color="white", setheading=0):
    t.up()
    t.goto(x, y)
    t.setheading(setheading)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for count in range(4):
        if count % 2 == 0:
            t.forward(length)
        else:
            t.forward(width)
        t.left(90)
    t.end_fill()
    return t.pos()

def drawTriangle(t: Turtle, x, y, length, color="white", setheading=0):
    t.up()
    t.goto(x, y)
    t.setheading(setheading)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for count in range(3):
        t.forward(length)
        t.left(120)
        print(t.pos())
    t.end_fill()
    
def drawCircle(t: Turtle, x, y, radius, color="white"):
    t.up()
    t.goto(x, y)
    t.setheading(360)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
if __name__ == "__main__":
    main()
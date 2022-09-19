import turtle, random
from turtle import Screen, Turtle
from ColorExtractor import ColorExtractor

colorextractor = ColorExtractor()
rgb_collection = colorextractor.extract_and_return_rgb(6)
print(rgb_collection)

screen = Screen()
#basic turtle setup
turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(20)
tim.penup()
#get to starting point
tim.setheading(225)
tim.forward(400)
tim.setheading(0)
#we will draw 150 dots
dot_amount = 150

for counter in range(1, dot_amount + 1):
    tim.dot(20, random.choice(rgb_collection))
    tim.penup()
    tim.forward(75)

    #after 10 dots the turtle goes up, turns around and goes back to start the next line
    if counter % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(40)
        tim.setheading(180)
        tim.forward(750)
        tim.setheading(0)

screen.exitonclick()

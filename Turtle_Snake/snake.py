import turtle
from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def move(self):
        # range: start, stop, step
        for seg in range(len(self.segments) - 1, 0, -1):
            # second to last segment's x and y coordinates
            newX = self.segments[seg - 1].xcor()
            newY = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, pos):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(pos)
        self.segments.append(tim)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())  # get the last segment with -1

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
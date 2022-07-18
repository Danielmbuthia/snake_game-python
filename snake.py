from turtle import Turtle

# constant
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]  # snake head

    def create_snake(self):
        for position in START_POSITION:
            self.add_turtle(position)

    def add_turtle(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.all_turtles.append(tim)

    def extend_turtle(self):
        self.add_turtle(self.all_turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)  # second last position
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

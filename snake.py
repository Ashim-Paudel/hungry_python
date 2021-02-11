from turtle import Turtle

START_POSITION = [(0, 0), (-12, 0), (-24, 0)]


class Snake:

    move_distance = 14

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("orange")

    def create_snake(self):
        for positions in START_POSITION:
            self.add_segment(positions)

    def add_segment(self, position):
        snake = Turtle(shape='square')  # creating a snake object
        snake.penup()
        snake.color('white')
        snake.shapesize(stretch_wid=0.6, stretch_len=0.6)
        snake.goto(position)
        self.segments.append(snake)


    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def is_tail_cut(self):
        for seg in self.segments[1:]:
            if seg.distance(self.head) < 10:
                return True

    def move_fd(self):
        a = list(range(len(self.segments)))[::-1]
        for seg_index in a:
            if seg_index == 0:
                self.head.fd(self.move_distance)
            else:
                self.segments[seg_index].setpos(self.segments[seg_index - 1].pos())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

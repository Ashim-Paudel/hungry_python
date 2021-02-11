from turtle import Turtle
bound_x = (-285, 279)
bound_y = (-279, 256)


class BoundaryLines(Turtle):            # class to create boundary lines

    def __init__(self):
        super().__init__()
        self.color('magenta')
        self.penup()
        self.hideturtle()
        self.goto(-298, 271)
        self.pendown()
        self.goto(-298, -287)
        self.goto(289, -287)
        self.goto(289, 271)
        self.goto(-298, 271)

    def is_collided(self, snake):            # defining collision with wall
        return (snake.head.xcor() < -294.5 or snake.head.xcor() > 280.5
                or snake.head.ycor() < -280.5 or snake.head.ycor() > 267)



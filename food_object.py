""""To keep track of food objects displayed randomly in the screen"""

from turtle import Turtle, Screen
import random

bound_x = (-285, 279)
bound_y = (-279, 256)


class Food(Turtle):

    colors = ['blue', 'green', 'red']

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color(random.choice(self.colors))
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(random.randint(-285, 279), random.randint(-279, 256))

    def collision_action(self):
        self.color(random.choice(self.colors))
        self.goto(random.randint(-285, 279), random.randint(-279, 256))


# this big food is unused for this game.....
class BigFood(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("purple")
        self.shape('turtle')
        self.setheading(random.choice([0, 90, 180, 270]))
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.penup()

    def place_big_food(self):
        self.goto(random.randint(-283, 277), random.randint(-277, 254))

    def check_collision(self, snake_head):
        return self.distance(snake_head) < 10


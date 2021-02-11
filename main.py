""" Snake game """
from turtle import Screen   # importing all reqd modules
from snake import Snake
from food_object import Food
from score_tracker import ScoreTracker, HighScore
from boundary_lines import BoundaryLines
import time

screen = Screen()       # creating a screen instance
screen.title("Snake Game -  By Ashim")
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)    # preventing user from resizing screen
screen.bgcolor("black")
screen.bgpic("background.png")
screen.tracer(0)

speed = 0.1


def updater():
    screen.update()
    time.sleep(speed)


snake = Snake()
food = Food()
current_score = ScoreTracker()
high_score = HighScore()
high_score.print_high_score()
boundary = BoundaryLines()
current_score.print_score()
screen.update()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    updater()
    snake.move_fd()

    if food.distance(snake.head) < 15:            # detect collision:
        food.collision_action()
        current_score.erase_score()
        current_score.score += 1
        current_score.print_score()
        snake.extend_snake()
        screen.update()

    if boundary.is_collided(snake):
        game_over = ScoreTracker().game_over()
        high_score.add_scores(current_score)
        game_is_on = False

    if snake.is_tail_cut():
        game_over = ScoreTracker().game_over()
        high_score.add_scores(current_score)
        game_is_on = False

screen.exitonclick()

"""keep track of current score and high score"""
from turtle import Turtle


class ScoreTracker(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.goto(-240, 275)

    def increase_score(self):
        self.score += 1

    def erase_score(self):
        self.clear()

    def print_score(self):
        self.write(arg=f"Current Score: {self.score}", align="left", font=("Comic Sans MS", 14, "bold"))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(arg="Game Over", align="Center", font=("Algerian", 56, "normal"))


class HighScore(ScoreTracker):

    def __init__(self):
        ScoreTracker.__init__(self)
        self.goto(80, 275)
        self.highscore = 0
        self.write_file()

    def print_high_score(self):
        self.write(arg=f"High Score: {self.highscore}", align="left", font=("Comic Sans MS", 14, "bold"))

    def write_file(self):
        highscore_file = open('high_score.txt', 'a+')
        highscore_file.write(str(0) + '\n')
        highscore_file.seek(0)
        self.highscore = max([int(scores) for scores in highscore_file.readlines()])

    def add_scores(self, current_score):
        highscore_file = open('high_score.txt', 'a+')
        highscore_file.seek(0)

        if current_score.score > max([int(scores) for scores in highscore_file.readlines()]):   # append only highest
            highscore_file.write(str(current_score.score)+'\n')
            highscore_file.seek(0)
            self.highscore = max([int(scores) for scores in highscore_file.readlines()])
            self.clear()
            self.print_high_score()
            highscore_file.close()
        else:
            highscore_file.close()

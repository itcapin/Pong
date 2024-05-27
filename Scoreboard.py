from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, player_name, cpu_name):
        super().__init__()
        self.color("gold")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.player_name = player_name
        self.cpu_name = cpu_name
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"{self.player_name}: {self.lscore}", align="center", font=("Courier", 24, "normal"))
        self.goto(200, 200)
        self.write(f"{self.cpu_name}: {self.rscore}", align="center", font=("Courier", 24, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.update()

    def rpoint(self):
        self.rscore += 1
        self.update()


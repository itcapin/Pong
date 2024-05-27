from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color="white", length=5):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=length, stretch_len=1)
        self.color(color)
        self.penup()
        self.goto(position)
        self.speed = 0

    def go_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)

    def move(self):
        new_y = self.ycor() + self.speed
        if new_y > 250 or new_y < -250:  # Adjust this condition to keep the paddle within the bounds
            self.speed *= -1
        self.goto(self.xcor(), new_y)

class PlayerPaddle(Paddle):
    def __init__(self, position):
        super().__init__(position, color="gray", length=5)

class CPUPaddle(Paddle):
    def __init__(self, position, speed, difficulty):
        length = 5 + (difficulty - 1) * 2  # Increase length based on difficulty
        super().__init__(position, color="darkgreen", length=length)
        self.speed = speed



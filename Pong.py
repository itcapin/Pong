from turtle import Screen, Turtle
from Paddle import PlayerPaddle, CPUPaddle
from Ball import Ball
from Scoreboard import Scoreboard
from PIL import Image
import pygame
import time

def start_game(player_name, cpu_name, cpu_speed, cpu_difficulty):
    screen.clear()
    screen.bgcolor("peru")
    screen.setup(width=800, height=600)
    screen.title("Ivy Bicker (Ivan Edition)")
    screen.tracer(0)
    show_title("IVY BICKER")

    lpaddle = PlayerPaddle((-350, 0))
    rpaddle = CPUPaddle((350, 0), cpu_speed, cpu_difficulty)
    ball = Ball()
    scoreboard = Scoreboard(player_name, cpu_name)

    screen.listen()
    screen.onkey(lpaddle.go_up, "w")
    screen.onkey(lpaddle.go_down, "s")

    screen.update()

    game = True
    while game:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        rpaddle.move()

        # Check for collision with the top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Check for collision with the paddles
        if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Check if ball is out of bounds and update score
        if ball.xcor() > 380:
            ball.reset()
            scoreboard.lpoint()
        if ball.xcor() < -380:
            ball.reset()
            scoreboard.rpoint()

        # Check for win condition
        if (scoreboard.lscore >= 7 or scoreboard.rscore >= 7) and abs(scoreboard.lscore - scoreboard.rscore) >= 2:
            game = False
            show_winner(scoreboard, player_name, cpu_name, ball)

    screen.exitonclick()

def show_title_screen():
    screen.bgcolor("green")
    screen.bgpic('./Images/Ivy Pixel.png')
    play_background_music()

    title = Turtle()
    title.hideturtle()
    title.penup()
    title.color("gold")
    title.goto(0, 200)
    title.write("Welcome to Ivy Bicker (Ivan Edition)", align="center", font=("Courier", 24, "bold"))
    title.goto(0, 150)
    title.write("Click to Start", align="center", font=("Courier", 18, "normal"))

    screen.update()

    screen.onscreenclick(lambda x, y: start_button_click(title))

def start_button_click(title):
    title.clear()
    screen.bgpic("")
    player_name = screen.textinput("Player Name", "Enter Bickeree name:")
    player_name = player_name if player_name else "Left Paddle"  # Default name if input is empty
    select_cpu_difficulty(player_name)

def select_cpu_difficulty(player_name):
    screen.clear()
    screen.bgpic('./Images/Bickerers.png')
    screen.bgcolor("green")
    title = Turtle()
    title.hideturtle()
    title.penup()
    title.color("gold")
    title.goto(0, 100)
    title.write("Select Bickerer", align="center", font=("Courier", 24, "bold"))
    title.goto(0, 50)
    title.write("1: Henry Knoll (Easy)", align="center", font=("Courier", 18, "normal"))
    title.goto(0, 20)
    title.write("2: Artemis Veizi (Medium)", align="center", font=("Courier", 18, "normal"))
    title.goto(0, -10)
    title.write("3: Anton Stengel (Hard)", align="center", font=("Courier", 18, "normal"))

    screen.update()

    screen.onkey(lambda: start_game(player_name, "Henry Knoll", 15, 2), "1")
    screen.onkey(lambda: start_game(player_name, "Artemis Veizi", 25, 3), "2")
    screen.onkey(lambda: start_game(player_name, "Anton Stengel", 35, 4), "3")
    screen.listen()

def show_title(title_text):
    title = Turtle()
    title.hideturtle()
    title.penup()
    title.color("darkgreen")
    title.goto(0, 260)  # Adjust the y-coordinate as needed
    title.write(title_text, align="center", font=("Courier", 24, "bold"))

def show_winner(scoreboard, player_name, cpu_name, ball):
    ball.hideturtle()
    winner = Turtle()
    winner.hideturtle()
    winner.penup()
    winner.color("gold")
    if scoreboard.lscore > scoreboard.rscore:
        winner_message = f"Congratulations, {player_name}! You got into Ivy!"
    else:
        if cpu_name == "Henry Knoll":
            winner_message = "You lost to Henry Knoll. Hosed!"
        elif cpu_name == "Artemis Veizi":
            winner_message = "You lost to Artemis Veizi. Hosed!"
        elif cpu_name == "Anton Stengel":
            winner_message = "You lost to Anton Stengel. Hosed!"

    winner.write(winner_message, align="center", font=("Courier", 24, "bold"))
    screen.update()

def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('/Users/ivan/Desktop/Pong Music.mp3')
    pygame.mixer.music.play(-1)

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
show_title_screen()

screen.mainloop()


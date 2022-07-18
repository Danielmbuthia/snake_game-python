from turtle import Screen
import time

from food import Food
from snake import Snake
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increment_score()
        snake.extend_turtle()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_board.game_over()

    # detect collision with all others segment
    for segment in snake.all_turtles[1:]:      # list slice
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()

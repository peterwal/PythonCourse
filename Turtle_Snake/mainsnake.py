import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 600)
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    # update screen every 0.1 seconds
    screen.update()
    time.sleep(0.1)
    snake.move()

    # colliding with food?
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()


    # detect walls and end game
    if snake.head.xcor() > 460 or snake.head.xcor() < -460 or snake.head.ycor() < -400 or snake.head.ycor() > 400:
        scoreboard.reset_scoreboard()
        scoreboard.keep_score()
        snake.reset_snake()

    # is head colliding with tail
    # loop through all segments except the first one, the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # if the snake head is away less than 10px from any segment
            scoreboard.reset_scoreboard()
            scoreboard.keep_score()
            snake.reset_snake()



screen.exitonclick()

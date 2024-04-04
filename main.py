from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_over = False
while not game_over:
    screen.update()     
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend_snake()
        score.encrease_score() 

    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() < -300 or snake.head.ycor() < -280 or snake.head.ycor() > 300:
        score.reset_game()
        score.update_sroreboard()
        snake.reset_game()
    
        
    # detect a collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            score.update_sroreboard()
            snake.reset_game()
            


    





screen.exitonclick()
from snake_and_food import snake,scoring
from Creating_screen import screen
import time


if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
    time.sleep(1)
    screen.clear()
    screen.bgcolor('turquoise')
    scoring.goto(0,0)
    scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
for food in old_fruit:
    if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
if snake.distance(fruit) < 20:
    x = random.randint(-290, 270)
    y = random.randint(-240, 240)
    fruit.goto(x, y)
    scoring.clear()
    score += 1
    scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
    delay -= 0.001

    new_fruit = turtle.Turtle()
    new_fruit.speed(0)
    new_fruit.shape('square')
    new_fruit.color('red')
    new_fruit.penup()
    old_fruit.append(new_fruit)

for index in range(len(old_fruit) - 1, 0, -1):
    a = old_fruit[index - 1].xcor()
    b = old_fruit[index - 1].ycor()

    old_fruit[index].goto(a, b)

if len(old_fruit) > 0:
    a = snake.xcor()
    b = snake.ycor()
    old_fruit[0].goto(a, b)
snake_move()
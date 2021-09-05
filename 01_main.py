try:

    def banner():
        print('\033[31m'+"""        8888888888                           888                 888      888                            
        888                                  888                 888      888                            
        888                                  888                 888      888                            
        8888888    888d888 888  888 88888b.  888888 .d88b.   .d88888      888  8888b.  888  888  8888b.  
        888        888P"   888  888 888 "88b 888   d8P  Y8b d88" 888      888     "88b 888  888     "88b 
        888        888     888  888 888  888 888   88888888 888  888      888 .d888888 Y88  88P .d888888 
        888        888     Y88b 888 888 d88P Y88b. Y8b.     Y88b 888      888 888  888  Y8bd8P  888  888 
        8888888888 888      "Y88888 88888P"   "Y888 "Y8888   "Y88888      888 "Y888888   Y88P   "Y888888 
                                    888                                                                  
                                    888                                                                  
                                    888\033[1;m                                     \033[34mhttps://t.me/Hackingzzzz\033[1;m  """)



    # importing modules
    import time , clear , snake , turtle 
    from food import Food
    from scoreboard import Scoreboard
    clear.cls()


    # making screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(1000,700)
    screen.title("MY SNAKE GAME")
    screen.tracer(0)

    # ----
    snake = snake.Snake()
    food = Food()
    scoreb = Scoreboard()

    # detecting keys
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")
    screen.onkey(key="e",fun=exit)


    # main program
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.131)
        snake.move()

        if snake.head.distance(food) < 15:
            print("Your Score >> ",scoreb.score+1)
            
            food.refresh()
            snake.extend()
            # snake.extend()
            # snake.extend()
            scoreb.increase_score()

        # Detect_collision_with_walls
        if snake.head.xcor() > 480 or snake.head.xcor() < -480 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
            banner()
            print("OOPPSS GAME OVER")
            game_is_on = False
            scoreb.game_over()
        
        for segment in snake.segments[1:]:

            if snake.head.distance(segment) < 10:
                banner()
                print("OOPPSS GAME OVER")
                game_is_on = False
                scoreb.game_over()

    # saying screen to not exit automaticall 
    screen.exitonclick()

except Exception as e:
    print("ERROR lol")
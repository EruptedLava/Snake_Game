from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Couriel", 22, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,300)
        self.print_score_board()
        
    def print_score_board(self):
        self.write(f"Score : {self.score}",align = ALIGNMENT,font = FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score_board()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align = ALIGNMENT,font = ("Couriel", 25, "normal"))
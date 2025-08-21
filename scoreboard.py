from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over" ,align= ALIGNMENT, font= ("Courier", 30, "bold"))
        self.goto(-20,-40)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()




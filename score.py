from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100,200)
        self.lscore = 0
        self.rscore = 0
        self.write(self.lscore,align="center",font=("Arial",48,"normal"))
        self.goto(100,200)
        self.write(self.rscore, align="center", font=("Arial", 48, "normal"))
    
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Arial", 48, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Arial", 48, "normal"))
 
    def l_score(self):
        self.lscore+=1
        self.update()
        
    def r_score(self):
        self.rscore+=1
        self.update()
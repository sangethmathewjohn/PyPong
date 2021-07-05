from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.movey=10
        self.movex=10
        self.moves=0.1

    def move(self):
        x= self.xcor() +self.movex
        y = self.ycor() +self.movey
        self.goto(x,y)
    
    def bouncey(self):
        self.movey *=-1
        self.moves *=0.9
    
    def bouncex(self):
        self.movex *=-1
        self.moves *= 0.9

    def reset(self):
        self.goto(0,0)
        self.bouncex()
        self.moves=.1

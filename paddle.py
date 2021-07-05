from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        ycord =self.ycor() + 20
        self.goto(self.xcor(),ycord)

    def go_down(self):
        ycord = self.ycor() - 20
        self.goto(self.xcor(), ycord)

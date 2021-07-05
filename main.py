from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

ball = Ball()
screen = Screen()
score = Score()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


gameover= False

while not gameover:
    time.sleep(ball.moves)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    if (ball.distance(r_paddle) < 60 or ball.distance(l_paddle) < 60) and (ball.xcor() > 325 or ball.xcor() < -325):
        ball.bouncex() 
    
    if ball.xcor()>350:
        time.sleep(1)
        ball.reset()
        score.l_score()

    
    if ball.xcor()<-350:
        time.sleep(1)
        ball.reset()
        score.r_score()

    


screen.exitonclick()

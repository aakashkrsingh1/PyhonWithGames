
import turtle
import winsound


#Creating A Window
wn= turtle.Screen()
wn.title("Pong Game Created By A K A S H")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle  A
paddle_a =turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #we stretch the square shaped turtle by width
paddle_a.penup() #because we do not want the turtle to draw lines
paddle_a.goto(-350,0) #we place the paddle on the middle of the left side

#Paddle B

paddle_b =turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #because we do not want the turtle to draw lines
paddle_b.goto(350,0) #we place the paddle on the middle of the right side


#Ball
ball =turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() #because we do not want the turtle to draw lines
ball.goto(0,0) #we place the paddle on the center
ball.dx=.2
ball.dy=.2

#Socoring Mechanism-Pen 
score_a=0
score_b=0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:{}  Player B: {}".format(score_a, score_b), align="center",font=("Courier",24,"normal"))


# moving the paddles 

def a_up () :
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def a_down () :
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def b_up () :
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def b_down () :
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)



#Keyboard Bindings
wn.listen() #to listen for keyboard input
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down,"s" )
wn.onkeypress(b_up, "Up")
wn.onkeypress(b_down, "Down")




#Main Game Loop
while True:
    wn.update()
    #Moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #ball.goto(ball.xcor()+ball.dx , ball.ycor()+ball.dy)
    #BoundaryCheck Top and Bottom
    if ball.ycor()>290 :
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.ycor()<-290 :
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
       


    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write("Player A:{}  Player B: {}".format(score_a, score_b), align="center",font=("Courier",24,"normal"))

        

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_b+=1
        pen.clear()

        pen.write("Player A:{}  Player B: {}".format(score_a, score_b), align="center",font=("Courier",24,"normal"))

    
    #Making the Paddles deflect
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40) :

        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("caughtball.wav", winsound.SND_ASYNC)
    
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40) :
        
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("caughtball.wav", winsound.SND_ASYNC)

    
        
    
import turtle 
import time
import random 

# Screen Building Time
screen = turtle.Screen()
screen.title("Centipede Destroyer")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) # Turns of the automatic screen updates

#create the Player
player = turtle.Turtle()
player.shape("circle")
player.color("red")
player.penup()
player.goto(0, -250)

#set the player speed
player_speed = 15

#create a centipede segment
centipede = [turtle.Turtle() for _ in range(10)]

for segment in centipede:
    segment.shape("circle")
    segment.color("blue")
    segment.penup()

#set the centipede speed
    centipede_speed = 20

# set the direction 
    direction = "Right"

# Create the player's missle 
    missle = turtle.Turtle()
    missle.shape("square")
    missle.color("green")
    missle.penup()
    missle.speed(0)
    missle.shapesize(stretch_wid=0.5, stretch_len=0.5)
    missle.hideturtle()

# set the Bullet speed 
    missle_speed = 20


#Functions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 290:
        x = 290
    player.setx(x)

def fire_missle():
    if not missle.isvisible():
        missle.showturtle()
        x = player.xcor()
        y = player.ycor() + 10
        missle.goto(x, y)

def is_collision(t1, t2):
    distance = t1.distance(t2)
    if distance < 15:
        return True
    return False

# Keyboard Bindings 
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(fire_missle, "space")

# Main game loop
while True:
    screen.update()

    # Move the Centipede
    for segment in centipede:
        x = segment.xcor()
        if direction == "Right":
            x += centipede_speed
        else:
            x -= centipede_speed
        segment.setx(x)
    
    # Check for collisions with the screen edges
    if centipede[0].xcor() > 290 or centipede[-1].xcor() < -290:
        direction = "Left" if direction == "Right" else "Right"
        for segment in centipede:
            y = segment.ycor()
            y -= 20
            segment.sety(y)

    # Move the Missle
        if missle.isvisible():
            y = missle.ycor()
            y += missle_speed
            missle.sety(y)
    

    # Check for missle collison with centipede segments
            for segment in centipede:
                if is_collision(missle, segment):
                    segment.hideturtle()
                    missle.hideturtle()
                    segment.goto(0, 1000) 


    # Check for collisions with the player
    for segment in centipede:
        if is_collision(player, segment):
            player.hideturtle()
            segment.hideturtle()
            print("Game Over!")
            time.sleep(2)
            screen.bye()
            exit()            


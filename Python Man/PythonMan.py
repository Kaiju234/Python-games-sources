# Python Man

# Window for the main Game

import turtle
import random
import time

lives = 3
score = 0

window = turtle.Screen()
window.tracer(0)
window.title("Python Man by Raj Shah")
window.bgcolor('black')
window.setup(600, 600)

pyman = turtle.Turtle()
pyman.speed(0)
pyman.penup()
pyman.color('green')
pyman.shape('circle')
pyman.direction = 'stop'

ghouls = []
for x in range(10):
    ghoul = turtle.Turtle()
    ghoul.color('#ff0000')
    ghoul.shape('turtle')
    ghoul.speed = 0.5
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    ghoul.setposition(x,y)
    ghouls.append(ghoul)
    
    


pen = turtle.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.goto(0, 245)
pen.pendown()
pen.write('Score: {} Lives {}'.format(score, lives), align='center', font=('Courier', 36))
pen.hideturtle()

pellets = []
for _ in range(40):
    pellet = turtle.Turtle()
    pellet.speed(0)
    pellet.penup()
    pellet.color('white')
    pellet.shape('circle')
    pellet.shapesize(stretch_wid=0.4, stretch_len=0.4)
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    pellet.setposition(x, y)
    pellets.append(pellet)


# Python man Movements

def movement():
    if pyman.direction == 'up':
        y = pyman.ycor()
        y += 5
        pyman.sety(y)

    if pyman.direction == 'down':
        y = pyman.ycor()
        y -= 5
        pyman.sety(y)

    if pyman.direction == 'left':
        x = pyman.xcor()
        x -= 5
        pyman.setx(x)

    if pyman.direction == 'right':
        x = pyman.xcor()
        x += 5
        pyman.setx(x)

# Ghoul Movement
def ghoulMovement():
    # Make the Ghouls Move
    for ghoul in ghouls:
        y = ghoul.ycor()
        x = ghoul.xcor()
        y += ghoul.speed
        x += ghoul.speed
        ghoul.sety(y)
        ghoul.setx(x)
    
    

# Window Binding function
def moveUp():
    pyman.direction = 'up'


def moveDown():
    pyman.direction = 'down'


def moveLeft():
    pyman.direction = 'left'


def moveRight():
    pyman.direction = 'right'


# set window bindings
window.listen()
window.onkeypress(moveUp, 'Up')
window.onkeypress(moveDown, 'Down')
window.onkeypress(moveLeft, 'Left')
window.onkeypress(moveRight, 'Right')

while True:
    window.update()
    
    
    if pyman.xcor() > 300 or pyman.xcor() < -300 or pyman.ycor() > 300 or pyman.ycor() < -300:
        lives -= 1
        pen.clear()
        pen.write('Score: {} Lives {}'.format(score, lives), align='center', font=('Courier', 36))
        time.sleep(1)
        pyman.goto(0, 0)
    
    
    if lives == 0:
        score = 0
        lives = 3
        pen.clear()
        pen.write('Score: {} Lives {}'.format(score, lives), align='center', font=('Courier', 36))
        time.sleep(1)
        pyman.goto(0, 0)

    
    for pellet in pellets:
        if pyman.distance(pellet) < 10:
            score += 1
            pen.clear()
            pen.write('Score: {} Lives {}'.format(score, lives), align='center', font=('Courier', 36))
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            pellet.goto(x, y)
            
    #Ghouls and Border
    for ghoul in ghouls:
        if ghoul.xcor()>300 or ghoul.xcor()<-300 or ghoul.ycor()>300 or ghoul.ycor()<-300:
             x = random.randint(-280, 280)
             y = random.randint(-280, 280)  
             ghoul.goto(x,y)
             ghoulMovement()
    
# Pyman and Ghouls
    for ghoul in ghouls:
        if pyman.distance(ghoul) < 10:
            lives -= 1
            pen.clear()
            pen.write('Score: {} Lives {}'.format(score, lives), align='center', font=('Courier', 36))
            time.sleep(1)
            pyman.goto(0,0)
            
    
    movement()
    ghoulMovement()

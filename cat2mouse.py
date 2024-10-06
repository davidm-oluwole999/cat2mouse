#make a similar game. Could be a Ash and Pickachu game where the Ash tries to catch the Pickachu and score points
import pgzrun
from random import randint

#size of screen
WIDTH= 600
HEIGHT= 500

#charactars in the game
cat= Actor("cat")
cat.pos= 100,100

mouse= Actor("mouse")
mouse.pos= 200,200

#scoring system
score= 0
game_over = False

#create characters
def draw():
    screen.blit("background",(0,0))
    cat.draw()
    mouse.draw()
    screen.draw.text("Score "+ str(score), color="black", topleft= (10,10))

    #end screen
    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's up! Your final score  "+ str(score), midtop= (WIDTH/2,10), fontsize=40, color="red")

#character placement
def place_mouse():
    mouse.x= randint(70, WIDTH-70)
    mouse.y= randint(70, HEIGHT-70)

#timer
def time_up():
    global game_over
    game_over= True

#movement/ how to score
def update():
    global score
   
    if keyboard.left:
        cat.x=cat.x-2
    if keyboard.right:
        cat.x=cat.x+2
    if keyboard.up:
        cat.y=cat.y-2
    if keyboard.down:
        cat.y=cat.y+2

    if cat.colliderect(mouse):
        score=score+10
        place_mouse()

clock.schedule(time_up, 30.0)
pgzrun.go()
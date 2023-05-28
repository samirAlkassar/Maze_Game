import math
import turtle
import random
import winsound
import time
#creating turtle screen
wn=turtle.Screen()
wn.bgcolor('white')
wn.title("Mze Game")
wn.setup(700,710)
wn.tracer(0)
wn.bgpic("background (1).gif")

#background music
winsound.PlaySound('mixkit-ominous-drums-227.wav',winsound.SND_ASYNC)

#----------------------------------------------------------------------------------
#all images registers....
#----Note---(i draw all of this my self using piskel)
turtle.register_shape("treature_map.gif")
turtle.register_shape("player_left.gif")
turtle.register_shape("player.gif")
turtle.register_shape("box.gif")
turtle.register_shape("brick.gif")
turtle.register_shape("background (1).gif")
turtle.register_shape("brike_block_up.gif")
turtle.register_shape("btike_block_down.gif")
turtle.register_shape("brike_block_right.gif")
turtle.register_shape("btike_block_left.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("text.gif")
turtle.register_shape("helthbar1.gif")
turtle.register_shape("helthbar2.gif")
turtle.register_shape("helthbar3.gif")
turtle.register_shape("helthbar4.gif")
turtle.register_shape("helthbar5.gif")
turtle.register_shape("helthbar6.gif")
turtle.register_shape("helthbar7.gif")
turtle.register_shape("helthbar8.gif")
turtle.register_shape("helthbar9.gif")
turtle.register_shape("helthbar10.gif")
turtle.register_shape("helthbar11.gif")
turtle.register_shape("helthbar12.gif")
turtle.register_shape("helthbar13.gif")
turtle.register_shape("helthbar14.gif")
turtle.register_shape("helthbar15.gif")
turtle.register_shape("heart.gif")
#brike_block texture
turtle.register_shape("brike_block_upleft.gif")
turtle.register_shape("btike_block_downleft.gif")
turtle.register_shape("brike_block_upright.gif")
turtle.register_shape("brike_block_downright.gif")
turtle.register_shape("brike_block_middle.gif")



#-----------------------------------------------------------------------------------

#pen class
class Pen(turtle.Turtle):
    def __init__ (self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
class grass(turtle.Turtle):
    def __init__ (self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color("green")
        self.penup()
        self.speed(0)        


#player class
class Player(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("player.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0
        self.goto(x,y)
        self.x=x
        self.y=y
#player movement
    def go_up(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        if (move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y) 
            winsound.PlaySound('mixkit-quick-jump-arcade-game-239.wav',winsound.SND_ASYNC)       
    def go_down(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        if (move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)
            winsound.PlaySound('mixkit-quick-jump-arcade-game-239.wav',winsound.SND_ASYNC)
    def go_left(self):
        move_to_x=player.xcor()-24
        move_to_y=player.ycor()
        if (move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("player_left.gif")
            winsound.PlaySound('mixkit-quick-jump-arcade-game-239.wav',winsound.SND_ASYNC)  
    def go_right(self):
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        if (move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)
            self.shape("player.gif")
            winsound.PlaySound('mixkit-quick-jump-arcade-game-239.wav',winsound.SND_ASYNC)  
    def is_collision(self,other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))
        if distance<5:
            return True
        else:
            return False                       

#the treature class
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("treature_map.gif")
        self.color("gold")
        self.penup()
        self.gold=100
        self.speed(0)
        self.goto(x,y)
    def destroy(self):
        self.goto(200,200)
        self.hideturtle()
    def update(self,x,y):
        self.x=x
        self.y=y    
#enemies class
class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("enemy.gif")
        self.color("red")
        self.penup()
        self.gold=25
        self.speed(0)
        self.goto(x,y)
#enemies random movement generator
        self.direction=random.choice(["up","down","left","right"])
    def destroy(self):
        self.goto(200,200)
        self.hideturtle() 
    def move(self):
        if self.direction=="up":
            dx=0
            dy=24 
        elif self.direction=="down":
            dx=0
            dy=-24 
        elif self.direction=="right":
            dx=24
            dy=0
        elif self.direction=="left":
            dx=-24
            dy=0
            self.shape("enemy.gif")
        else:
            dx=0
            dy=0    
        move_to_x=self.xcor()+dx
        move_to_y=self.ycor()+dy
        if (move_to_x,move_to_y)not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction=random.choice(["up","down","left","right"])
        turtle.ontimer(self.move,t=random.randint(100,300))
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


    
    
        


#create levels list
levels=[""]
#maze list
level_1=[
"ggggggggggggggggggggggggg",
"m kddddddddddl Bqmmr Eqmm",
"m               qmmr  qmm",
"m E             qmmr  qmm",
"muuuuuup  ggggggkddl  kdm",
"mmmmmmmr  xxx           q",
"mmdddddl  xxxt          q",
"mr        xxxggggggggg gm",
"mr        xxxxxxxgxxgg  q",
"mr   ggg                g",
"mr   iupt               g",
"mr   qmmuuuuuuuuuuup  igg",
"mr     E   gggmmmmmr  qgg",
"mr         gggmmmmmr  qgg",
"mmp  ggggggggggggggl  qmg",
"mmr  xxxx             qmg",
"mmr  xxxx             qmg",
"mmr  xxxxx  iuuuuuuuuummg",
"mmr  xxxxx  kdddmmmmmmmmm",
"mmrg   xxx      gggggmmmm",
"mmr    xxx          ggmmm",
"mmmgg  xxxggggggggg  ggmm",
"mmddl  xxxxxxx  xxxg  gmm",
"ml     xxxxxxx  xxxx  gmm",
"rt E ggxxxxxxx        gmm",
"mggggxxxxxxxxx  gggggggmm",
"mmmmmmmmmmmmmm  mmmmmmmmm",
"ggggggggggggggggggggggggg",
]

treatures=[]
enemies=[]
levels.append(level_1)
#drawing the maze
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            xscreen=288
            screen_x=-xscreen+(x*24)
            yscreen=288
            screen_y=yscreen-(y*24)
            if character=="x":
                pen.goto(screen_x,screen_y)
                pen.shape("brick.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character=="g":
                pen.goto(screen_x,screen_y)
                pen.shape("box.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))    
            if character=="B":
                player.goto(screen_x,screen_y) 
            if character=="t":
                treatures.append(Treasure(screen_x,screen_y))
            if character=="E":
                enemies.append(Enemy(screen_x,screen_y))
            if character=="u":
                pen.goto(screen_x,screen_y)
                pen.shape("brike_block_up.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character=="d":
                pen.goto(screen_x,screen_y)
                pen.shape("btike_block_down.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))  
            if character=="q":
                pen.goto(screen_x,screen_y)
                pen.shape("btike_block_left.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))   
            if character=="r":
                pen.goto(screen_x,screen_y)
                pen.shape("brike_block_right.gif")
                pen.stamp()
                walls.append((screen_x,screen_y)) 
#assets
            if character=="p":
                pen.goto(screen_x,screen_y)
                pen.shape("brike_block_upright.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character=="l":
                pen.goto(screen_x,screen_y)
                pen.shape("brike_block_downright.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character=="i":
                pen.goto(screen_x,screen_y)
                pen.shape("brike_block_upleft.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character=="k":
                pen.goto(screen_x,screen_y)
                pen.shape("btike_block_downleft.gif")
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character=="m":
                pen.goto(screen_x,screen_y)
                pen.shape("brike_block_middle.gif")
                pen.stamp()
                walls.append((screen_x,screen_y)) 
#adding health_bar
def helth():
    healthbar=turtle.Turtle()
    healthbar.up()
    healthbar.goto(-160,273)
    if heart==100:
        healthbar.shape("helthbar1.gif")
    elif heart==95:
        healthbar.shape("helthbar2.gif") 
    elif heart==90:
        healthbar.shape("helthbar3.gif")  
    elif heart==85:
        healthbar.shape("helthbar4.gif")  
    elif heart==80:
        healthbar.shape("helthbar5.gif")  
    elif heart==75:
        healthbar.shape("helthbar6.gif")
    if heart==70:
        healthbar.shape("helthbar7.gif")
    elif heart==60:
        healthbar.shape("helthbar8.gif") 
    elif heart==50:
        healthbar.shape("helthbar9.gif")  
    elif heart==55:
        healthbar.shape("helthbar10.gif")  
    elif heart==40:
        healthbar.shape("helthbar11.gif")  
    elif heart==35:
        healthbar.shape("helthbar12.gif")
    if heart==30:
        healthbar.shape("helthbar13.gif")
    elif heart==20:
        healthbar.shape("helthbar14.gif") 
    elif heart==10:
        healthbar.shape("helthbar15.gif")
hert=turtle.Turtle()
hert.up()  
hert.shape("heart.gif")
hert.goto(-270,326)                          
heart=100

pen=Pen()  
player=Player(0,0)  
walls=[]
setup_maze(levels[1])
sprites = []
turtle.listen()
turtle.onkeypress(player.go_left,"Left")
turtle.onkeypress(player.go_right,"Right")
turtle.onkeypress(player.go_up,"Up")
turtle.onkeypress(player.go_down,"Down")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)
text=turtle.Turtle()
text.shape("text.gif")
text.up()
text.goto(180,225)


#=======================================================================#
#main game loop
while True:
    helth()

    for trearure in treatures:
        if player.is_collision(trearure):
            player.gold+=trearure.gold
            print("player gold: {}",format(player.gold))
            trearure.destroy()
            treatures.remove(trearure)
            winsound.PlaySound('mixkit-video-game-mystery-alert-234.wav',winsound.SND_ASYNC)  

    for enemy in enemies: 
        if player.is_collision(enemy):
            print("-10")
            heart=heart-10
            winsound.PlaySound('mixkit-small-hit-in-a-game-2072.wav',winsound.SND_ASYNC)  
        if heart<=0:
            winsound.PlaySound('mixkit-wrong-answer-fail-notification-946.wav',winsound.SND_ASYNC)
            turtle.done()
            print ("Game Over")   
             
#update the screen 
    wn.update()
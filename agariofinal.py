import turtle
from turtle import *
import time
import random
import pygame
import math
global timeScore
global score 
score = 0

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		# self.x = x
		# self.y = y
		self.goto(x, y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.penup()
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)

	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		top_side_ball=new_y+self.r
		bottom_side_ball=new_y-self.r
		self.goto(new_x,new_y)
		# self.x = new_x
		# self.y = new_y

		if top_side_ball > screen_height:
			self.dy = -self.dy
		

		elif bottom_side_ball < -screen_height:
			self.dy = -self.dy
		

		elif left_side_ball < -screen_width:
			self.dx = -self.dx
		
		elif right_side_ball > screen_width:
			self.dx = -self.dx
			

tracer(0,0)
hideturtle()


RUNNING=True 
SLEEP=0.0077
SCREEN_WIDTH=int(getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(getcanvas().winfo_height()/2)
SCORE_SIZE = 15
SCORE_TYPE = "bold"
SCORE_COLOR = "red"

turtle.pu()
turtle.goto(0,SCREEN_HEIGHT-50)
turtle.write("WHATEVER", move=False , align="right" , font=("Arial", 16 , "bold"))
turtle.goto(SCREEN_WIDTH -50, SCREEN_HEIGHT-50)
turtle.write("Score:"+str(score), move=False , align="right" , font=("Arial", 16 , "bold"))

turtle.bgpic('smoke.1.gif')


pygame.init()
pygame.mixer.music.load("Happier.mp3")
pygame.mixer.music.play()

MY_BALL=Ball(12,12,10,15,23,"blue")

NUMBER_OF_BALLS=15
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=30
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5

BALLS=[]


for i in range(NUMBER_OF_BALLS):
	x= random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy= random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while x>-70 and x<70:
		x=random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	while y>-70 and y<70:
		y= random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	while dx==0:
		dx= random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius= random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color=(random.random(), random.random(), random.random())
	ball1=Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball1)


def move_all_balls():
	for b in BALLS :
		b.move(SCREEN_WIDTH,SCREEN_HEIGHT)
def hide_all_balls():
	for b in BALLS:
		b.hideturtle()


def collide(ball_a,ball_b):
	
	if ball_a==ball_b:
		return False
	distance = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(), 2)+math.pow(ball_a.ycor()-ball_b.ycor(), 2))
	if(distance + 10 < ball_a.r +ball_b.r):
		return True
	else:	
		return False
		
		

def check_all_balls_collision():
	for ball_a in (BALLS):
		for ball_b in (BALLS):
			if collide(ball_a,ball_b)==True:
				ball_a_radius=ball_a.r
				ball_b_radius=ball_b.r	
				X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
				Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
				X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
				Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
				while X_AXISSPEED or Y_AXISSPEED == 0:
					X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
					Y_AXISSPEED = random.randint( MINIMUM_BALL_DY , MAXIMUM_BALL_DY )

				radius =random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)

				color = (random.random(),random.random(),random.random())
					
				if ball_a.r  > ball_b.r:
					ball_b.r = radius
					ball_b.goto(X_COORDINATE, Y_COORDINATE)
					ball_b.dx = X_AXISSPEED
					ball_b.dy = Y_AXISSPEED
					ball_a.r = ball_a.r+2
					ball_b.color(color)
					ball_b.shapesize(ball_b.r/10)
					ball_a.shapesize(ball_a.r/10)
				else:

					ball_a.r = radius
					ball_a.goto(X_COORDINATE, Y_COORDINATE)
					ball_a.dx = X_AXISSPEED
					ball_a.dy = Y_AXISSPEED
					ball_a.color(color)
					ball_a.shapesize(ball_a.r/10)
					ball_b.r = ball_b.r+2
					ball_b.shapesize(ball_b.r/10)

 

def check_myball_collision():
	global score
	for ball in BALLS:
		if collide(MY_BALL,ball) == True:
			ball_r4 = ball.r 
			my_ball_r4 = MY_BALL.r
			X_COORDINATE=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
			Y_COORDINATE=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS)
			X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			while X_AXISSPEED and Y_AXISSPEED == 0:
				X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DY)
				Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			

			color = (random.random(),random.random(),random.random())
			

			if my_ball_r4 > ball_r4:
				score = score + 2

				ball.r = radius
				ball.x = X_COORDINATE
				ball.y = Y_COORDINATE
				ball.goto(X_COORDINATE, Y_COORDINATE)
				ball.dx = X_AXISSPEED
				ball.dy = Y_AXISSPEED
				ball.color(color)
				ball.shapesize(ball.r/10)
				MY_BALL.r = my_ball_r4 + 2
				MY_BALL.shapesize(MY_BALL.r/10)
				turtle.undo()
				turtle.write("Score:"+str(score), move=False , align="right" , font=("Arial", 16 , "bold"))
				turtle.update()

			else:
				turtle.goto(0,0)
				turtle.write("YOU LOST!!", move=False , align="center" , font=("Arial", 16 , "bold"))
				hide_all_balls()
				return False

	return True		


def movearound(event):
	X = event.x - round(SCREEN_WIDTH)
	Y = round(SCREEN_HEIGHT) - event.y
	MY_BALL.goto(X,Y)

turtle.getcanvas().bind("<Motion>" , movearound)
turtle.listen()
'''
def check():

	check_all_balls_collision()
	check_myball_collision()

	if MY_BALL.xcor() == new_ball.xcor() or MY_BALL.ycor()==newballs.ycor():
		x = randon.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,  SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
		Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
'''
global timescore
timescore = 0
timewrite = turtle.Turtle()
timewrite.ht()
start = time.time()
def timer():
	global timescore
	timescore = int(time.time()-start)
	timewrite.goto(200,350)
	timewrite.clear()
	timewrite.write(" Time : " + str(timescore),move=False , align="left" , font=("Arial",16,"bold"))



while RUNNING == True:
	move_all_balls()
	check_all_balls_collision()
	if check_myball_collision() == False :
		RUNNING = False
	if score >=10:
		turtle.goto(0,0)
		turtle.write("YOU WON!!",move=False , align="center" , font=("Arial", 20 , "bold"))
		hide_all_balls()
		pygame.mixer.music.play()

		RUNNING=False
	SCREEN_WIDTH=int(getcanvas().winfo_width()/2)
	SCREEN_HEIGHT=int(getcanvas().winfo_height()/2)

	timer()
	turtle.update()
	time.sleep(0.01)
'''

def timerDisplay():
	global timeScore
	timeScore = int(time.clock() * 1.5)
	timeWrite.goto(-SCREEN_WIDTH + 10 , SCREEN_HEIGHT - 30)
	timeWrite.clear()
	timeWrite.write("Time: " + str(timeScore), False , "left" , (TIME_FONT_NAME) , )
	'''


turtle.mainloop()
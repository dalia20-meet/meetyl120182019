from turtle import *
import random
import time

colormode(255)
#tracer(0)
hideturtle()

SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HIGHT = getcanvas().winfo_height()/2

right_side_ball = 0
left_side_ball = 0
up_side_ball = 0
down_side_ball = 0
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)


		def random_color(self):
			r =random.randint(0,255) 

			g =random.randint(0,255) 

			b =random.randint(0,255)

			self.color(r,g,b)

	def move (self,width,hight):
		current_x = self.xcor()
		new_x= current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy 
		global right_side_ball
		global left_side_ball
		global up_side_ball
		global down_side_ball
		right_side_ball= new_x + self.radius
		left_side_ball = new_x - self.radius
		up_side_ball = new_y + self.radius
		down_side_ball = new_y- self.radius
		self.goto(new_x,new_y)
		if new_x == right_side_ball:
			self.dx = -self.dx

		if new_x == left_side_ball:
			self.dx = -self.dx

		if new_y == up_side_ball:
			self.dy = -self.dy

		if new_y == down_side_ball:
			self.dy = -self.dy		
	
mainloop()

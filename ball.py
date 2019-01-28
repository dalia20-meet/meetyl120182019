from turtle import *
import random
import time

class Ball(Turtle):
	def __init__(self,x ,y ,dx ,dy , radius):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
				
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))

	def move(self , width, height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		left_side = new_x - self.radius
		Right_side = new_x + self.radius
		top_side = new_y + self.radius
		bottom_side = new_y -self.radius
		self.goto(new_x,new_y)
		if top_side >= height:
			self.dy = -self.dy

		elif bottom_side <= -height:
			self.dy = -self.dy

		elif Right_side >= width:
			self.dx = -self.dx

		elif left_side <= -width:
			self.dx = -self.dx
	
		






mainloop()

import turtle
from turtle import Turtle
import math
import random
turtle.tracer(0)
class Ball(Turtle):
	def __init__(self, radius, dx, dy, color):
		Turtle.__init__(self)
		self.shape("circle")
		self.radius=radius
		self.dx=random.randint(20,40)/40
		self.dy=random.randint(30,50)/40
		self.shapesize(radius/10)
		self.color(color)
	def move(self,width,height):
		oldx=self.xcor()
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		if newx >= width or newx <= -width:
			self.dx= -self.dx
			newx=oldx + self.dx
		if newy>= height or newy<= -height:
			self.dy= -self.dy
			newy=oldy + self.dy
		self.goto(newx,newy)


ball2=Ball(20,3,3,"blue")		
ball1=Ball(20, 5, 5, "pink")

def check_collision(ball1, ball2):
	x2=ball1.xcor()
	x1=ball2.ycor()
	y2=ball1.xcor()
	y1=ball2.ycor()
	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if ball1.radius + ball2.radius >= D:
		return True
	else:
		return False

	
while True:
	ball1.penup()
	ball1.move(300,300)	
	ball2.penup()
	ball2.move(300,300)
	if check_collision(ball1,ball2):
		print("we have a collision")
	turtle.update()


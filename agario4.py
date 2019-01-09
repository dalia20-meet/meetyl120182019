from turtle import Turtle
import turtle
import random

class  Ball(Turtle):
	def __init__(self,x,y,dx,r,color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		turtle.penup()
		self.goto(x,y)
		self.shape("circle")
		turtle.goto(x,y)
		self.shapesizer(r/10)


	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = (current_x + self.dx)

		current_y = self.ycor()
		new_y = (current_y + self.dy)
		right_side_ball = (new_x + self.r)
		left_side_ball = (new_x - self.r)
		upper_side_ball = (new_y + self.r)
		bottom_side_ball = (new_y - self.r)

		self.goto(new_x)
		self.goto(new_y)
dalia= Ball(0,0,0,0,100,"blue")

turtle.mainloop()

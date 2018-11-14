import turtle

import random
turtle.colormode(255)
from turtle  import Turtle

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		R = random.randrange(0,257,10)
		G = random.randrange(0,257,10)
		B = random.randrange(0,257,10)

		self.color(R,G,B)
Square1 = Square(3)


Square1.random_color()

class Hexagon(Square):
	pass


turtle.mainloop()
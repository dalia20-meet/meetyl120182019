import turtle

import random
turtle.colormode(255)
from turtle  import Turtle
'''
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
'''
class Hexagon(Turtle):
	def __init__ (self,x):
		Turtle.__init__ (self)
		turtle.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,x*2),(x,3*x),(0,3*x),(-x,2*x),(-x,x),(0,0)))
		self.shape("Hexagon")
H = Hexagon(20)

turtle.mainloop()


	
	

'''
class Hexagon(T):
	def __init__(self,x):
		Turtle.__init__ (self)
		turtle.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,x*2),(x,3*x),(-x,2*x),(-x,x),(0,0)))

	
	

'''
turtle.mainloop()
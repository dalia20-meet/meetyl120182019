
import turtle
import random
from turtle import Turtle
turtle.colormode(255)

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		R = random.randrange(0, 257, 10)
		B = random.randrange(0, 257, 10)
		G = random.randrange(0, 257, 10)

		self.color(R, G, B)
square1 = Square(3)

square1.random_color()

# class Rectangle(Square):
# def __init__(self,width,height)
# self.width = width
# self.height = height
class Hexagon(Turtle):
	def __init__ (self,x):
		Turtle.__init__(self)
		turtle.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,x*2),(x,3*x),(0,3*x),(-x,2*x),(-x,x),(0,0)))
		self.shape("Hexagon")
H = Hexagon(20)
turtle.mainloop()


"""
class Hexagon(Turtle):
	Turtle.__init__ (self,x):
		self.register_shape("Hexagon",((0,0),(x,0),(2*x,x),(2*x,x*2),(x,3*x),(0,3*x),(-x,2*x),(-x,x),(0,0)))
		self.shape("Hexagon")
H = Hexagon(20)
"""

	



	
	
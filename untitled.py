
from turtle import Turtle
import turtle
import random
turtle.colormode(255)
class Square(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape('square')
	def random_color(self):

		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)

		self.color(r,g,b)
s=Square(5)
s.random_color()
turtle.mainloop()
'''

from turtle import Turtle
import turtle
turtle.begin_poly()
turtle.register_shape("strawberry",(turtle.get_poly()))
import turtle
turtle.pu()
turtle.forward(50)
for i in range (6):
	turtle.pd()
	turtle.right(60)
	turtle.forward(50)
turtle.mainloop()
turtle.end_poly()
class Hexagon(Turtle):
	def __init__(self,size):
		self.shapesize(size)
		self.shape(strawberry)

c=Hexagon(200)
turtle.mainloop()


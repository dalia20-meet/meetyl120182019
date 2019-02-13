import turtle
from turtle import Turtle





turtle.register_shape("CharacterLeft.gif")
turtle.shape("CharacterLeft.gif")
turtle.pu()
turtle.goto(100,100)

OBSTICLES_LIST = []
global new_obsticle
class obsitcles(Turtle):
	def __init__(self,x,y,dx):
		Turtle.__init__(self)
		self.pu()
		self.x = x
		self.y = y
		self.dx = x
		self.shape("square")
		self.hideturtle()
		self.goto(self.x,self.y)
		self.showturtle()

	def move(self):
		x=self.xcor()
		y=self.ycor()
		self.goto(x-2,y)

	def make_obsticles(self, OBSTICLES_LIST):
		self.y = random.randint(-500,500)
		new_obsticle = obsitcles(500,self.y,5)
		OBSTICLES_LIST.append(new_obsticle)
		new_obsticle.move()
		
obsticle_1 = obsitcles(500,300,5)
		
while True:	
	obsticle_1.move()
	new_obsticle.make_obsticles()












































































turtle.mainloop()
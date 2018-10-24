import turtle
'''
turtle.addshape("car.gif")
turtle.goto(0,0)
turtle.shape("car.gif")
turtle.mainloop()
'''
for i in range(3000):
	turtle.speed(0)
	turtle.forward(200)
	turtle.left(300)
	turtle.forward(75)
	turtle.right(100)
	turtle.forward(20)
	turtle.right(30)
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.left(i+30) 
turtle.mainloop()	

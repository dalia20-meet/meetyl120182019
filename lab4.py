class Animal(object):
	def __init__ (self,sound,name,age,favorite_color,food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color

	def eat(self,food):
		print("yummy!! " + self.name + "is eating" +food)
	def description(self):
		print(self.name + "is" + str(self.age) +"years old and loves the color"+self.favorite_color)
	def make_sound(self):
		for i in range(3):
			print(self.sound)

a = Animal("Barking","dog",3,"blue","dog food")
a.make_sound()
a.description()
a.eat("dog food")

class Person(object):
	def __init__ (self,name,age,city,gender,height,favorite_food):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.height = height
		self.favorite_food = favorite_food
	def eat(self):
		print(self.name +"is eating" + self.favorite_food)
	def discription(self):
		print(self.name + "is"+ str(self.age) + "years old.She lives in "+ self.city)
b = Person("Dalia",15,"Jerusalem","female",160,"cereal")
b.eat()
b.discription()		
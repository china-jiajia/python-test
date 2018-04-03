
class Animal():
	def shout(self):
		print('旺旺叫')
	def eat(self):
		pass

class Dog(Animal):
	pass

class Taidi(Dog):
	pass

class Cat(Animal):
	def shout(self):
		print("喵喵叫")

dog=Dog()
cat = Cat()
cat.shout()

dog.shout()
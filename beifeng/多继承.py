
class Animal():
	def shout(self):
			print('喵喵叫')
	def eat(self):
		pass

class Dog():
	def shout(self):
		print('旺旺叫')


class Taidi(Animal,Dog):
	pass


taidi=Taidi()
taidi.shout()
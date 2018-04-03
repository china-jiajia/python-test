
class Person():
	def __eat(self):
		print("这是私有方法:__eat()")

	def get_eat(self):
		self.__eat()


xiaoming=Person()
xiaoming.get_eat()
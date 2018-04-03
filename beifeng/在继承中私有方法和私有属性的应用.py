
class Person():
	def __int__(self):
		self.__name="小明"
		self.age=10
		
	def test1(self):
		print("----------test1----------")
		

	def __test2(self):
		print("----------test2----------")
		

	def test3(self):
		self.__name
		self.__test2()
		

class xiaoming(Person):
	pass

	# def test3(self):
	# 	self.__name 	私有属性不能够被继承
	# 	self.__test2()	私有方法不能够被继承
		

xiaoming1=xiaoming()
xiaoming1.test3()
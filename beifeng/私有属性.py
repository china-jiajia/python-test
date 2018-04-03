# class Person():
# 	def __int__(self):
# 		self.__name="小明"


# 	def set_age(self,new_age):
# 		if new_age>0 and new_age<100:
# 			self.age=new_age
# 		else:
# 			self.age=18

# 	def get_age(self):
# 		return self.age 



# xiaoming = Person()
# # xiaoming.age=10
# xiaoming.set_age(19)
# age=xiaoming.get_age()
# print(xiaoming.name)
# print(xiaoming.age)


class Person():
	def set_age(self,new_age):
		if new_age>0 and new_age<100:
			self.age=new_age
		else:
			self.age=18

	def get_age(self):
		return self.age
		


xiaoming = Person()
# xiaoming.age=-18
xiaoming.set_age(-10)
age=xiaoming.get_age()
print(xiaoming.age)

class Animal():
		# 类属性
		num=0
		# 类型.num
		# 实例方法
		def __in__(self):
			# 实例属性
			self.name="小明"
			
		@classmethod 	#类方法
		def test1(cls):
			# Animal.num=100
			cls.num=100
			print(cls.num)

		@staticmethod 	#静态方法
		def test2():
			print("----------欢迎进入宠物管理系统---------")
			


animal=Animal()
animal.test2()
Animal.test2()
animal.test1()
Animal.test1()			
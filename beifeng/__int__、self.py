
class Animal():
	# 属性: 种类、姓名、叫声
	def __init__(self,types,name,shouts):		#初始化
		self.name=name
		self.types=types
		self.shouts=shouts


	# 方法: 叫，跑
	def shout(self):
		print("%s,%s,%s"%(self.types,self.name,self.shouts))


dog1=Animal('泰迪','小黑','旺旺叫')
dog1.shout()
cat1=Animal('波斯','小黄','喵喵叫')
cat1.shout()





__init()__是一个特殊的方法，方法的前面和后面都两个下划线.这是为了避免Python默认方法和普通方法发生名称的冲突.每当
创建类的实例的时候,__init__()方法都会默认被运行.作用就是初始化已实例化后的对象

在方法定义中,第一个参数self是必不可少的.类的方法和普通的函数的区别就是self，self并不是Python的关键字,完全可以使用其他
单词取代它,只是按照惯例和标准的规定,推荐使用self

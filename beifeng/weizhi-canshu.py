

def animal(pet1,pet2):
	print(pet1,'汪汪叫',pet2,'喵喵叫')

# 位置传递参数
animal('小狗','小猫')

# 对应传参 	这样会比位置传参会更加准确些
animal(pet1='小狗',pet2='小猫')
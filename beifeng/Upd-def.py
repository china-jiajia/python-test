
# 形参数:	形式参数
# 实参数:	实际参数

# 定义列表
students=['amy','tom','john']

# 定义函数
def Updstudent(student):
	student[2]='小明'
	print('修改前的列表为:',student)


# 引用函数
Updstudent(students)
print('修改后的列表为:',students)
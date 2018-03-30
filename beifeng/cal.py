# 三个参数: 运算符，数字1，数字2

def cal(flg,num1,num2):
	if flg=='+':
		return num1+num2
	elif	flg=='-':
		return num1-num2
	elif	flg=='*':
		return num1*num2
	elif	flg=='/':
		return	num1/num2
	else:
		return 	'您输入的运算符不合法!'


num1=int(input('请输入要进行计算的第一个数字:'))
flg=input('输入您要做的算数运算符:')
num2=int(input('请输入要进行计算的第二个数字:'))


# cal(flg,num1,num2)

calcultion=cal(flg,num1,num2)
print(calcultion)



# totla=cal('/',10,50)
# print(totla)


count = 0

while  count < 3:
	user = input('请输入用户名:',)
	pwd = input('请输入密码:',)
	if user == 'root' and pwd == 'tJJ199005':
		print('欢迎登陆系统')
		break
	else:
		print('您输入的用户名或密码错误,请重新输入')
	count = count +1
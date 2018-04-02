#-*-UTF-8-*-
# 99乘法表

for i  in range(1,10):
	for n in range(1,i+1):
		print("%s*%s=%s" %(n,i,i*n),end=' ')			#print默认后面跟一个\n换行,end的意思是将最后默认的\n换成end指定的内容
	print()


# for i in range(1,10):
# 	print(i)
# 	for n  in range(1,i+1):
# 		print(n)

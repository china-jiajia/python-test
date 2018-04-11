
n = 1
s = 0

while n < 100:
	temp = n % 2
	if temp == 0:
		s = s - n
	else:
		s = s + n
	n = n + 1
print(s)
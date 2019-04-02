'''
设计一个验证用户密码的程序，用户只有三次机会输入错误，但是如果用户输入的内容包括“*”则不计算在内
'''
password = 'abc1230'
times = 3
while times:
	input_password = input("请输入密码：")
	if '*' in input_password:
		print("密码中不能带*号！")
	else:
		if input_password == password:
			print("密码输入正确！")
			break
		else:
			print("密码输入错误！")
			times -= 1


'''
使用for循环打印以下图案:
* * * * *
*       *
*       *
* * * * *
'''
#外层循环控制行
for i in range(4):
	if i == 0 or i ==3:
		print("* " * 5)
	if i == 1 or i == 2:
		for j in range(5):
			if j == 0 or j == 4:
				print("* ", end="")
			else:
				print("  ", end="")
		print()



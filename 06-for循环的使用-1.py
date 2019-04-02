'''
利用双层for循环打印以下图案：
* * * * *
* * * * *
* * * * *
* * * * *
'''
for i in range(0, 4):
	#利用for循环打印一行*号
	for j in range(0, 5):
		#print自动换行
		#可以利用end参数进行控制
		print("* ", end='')
	print()


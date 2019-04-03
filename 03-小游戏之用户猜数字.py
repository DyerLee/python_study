'''
给用户三次机会A，猜想程序随机生成的数字,每次猜想之后提示数字是否正确以及用户输入数字大于还是小于A，当机会用完，游戏结束！
'''
import random

secret = random.randint(1, 100)

times = 10

while times:	
    tmp = input("请输入数字：")
    num = int(tmp)
    if num == secret:
        print("恭喜你，猜对了！！")
        break
    elif num < secret:
        print("你输入的数字太小了！！")
        times = times -1
    else:
        print("你输入的数字太大了！！")
        times = times -1
print("你的机会用完了！！")


# 产生一个随机整数1~100
# 让使用者重复输入数字去猜
# 猜对的话 印出“终于猜对了”
# 猜错的话 要告诉他 比答案大/小

import random

r = random.randint(1,100) # 产生随机数
while True: # 无限循环游戏次数
	guess_number = input('请输入一个数:') # 让玩家猜数
	guess_number = int(guess_number) # 型转换方便对比
	if guess_number == r:
		print('恭喜你 猜对了')
		break # 答案正确 终止循环
	else:
		if guess_number > r:
			print('猜的数字有点大哦 再试一遍吧')
		else:
			print('猜的数字有点小哦 再试一遍吧')
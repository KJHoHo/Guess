# 产生一个随机整数1~100
# 让使用者重复输入数字去猜
# 猜对的话 印出“终于猜对了”
# 猜错的话 要告诉他 比答案大/小

import random
little_num = input('你希望随机范围从什么数字开始?')
little_num = int(little_num)
big_num = input('你希望最大的随即数是？')
big_num = int(big_num)
r = random.randint(little_num,big_num) # 产生随机数
count = 0 # 初始化猜谜次数
while True: # 无限循环游戏次数
	count = count + 1
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

print('你总共猜了' + str(count) + '次')
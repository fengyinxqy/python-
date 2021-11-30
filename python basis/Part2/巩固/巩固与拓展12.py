""" 
思路：
    先找出100~2000之间所有的素数，然后从倒数第一个开始输出10个即可
"""
sushu = []
for i in range(100, 2001):
    for j in range(2, i):
        if i % j == 0:
            break
    if i == j+1:
        sushu.append(i)
print(sushu[-10:])

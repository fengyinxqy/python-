m = int(input("请输入一个整数:"))
n = int(input("请输入一个整数:"))
sum = 0
for i in range(m, n+1):
    if i < 10:  # 小于10的数字直接判断是否为奇数
        if i % 2 != 0:
            sum += i
    else:  # 大于10的数字分两种情况讨论
        if i % 2 != 0:  # 对2求余不为0的即合在一起为奇数的如11,13
            sum += i % 10
            i = i//10  # 分离数字
            if i % 2 != 0:  # 判断分离后的数字
                sum += i
        else:           # 对2求余为0的即合在一起为偶数的如10,12
            i = i//10  # 个位数不管，直接分离
            if i % 2 != 0:
                sum += i
print(sum)

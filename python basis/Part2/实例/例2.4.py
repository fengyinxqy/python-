num1 = int(input("请输入一个整数:"))
num2 = int(input("请输入一个整数:"))
if num1 < num2:
    t = num1
    num1 = num2
    num2 = t
print("从大到小为:%d,%d" % (num1, num2))

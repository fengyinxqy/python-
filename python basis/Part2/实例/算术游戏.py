import sys
import random
for i in range(3):
    psd = input("请输入密码")
    if psd.strip(" ") == "123":
        break
    else:
        if(i == 2):
            print("密码错误3次,程序停止运行!")
            sys.exit(1)
        else:
            print("密码错误,请重新输入!")
signs = ['+', '-', '*', '//']
right = 0
error = 0
for i in range(10):
    op1 = random.randint(0, 100)
    op2 = random.randint(0, 100)
    sign = random.choice(signs)
    if sign == '+':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1+op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1+op2))
            error += 1
    elif sign == '-':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1-op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1-op2))
            error += 1
    elif sign == '*':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1*op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1*op2))
            error += 1
    if sign == '//':
        print(str(op1)+sign+str(op2)+"=", end=' ')
        answer = int(input())
        if answer == op1//op2:
            print("恭喜你答对了!")
            right += 1
        else:
            print("很遗憾答错了!")
            print("正确答案是:%d" % (op1//op2))
            error += 1
print("答对的次数: ", right, "答错的次数: ", error)

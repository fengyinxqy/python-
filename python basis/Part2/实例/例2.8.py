key = "1234xyz"
password = input("请输入密码:")
for i in range(1, 6):
    if password == key:
        print("欢迎使用本系统!")
        break
    else:
        if i < 5:
            print("密码错误！还剩%d次机会！" % (5-i))
            password = input("请重新输入:")
        else:
            print("密码错误，次数用完，请下次再试！")

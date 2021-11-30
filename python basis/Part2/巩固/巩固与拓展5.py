a, b = eval(input("开始游泳的时间："))
c, d = eval(input("结束游泳的时间："))
minutes = (c-a-1)*60+(60-b)+d
print("小明游了%d小时%d分钟" % (divmod(minutes, 60)[0], divmod(minutes, 60)[1]))

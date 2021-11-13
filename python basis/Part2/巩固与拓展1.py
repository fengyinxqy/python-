score1 = int(input("第一位同学的成绩："))
score2 = int(input("第二位同学的成绩："))
score3 = int(input("第三位同学的成绩："))
avg_score = (float(score1+score2+score3))/3
print("平均成绩:%.2f" % (avg_score))  # 保留两位小数
print("平均成绩:%d" % (round(avg_score)))  # 四舍五入
print("平均成绩:%d" % (int(avg_score)))  # 向下取整

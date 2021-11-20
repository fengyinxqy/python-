score = [[1901, '张三', 80], [1902, '李四', 69], [
    1903, '王二', 70], [1904, '赵六', 68], [1905, '孙七', 58]]
for item in score:
    print(item)
print("******><><******")
while(1):
    print("1.增加一条学生成绩")
    print("2.按照学号删除成绩")
    print("3.全部学生成绩平均值")
    print("4.输出成绩的前三名")
    print("0.Exit")
    choice = int(input("请输入你的选择:").strip(" "))
    if choice == 0:
        break
    elif choice == 1:
        new_score = input("按学号、姓名和成绩的顺序输入一条信息(逗号隔开):\n").strip(" ")
        new_score = new_score.strip(" ").split(",")
        new_score[0] = int(new_score[0])
        new_score[2] = int(new_score[2])
        score.append(new_score)
    elif choice == 2:
        num = int(input("请输入要删除的学号:").strip(" "))
        for item in score:
            if item[0] == num:
                score.remove(item)
                break
    elif choice == 3:
        sum = 0
        for item in score:
            sum += item[2]
        average = sum/len(score)
        print(average)
    elif choice == 4:
        score.sort(key=lambda x: x[2], reverse=True)
        print(score[0:3])
    else:
        print("编号输入错误!")

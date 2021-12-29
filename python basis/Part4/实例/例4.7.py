def add_student():
    new_score = input("按学号、姓名和成绩的顺序输入一条信息(逗号隔开):\n").strip(" ")
    new_score = new_score.strip(" ").split(",")
    new_score[0] = int(new_score[0])
    new_score[2] = int(new_score[2])
    return score.append(new_score)


def del_student():
    num = int(input("请输入要删除的学号:").strip(" "))
    count = len(score)
    for item in score:
        count = count-1
        if item[0] == num:
            score.remove(item)
            print("删除成功!")
            break


def average():
    sum = 0
    for item in score:
        sum += item[2]
    if sum == 0:
        print("学生数据为空!")
    else:
        average = sum/len(score)
        print(average)


def top3(line):
    line = sorted(line, key=(lambda item: item[2]), reverse=True)
    print(line[0:3])


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
    try:
        choice = int(input("请输入你的选择:").strip(" "))
        if choice == 0:
            break
        elif choice == 1:
            add_student()
        elif choice == 2:
            del_student()
        elif choice == 3:
            average()
        elif choice == 4:
            top3(score)
        else:
            print("输入编号错误!")
    except:
        print("请输入数字!")

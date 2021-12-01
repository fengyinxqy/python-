student_xy = []
print("原文件的内容是:")
with open('student.csv', 'r', encoding='gb18030') as data:
    for line in data:
        print(line.strip())
        line = line.strip()
        student_xy.append(line.split('，'))
print("转换成列表后是: ")
print(student_xy)
print("课程的平均成绩是: ")
score = student_xy[1:]
sum = 0
for item in score:
    sum = sum+int(item[2])
average = sum/len(score)
print(average)
print("按照成绩排名是: ")
score = sorted(score, key=(lambda item: int(item[2])), reverse=True)
print(score)
with open('student123.csv', 'w', encoding='utf-8')as data:
    data.write('，'.join(student_xy[0])+'\n')
    for s in score:
        data.write('，'.join(s)+'\n')
print("排序后的新文件内容是: ")
with open('student123.csv', 'r', encoding='utf-8')as data:
    for line in data:
        print(line.strip())

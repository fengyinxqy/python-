import random


class Student(object):
    def __init__(self, name, snum):
        self.name = name
        self.snum = snum
        self.course = []
        self.score = {}

    def choice(self, course):
        for item in course:
            self.course.append(item)

    def exam(self):
        for item in self.course:
            self.score[item] = random.randint(30, 100)

    def OutputScore(self):
        print("课程类\t成绩")
        for key, value in self.score.items():
            print(key, "\t", value)


class course(object):
    cour_info = ["英语", "数学", "计算机", "政治", "哲学", "品德"]

    @classmethod
    def ShuffleCourse(cls):
        random.shuffle(cls.cour_info)

    @classmethod
    def AddCourse(cls, new_course):
        cls.cour_info.append(new_course)

    @classmethod
    def DelCourse(cls, old_course):
        cls.cour_info.pop(old_course)

    @classmethod
    def OutputCourse(cls):
        print("课程名: ", end=' ')
        for item in cls.cour_info:
            print(item, end=' ')
        print("\n")


course.ShuffleCourse()
course.OutputCourse()
s1 = Student("张三", "2021")
n = int(input("请输入选课的门数:"))
if n <= len(course.cour_info):
    s1.choice(random.sample(course.cour_info, n))
    s1.exam()
    s1.OutputScore()
else:
    print("选课门数超过已有课程!")

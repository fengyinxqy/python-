import random


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say1(self):
        print("我叫{},今年{}岁".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, snum, course):
        Person.__init__(self, name, age)
        self.snum = snum
        self.course = course

    def say2(self):
        print(self.course+"课的分数为: "+str(random.randint(80, 100)))


stu1 = Person("张三", 18)
stu2 = Student("李四", 20, "202101", "数学")
stu1.say1()
stu2.say1()
stu2.say2()

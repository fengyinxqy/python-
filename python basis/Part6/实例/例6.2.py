class Person(object):
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say(self):
        print("大家好，我叫"+self.name+"，今年"+str(self.age) + ",职业是:"+self.occupation)

    def judge_occupation(self, work):
        if self.occupation == work.strip(" "):
            print("职业相同")
        else:
            print("职业不同")

    def judge_age(self, age):
        if self.age == age:
            print("年龄相同")
        else:
            print("年龄不同")


Person1 = Person("张三", 20, "教师")
Person2 = Person("李四", 30, "医生")
Person1.say()
Person2.say()
Person1.judge_occupation("律师")
Person2.judge_occupation("医生")
Person2.judge_age(21)

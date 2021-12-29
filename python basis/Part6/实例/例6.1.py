class Person:
    def say(self, name, occupation):
        print("大家好,我叫"+name)
        print("职业是"+occupation)


teacher = Person()
doctor = Person()
teacher.say("张三", "教师")
doctor.say("李四", "医生")

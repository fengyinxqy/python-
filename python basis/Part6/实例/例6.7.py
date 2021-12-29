class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我叫"+self.name)


class Student(Person):
    def __init__(self, name, age, height):
        Person.__init__(self, name)
        self.age = str(age)
        self.height = str(height)

    def say(self):
        print("我叫{},今年{}岁,身高{}cm.".format(self.name, self.age, self.height))


def introduce(obj):
    obj.say()


p1 = Person("张三")
p2 = Student("李四", 20, 180)
introduce(p1)
introduce(p2)

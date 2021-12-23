class Student():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def output(self):
        print("姓名:"+self.name)
        print("学号:"+str(self.number))


Student1 = Student("张三", 1)
Student2 = Student("李四", 2)
Student1.output()
Student2.output()

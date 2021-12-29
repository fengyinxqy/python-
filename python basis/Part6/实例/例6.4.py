class CourseSelect(object):
    credit = 3
    cname = "计算机"

    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 显示课程信息

    def CourseInfo(self):
        print("课程名:"+CourseSelect.cname)
        print("学分为:"+str(CourseSelect.credit))
    # 修改课程学分

    def set_credit(self, n):
        CourseSelect.credit = n
    # 修改课程名称

    @classmethod
    def set_name(cls, c):
        cls.cname = c


if __name__ == "__main__":
    stu1 = CourseSelect("张三", 90)
    stu2 = CourseSelect("李四", 100)
    stu1.CourseInfo()
    stu2.CourseInfo()
    stu2.set_credit(5)
    stu1.CourseInfo()
    stu2.CourseInfo()
    CourseSelect.set_name("英语")
    stu1.CourseInfo()
    stu2.CourseInfo()

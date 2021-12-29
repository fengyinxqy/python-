class Admin(object):
    userlist = []

    def __init__(self, name, password):
        self.__name = "admin"
        self.__password = "admin2010"
        self.IsNameOk(name)  # 检测用户名是否合法
        self.IsPasswordOk(password)  # 检测密码是否合法
    """ 检测账户是否合法 """

    def IsNameOk(self, name):
        if name.strip(" ") != self.__name:
            raise Exception("用户名错误!")

    def IsPasswordOk(self, password):
        if password.strip(" ") != self.__password:
            raise Exception("密码错误!")

    def AddUser(self, user_name, user_pwd):
        Admin.userlist.append([user_name, user_pwd])

    def DeleteUser(self, user_name):
        flag = 1
        for line in Admin.userlist:
            if line[0] == user_name:
                Admin.userlist.remove(user_name)
                flag = 0
                break
        if flag:
            print("该用户名不存在!")

    def ChangePsd(self, user_name, user_password):
        flag = 1
        for line in Admin.userlist:
            if line[0] == user_name:
                Admin.userlist.remove(line)
                flag = 0
                break
        if flag:
            print("该用户不存在!")
        else:
            Admin.userlist.append([user_name, user_password])

    @classmethod
    def PrintUserlist(cls):
        print("用户名\t密码")
        for item in cls.userlist:
            print(item[0], item[1], sep='\t')


if __name__ == "__main__":
    a1 = Admin("admin", "admin2010")
    a1.AddUser("xiaoqiyan", "666888")
    a1.AddUser("zhangsan", "123456")
    a1.ChangePsd("zhangsan", "456")
    a1.PrintUserlist()

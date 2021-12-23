class Login(object):
    def __init__(self):
        self.userlist = self.setvalue()

    def setvalue(self):
        userlist = []
        with open('账号密码.txt', "r", encoding="utf-8")as f:
            for line in f.readlines():
                info = line[:-1].split(",")  # 读取到最后
                userlist.append(info)  # 把它添加到列表中
        return userlist

    def Check(self, name, password):
        flag = 0
        if self.isLegalUser(name, password):  # 如果账号密码位数都在指定的范围
            for line in self.userlist:
                if line[0] == name and line[1] == password:  # 验证账号密码是否一致
                    print("登录成功")
                    flag = 1
                    return flag
            if flag == 0:
                print("用户名或密码错误")
        else:
            print("账号或密码长度非法!")

    def isLegalUser(self, name, password):
        if len(name) >= 3 and len(name) < 16:
            if len(password) >= 3 and len(password) <= 16:
                return True
        return False


if __name__ == "__main__":
    login = Login()
    while(True):
        str_name = input("请输入用户名:")
        str_pwd = input("请输入密码:")
        if login.Check(str_name, str_pwd):
            break

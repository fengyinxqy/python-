class manager(object):
    Acount = "admin"
    password = "2020"

    def __init__(self, Acount, password):
        self.Acount = Acount
        self.password = password

    @classmethod
    def Change(cls, a, p):
        cls.Acount = a
        cls.password = p

    def pnf(self):
        print("账号:"+manager.Acount + " 密码:"+str(manager.password))


manager1 = manager("admin", "2020")
manager1.pnf()
manager.Change("xiaoqiyan", "2001")
manager1.pnf()

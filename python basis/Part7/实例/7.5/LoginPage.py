from tkinter import *
from tkinter.messagebox import *
from MainPage import *
class LoginPage(object):
    def __init__(self,master=None):
        self.root = master
        self.root.geometry('%dx%d'%(500,300))
        self.username=StringVar()
        self.password = StringVar()
        self.createPage()
        
    def createPage(self):
        Label(self.root,text='计算BMI指数',bg='#d3fbfb',fg='red',font=('宋体',25),relief=SUNKEN).pack(fill=X)
        self.page=Frame(self.root)
        self.page.pack()
        Label(self.page, text='账号: ',font=('宋体',12)).grid(row=2,sticky=W,pady=10)
        Entry(self.page,textvariable=self.username).grid(row=2,column=1,sticky=E)
        Label(self.page, text='密码: ',font=('宋体',12)).grid(row=4,sticky=W,pady=10)
        Entry(self.page,textvariable=self.password,show='*').grid(row=4,column=1,sticky=E)
        Button(self.page, text='登录',font=('宋体',10),command=self.loginCheck).grid(row=6,sticky=W,pady=10)
        Button(self.page, text='退出',font=('宋体',10),command=self.root.destroy).grid(row=6,column=1,sticky=E)
    
    def loginCheck(self):
        name=self.username.get()
        password = self.password.get()
        if self.isLegalUser(name,password):
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误',message='账号或密码错误!')
            self.username.set("")
            self.password.set("")
    def isLegalUser(self, name, password):
        with open('python\python basis\Part7\文件\账号密码.txt',"r",encoding="utf-8")as f:
            for line in f.readlines():
                info=line[:-1].split(",")
                if len(info)<2:
                    break
                if info[0].strip()==name and info[1].strip() ==password:
                    f.close()
                    return True
        return False
        
from tkinter import *
from view import *


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry("%dx%d" % (600, 500))
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)
        self.addPage = AddFrame(self.root)
        self.deletePage = DeleteFrame(self.root)
        self.addPage.pack()
        mainmenu = Menu(self.root)
        menuFile = Menu(mainmenu)
        mainmenu.add_cascade(label="文件", menu=menuFile)
        menuFile.add_command(label="导入数据", command=self.inputData)
        menuEdit = Menu(mainmenu)
        mainmenu.add_cascade(label="处理", menu=menuEdit)
        menuEdit.add_command(label="插入数据", command=self.addData)
        menuEdit.add_command(label="删除数据", command=self.deleteData)
        menuExit = Menu(mainmenu)
        mainmenu.add_cascade(label="退出", menu=menuExit)
        menuExit.add_command(label="退出", command=self.root.destroy)
        self.root["menu"] = mainmenu

    def inputData(self):
        self.inputPage.pack()
        self.addPage.pack_forget()
        self.deletePage.pack_forget()

    def addData(self):
        self.inputPage.pack_forget()
        self.addPage.pack()
        self.deletePage.pack_forget()

    def deleteData(self):
        self.inputPage.pack_forget()
        self.addPage.pack_forget()
        self.deletePage.pack()

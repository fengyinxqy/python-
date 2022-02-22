from os import write
from tkinter import *
from tkinter import ttk
import csv
import tkinter.messagebox


class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        s_x = Scrollbar(self)
        s_x.pack(side=RIGHT, fill=Y)
        s_y = Scrollbar(self, orient=HORIZONTAL)
        s_y.pack(side=BOTTOM, fill=X)
        text = Text(self, yscrollcommand=s_x.set, xscrollcommand=s_y.set, wrap="none")
        text.pack(fill=BOTH)
        s_x.config(command=text.yview)
        s_y.config(command=text.xview)

        def openfile():
            text.delete(1.0, END)
            csvreader = csv.reader(
                open("python basis\Part7\文件\招生人数.csv", "r", encoding="utf-8")
            )
            final_list = list(csvreader)
            for i in range(0, len(final_list)):
                text.insert(INSERT, final_list[i])
                text.insert(INSERT, "\n")

        def savefile():
            text_content = []
            text_content = (text.get(1.0, END).replace(" ", ",")).split("\n")
            text_content.pop()
            text_content.pop()
            new = []
            for el in text_content:
                new.append(el.split(","))
                with open(
                    "python basis\Part7\文件\招生人数.csv", "w", newline="", encoding="utf-8"
                ) as t:
                    write = csv.writer(t)
                    write.writerows(new)
                    tkinter.messagebox.showinfo("通知", "保存成功!")

        Button(self, text="显示数据", width=10, command=openfile).pack(side="left", padx=10)
        Button(self, text="保存数据", width=10, command=savefile).pack(
            side="right", padx=10
        )


class AddFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemYear = StringVar()
        self.itemMajor = StringVar()
        self.itemNation = StringVar()
        self.itemNo = StringVar()
        self.createPage()

    def add_num(self):
        info = []
        if self.S1.get():
            info.append(self.S1.get())
            if self.E1.get():
                info.append(self.E1.get())
                if self.comb.get():
                    info.append(self.comb.get())
                    if self.E2.get():
                        info.append(self.E2.get())
                    else:
                        info.append("无")
                else:
                    info.append("无")
            else:
                info.append("无")
        else:
            info.append("无")
        with open(
            "python basis\Part7\文件\招生人数.csv", "a", newline="", encoding="utf-8"
        ) as t:
            write = csv.writer(t)
            write.writerow(info)
            tkinter.messagebox.showinfo("通知", "插入成功!")

    def createPage(self):
        Label(self, text="年份").grid(row=1, sticky=W, pady=10)
        self.S1 = Spinbox(self, from_=2001, to=2021, increment=1)
        self.S1.grid(row=1, column=1, sticky=E)
        Label(self, text="专业").grid(row=2, sticky=W, pady=10)
        self.E1 = Entry(self, textvariable=self.itemMajor)
        self.E1.grid(row=2, column=1, sticky=E)
        Label(self, text="民族 ").grid(row=3, sticky=W, pady=10)
        self.comb = ttk.Combobox(self, value="汉族、蒙古族、回族、藏族、满族、维吾尔族、土家族、哈萨克族".split("、"))
        self.comb.grid(row=3, column=1, sticky=E)
        Label(self, text="人数").grid(row=4, sticky=E, pady=10)
        self.E2 = Entry(self, textvariable=self.itemYear)
        self.E2.grid(row=4, column=1, sticky=E)
        Button(self, text="添加", command=self.add_num).grid(
            row=6, column=1, sticky=E, pady=10
        )


class DeleteFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemMajor = StringVar()
        self.itemYear = StringVar()
        self.createPage()

    def del_num(self):
        if self.S1.get() == "":
            tkinter.messagebox.showinfo(title="出错", message="输入年份不能为空")
        if self.E1.get() == "":
            tkinter.messagebox.showinfo(title="出错", message="输入专业不能为空")
        if self.comb.get() == "":
            tkinter.messagebox.showinfo(title="出错", message="输入民族不能为空")
        csvreader = csv.reader(
            open("python basis\Part7\文件\招生人数.csv", "r", encoding="utf-8")
        )
        final_list = list(csvreader)
        for i in range(0, len(final_list)):
            if (
                final_list[i][0] == self.S1.get()
                and final_list[i][1] == self.E1.get()
                and final_list[i][2] == self.comb.get()
            ):
                delnum = i
                del final_list[delnum]
                break
        with open(
            "python basis\Part7\文件\招生人数.csv", "w", newline="", encoding="utf-8"
        ) as t:
            writer = csv.writer(t)
            writer.writerows(final_list)
            tkinter.messagebox.showinfo("通知", "删除成功!")

    def createPage(self):
        Label(self, text="年份").grid(row=1, sticky=W, pady=10)
        self.S1 = Spinbox(self, from_=2001, to=2021, increment=1)
        self.S1.grid(row=1, column=1, sticky=E)
        Label(self, text="专业").grid(row=2, sticky=W, pady=10)
        self.E1 = Entry(self, textvariable=self.itemMajor)
        self.E1.grid(row=2, column=1, sticky=E)
        Label(self, text="民族 ").grid(row=3, sticky=W, pady=10)
        self.comb = ttk.Combobox(self, value="汉族、蒙古族、回族、藏族、满族、维吾尔族、土家族、哈萨克族".split("、"))
        self.comb.grid(row=3, column=1, sticky=E)
        Button(self, text="删除", command=self.del_num).grid(
            row=6, column=1, sticky=E, pady=10
        )

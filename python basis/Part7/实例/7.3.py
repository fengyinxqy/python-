from tkinter import ttk
from tkinter import *
import csv
from typing import ValuesView

final_list = []
with open(
    "E:\Desktop\Python\python basis\Part7\文件\招生人数.csv", "r", encoding="utf-8"
) as f:
    for line in f:
        line = line.strip()
        final_list.append(line.split("\t"))
final_list.pop(0)
print(final_list)
""" f = open('E:\Desktop\Python\python basis\Part7\文件\招生人数.csv',
        "r", encoding='utf-8')
csvreader = csv.reader(f).split('\t')
final_list = list(csvreader)[1:] """
root = Tk()
root.geometry("600x300")
lb1 = Label(root, text="选择查询条件", font=("华文仿宋", 15))
lb1.place(relx=0.1, rely=0.1)


def query():
    year = spin.get()
    major = var.get()
    nation = comb.get()
    selected = [
        x for x in final_list if x[0] == year and x[1] == major and x[2] == nation
    ]
    if selected:
        text.insert(
            INSERT, year + "年" + major + "专业招收" + nation + "民族学生人数为: " + selected[0][3]
        )
    else:
        text.insert(INSERT, "没有查询到结果!")


def clear():
    text.delete(1.0, END)


spin = Spinbox(root, values=("2016", "2017", "2018", "2019", "2020"))
spin.place(relx=0.1, rely=0.3, relwidth=0.25)
comb = ttk.Combobox(root, value="汉族、蒙古族、回族、藏族、满族、维吾尔族、土家族、哈萨克族".split("、"))
comb.place(relx=0.1, rely=0.45, relwidth=0.25)
comb.current(0)
var = StringVar(root)
var.set("专业")
om = OptionMenu(root, var, *"哲学、经济学、法学、教育学、文学、历史学、理学、工学、管理学".split("、"))
om.place(relx=0.1, rely=0.6, relwidth=0.25)
btn1 = Button(root, text="查询", command=query)
btn1.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)
btn1 = Button(root, text="清空", command=clear)
btn1.place(relx=0.25, rely=0.8, relwidth=0.1, relheight=0.1)
lb2 = Label(root, text="结果", font=("华文仿宋", 15))
text = Text(root, width=30, height=10)
text.place(relx=0.5, rely=0.3)
root.mainloop()

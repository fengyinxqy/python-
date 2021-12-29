from os import write
from tkinter import *
import csv
import tkinter.messagebox
""" 导入数据 """
def openfile():
    csvreader=csv.reader(open('python\python basis\Part7\文件\招生人数.csv',encoding='utf-8'))
    final_list=list(csvreader)
    text.delete(1.0,END)
    for i in range(0,len(final_list)):
        text.insert(INSERT,final_list[i])
        text.insert(INSERT,'\n')
""" 保存数据 """
def savefile():
    text_content=[]
    text_content=(text.get(1.0,END).replace(' ', ',')).split("\n")
    text_content.pop()
    text_content.pop()
    new=[]
    for el in text_content:
        new.append(el.split(","))
    with open('python\python basis\Part7\文件\招生人数.csv','w',newline='',encoding='utf-8') as t:
        write=csv.writer(t)
        write.writerows(new)
        tkinter.messagebox.showinfo('通知','保存成功')

""" 退出 """
def ask():
    if tkinter.messagebox.askokcancel('退出','确定退出吗?'):
        root.destroy()
        
root=Tk()
root.title('菜单')
root.geometry('600x500')
mainmenu=Menu(root)
menuFile=Menu(mainmenu)

mainmenu.add_command(label='导入数据',command=openfile)
mainmenu.add_command(label='保存数据',command=savefile)
menuFile.add_separator()
menuFile.add_command(label='退出',command=ask)
mainmenu.add_cascade(label='文件',menu=menuFile)
root['menu']=mainmenu
s_x=Scrollbar(root)
s_x.pack(side=RIGHT,fill=Y)
s_y=Scrollbar(root,orient=HORIZONTAL)
s_y.pack(side=BOTTOM,fill=X)
text=Text(root,width=200,yscrollcommand=s_x.set,xscrollcommand=s_y.set,wrap='none')
text.pack(expand=YES,fill=BOTH)
s_x.config(command=text.yview)
s_y.config(command=text.xview)
root.mainloop()
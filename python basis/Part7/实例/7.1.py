from tkinter import *
root = Tk()
root.title('学生成绩')
root.geometry('300x450+100+100')


def show():
    with open('E:\Desktop\Python\python basis\Part7\文件\学生成绩.csv', "r", encoding="utf-8") as f:
        lb.configure(text=f.read())


lb = Label(root, text='', width=30, height=15, fg='purple', font=("黑体", 15))
lb.pack()
btn = Button(root, text="显示", command=show)
btn.pack()
root.mainloop()

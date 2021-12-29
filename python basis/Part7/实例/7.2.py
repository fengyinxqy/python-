from tkinter import *
root = Tk()
root.title("计算两个数的和")
root.geometry('400x180')


def summation():
    a = float(num1.get())
    b = float(num2.get())
    s = '%0.2f+%0.2f=%0.2f\n' % (a, b, a+b)
    lb.configure(text=s)


def clear():
    num1.delete(0)
    num2.delete(0)
    lb.configure(text='请输入两个数，计算两个数的和')


lb = Label(root, text='请输入两个数，计算两个数的和', font=('华文仿宋', 15))
lb.grid(row=0, column=1, columnspan=3)
lb1 = Label(root, text='请输入第一个数字', fg='blue', font=('华文仿宋', 12))
lb1.grid(row=1, column=1)
num1 = Entry(root)
num1.grid(row=1, column=2)

lb2 = Label(root, text='请输入第二个数字', fg='blue', font=('华文仿宋', 12))
lb2.grid(row=2, column=1)
num2 = Entry(root)
num2.grid(row=2, column=2)

btn1 = Button(root, text='求和', command=summation)
btn1.grid(row=1, column=3, sticky=E)
btn2 = Button(root, text='清空', command=clear)
btn2.grid(row=2, column=3, sticky=E)


root.mainloop()

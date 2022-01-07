from tkinter import *
class MainPage(object):
    def __init__(self,master=None):
        self.root = master
        self.root.geometry('%dx%d'%(500,300))
        self.entry_height=StringVar()
        self.entry_weight = StringVar()
        self.Bmi1=StringVar()
        self.Bmi2 = StringVar()
        self.createPage()
        
    def createPage(self):
        self.main=Frame(self.root)#创建Frame
        self.main.pack()
        #设置身高标签和输入框
        Label(self.main,text='身高(cm)',font=('隶书,18')).grid(row=2,column=1,sticky=W,pady=2)
        Entry(self.main,textvariable=self.entry_height,font=('隶书,18')).grid(row=2,column=3,sticky=W,pady=2)
        #设置体重标签和输入框
        Label(self.main,text='体重(kg)',font=('隶书,18')).grid(row=3,column=1,sticky=W,pady=2)
        Entry(self.main,textvariable=self.entry_weight,font=('隶书,18')).grid(row=3,column=3,sticky=W,pady=2)
        Button(self.main, text='计算BMI指数',font=('隶书',14),command=self.bmi).grid(row=4, column=1, rowspan=2,columnspan=2)
        Button(self.main, text='清空',font=('隶书',14),command=self.clear).grid(row=4, column=3, rowspan=2, columnspan=2)
        #添加显示结果的输入框
        Entry(self.main, textvariable=self.Bmi1,font=('隶书',18)).grid(row=7, column=1, rowspan=2, columnspan=3)
        Entry(self.main, textvariable=self.Bmi2,font=('隶书',18)).grid(row=10, column=1, rowspan=2, columnspan=3)
    def bmi(self):
        bmi_set=round(float(self.entry_weight.get())/(float(self.entry_height.get())*float(self.entry_height.get()))*10000,2)
        if bmi_set<18.5:
            state=('过轻')
        elif 18.5<=bmi_set<25:
            state=('正常')
        elif 25<=bmi_set<28:
            state=('过重')
        elif 28 <= bmi_set <32:
            state=('肥胖')
        else:
          state = ('严重肥胖')
        BMI_result=('您的BMI为: ',bmi_set)
        BMI_state=('您的体型属于: ',state)
        self.Bmi1.set(BMI_result)
        self.Bmi2.set(BMI_state)
    def clear(self):
        self.entry_height.set("")
        self.entry_weight.set("")
        self.Bmi1.set("")
        self.Bmi2.set("")
            
            
        
        
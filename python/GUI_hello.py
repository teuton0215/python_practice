#!/user/bin/env python3
# -*-  coding: utf-8 -*-

from  tkinter import  *            #tkinter 是python自带的包

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helllabel  =  Label(self, text='Hello, World!')
        self.helllabel.pack()
        self.quitButtom = Button(self,text='Quite',command =self.quit)
        self.quitButtom.pack()


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
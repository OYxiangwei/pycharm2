import tkinter

tk = tkinter.Tk()
tk.wm_title("测试TK")
#lab1 = tkinter.Label(tk,text ="标签",font ="篆书")
#lab1.pack()
#lab2 = tkinter.Label(tk,text="绿色背景",background= "green",underline = True)
#lab2.pack()
#lab3 = tkinter.Label(tk,text="红色背景",background="red" )
#lab3.pack()
def showlabel():
    global tk
    lab = tkinter.Label(tk,text="创建标签")
    lab.grid(row=0,sticky=tkinter.W)

#btn1= tkinter.Button(tk,text="显示标签",command=showlabel,bg="blue",bd="32px",width="40",font="楷书")
#btn1.pack(side = tkinter.LEFT,expand=tkinter.YES,fill=tkinter.Y)
#btn2= tkinter.Button(tk,text="显示标签",command=showlabel,bg="yellow",bd="12px",width="18",font="楷书")
#btn2.pack(side =tkinter.BOTTOM,fill=tkinter.BOTH,expand=tkinter.NO,anchor=tkinter.S,ipadx=10,ipady=10,padx=10,pady=10)
en = tkinter.Entry(tk,text="输入")
en.grid(row=1,column=2,sticky=tkinter.E)
btn3 = tkinter.Button(tk,text="按钮3",command=showlabel).grid(row=3,column=5,sticky=tkinter.W)
tk.mainloop()

import tkinter

baseframe = tkinter.Tk()
def reg():
    name = en1.get()
    pwd = en2.get()
    t1 = len(name)
    t2 = len(pwd)
    if name=="11" and pwd =="22":
        lb3["text"]="登入成功"
    else:
        lb3["text"]="密码或者用户名错误"
        en1.delete(0,t1)
        en2.delete(0,t2)
lb1 = tkinter.Label(baseframe,text="用户名：")
lb1.grid(row=0,column=1)
lb2 = tkinter.Label(baseframe,text = "密码:")
lb2.grid(row=1,column=1)
lb3 = tkinter.Label(baseframe,text="")
lb3.grid(row=3,column=4)
en1 = tkinter.Entry(baseframe)
en1.grid(row=0,column=2)
en2 = tkinter.Entry(baseframe)
en2.grid(row=1,column=2)
en2['show'] = "*"
bn = tkinter.Button(baseframe,text="登录",command=reg).grid(row=4,column=2)

baseframe.mainloop()
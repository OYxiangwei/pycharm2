import tkinter

baseframe= tkinter.Tk()
def baselabel(event):
    global baseframe
    lb = tkinter.Label(baseframe,text="谢谢点击")
    lb.pack()

lb2 = tkinter.Label(baseframe,text="模拟按钮")
lb2.bind("<Button-1>",baselabel)
lb2.pack()

baseframe.mainloop()
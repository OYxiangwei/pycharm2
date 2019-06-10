import tkinter

tk = tkinter.Tk()
def makelabel():
    global tk
    tkinter.Label(tk,text="最好的足迹").pack()

meun1 = tkinter.Menu(tk)
for i in ["小鸡","蘑菇","大葱"]:
    meun1.add_separator()
    meun1.add_command(label=i)

meun1.add_command(label="火锅",command=makelabel)

def pop(event):
    meun1.post(event.x,event.y)

tk.bind("<Button-1>",pop)
tk.mainloop()

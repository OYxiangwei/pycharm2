import tkinter

tk = tkinter.Tk()
tk.wm_title("球运动")
def bck(event):
    global cav
    cav.move(ball,12,5)
    cav.move("fall",0,5)
cav = tkinter.Canvas(tk,width = 500, height = 500)
cav.pack()
cav.bind("<Button-1>",bck)

ball= cav.create_oval(20,20,50,50, fill="green")
cav.create_text(123,56,text="i love hack",fill="red",tag="fall")
re = cav.create_rectangle(56,78,173,110,fill="gray")
cav.addtag_withtag("fall",re)
tk.mainloop()
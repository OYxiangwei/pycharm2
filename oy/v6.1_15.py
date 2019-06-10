import tkinter

tk = tkinter.Tk()
cav = tkinter.Canvas(tk,width =200, height=210)
cav.pack()
cav.create_line(12,13,150,160)
cav.create_text(23,23,text="xian")
tk.mainloop()
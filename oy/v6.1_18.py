import tkinter
baseframe = tkinter.Tk()
mu = tkinter.Menu(baseframe)
for item in ("1号","2号","3号","4号"):
    mu.add_command(label=item)

baseframe["menu"] =mu

baseframe.mainloop()
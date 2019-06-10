import tkinter
tk = tkinter.Tk()
emenu = tkinter.Menu(tk)
cmenu= tkinter.Menu(tk)
c2menu = tkinter.Menu(tk)
for item in ["yi","er","san","shi"]:
    cmenu.add_cascade(label=item)
for item2 in ["dage","brother"]:
    c2menu.add_cascade(label = item2)
emenu.add_cascade(label="file")
emenu.add_cascade(label="edit",menu=cmenu)
emenu.add_cascade(label="about",menu=c2menu)
tk["menu"]=emenu
tk.mainloop()
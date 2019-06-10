import tkinter
import math as m

tk = tkinter.Tk()
cav = tkinter.Canvas(tk,width=500,height=500,background="gray")
cav.pack()
center_x =150
center_y =150
r = 150
points = [
    center_x-int(r*m.sin(2*m.pi/5)),
    center_y-int(r*m.cos(2*m.pi/5)),

    center_x+int(r*m.sin(2*m.pi/5)),
    center_y-int(r*m.cos(2*m.pi/5)),
    center_x-int(r*m.sin(m.pi/5)),
    center_y+int(r*m.cos(m.pi/5)),
    center_x,
    center_y-r,
    center_x+int(r*m.sin(m.pi/5)),
    center_y+int(r*m.cos(m.pi/5)),
]
cav.create_polygon(points,outline="red",fill="yellow")
cav.create_text(150,150,text="五角星")
tk.mainloop()
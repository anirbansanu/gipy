from tkinter import *


def call():
    var.set("funtion is called")
    v = e.get()
    s.set(v)


tk = Tk()
tk.geometry("500x300+20+20")

var = StringVar()
s = StringVar()
s.set("None")
var.set("Hello World")

f = Frame(tk, bg="black", height=100, width=300)
f.winfo_geometry()
f.grid(row=0)

l = Label(f, textvariable=var, width=20, fg="grey", bg="black")
l1 = Label(f, textvariable=s, width=33, fg="green", bg="black")
b = Button(f, text="click", command=call)
e = Entry(f, width=35)

l.grid(row=0, column=0)
e.grid(row=1)
b.grid(row=2)
l1.grid(row=3)
tk.mainloop()

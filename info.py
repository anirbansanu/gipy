from tkinter import *


def on_click():
    print("clicked")


root = Tk()
root.title("Search")
root.resizable(width=False, height=False)

f = Frame(root, bg="#de5b6f")
f.grid(row=0)

e = Entry(f, width=35)
e.grid(row=1)

b = Button(f, text="Search", command="on_click")
b.grid(row=1, column=1)

f2 = Frame(f)
f2.grid(row=2, columnspan=2)

sbar = Scrollbar(f2)
sbar.pack(side=RIGHT, fill=Y)


t = Text(f2, width=50, height=20, fg="black", bg="grey", wrap=WORD, yscrollcommand = sbar.set)
t.pack(side=LEFT)
sbar.config(command=t.yview())


root.mainloop()

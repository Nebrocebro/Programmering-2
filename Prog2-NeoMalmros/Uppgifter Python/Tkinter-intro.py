from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
b = Button(root, text="Tryck mig!")
def click_handler(self):
    lbl["text"] = "Du skrev: " + e.get()
b.bind("<Button-1>", click_handler)
b.pack()
lbl = Label(root)
lbl.pack()
root.mainloop()
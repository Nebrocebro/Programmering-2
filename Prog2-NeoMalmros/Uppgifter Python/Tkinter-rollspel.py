from tkinter import *
import random as rand
root = Tk()

racelistheader = StringVar(root)
racelistheader.set("Choose Race") # default value

racelist = OptionMenu(root, racelistheader, "Choose Race", "Human", "Orc", "Dwarf", "Elf", "Wizard")
def click_handler(self):
    race = str("")
racelist.pack()
nameentry = Entry(root)
nameentry.pack

root.mainloop()
# frame = Frame(root) #, height="300px", width="200px"
# frame.pack()
# racelist = Listbox(root)
# racelist.place(frame)
# racelist.insert(1, "Orc")
# racelist.insert(2, "Human")
# racelist.insert(3, "Dwarf")
# racelist.insert(4, "Elf")
# racelist.insert(5, "Wizard")
# racelist.pack()

class Character():
    
    name = str(nameentry.get())
    pow = rand.randint(1, 100)
    hp = rand.randint(1, 250)
    spd = rand.randint(1, 100)
    itl = rand.randint(1, 100)
    psy = rand.randint(1, 100)
    cha = rand.randint(1, 100)
    siz = rand.randint(1, 30)

class Work():
    salary = rand.randint(1, 100000)
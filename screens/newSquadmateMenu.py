from tkinter import *
from objects import characterClass
import json

s = ""
name = ""

# New Windows
def new(root):  # new window definition
    # Create New Window
    newwin = Toplevel(root)

    # Title Label
    label1 = Label(newwin, text="New Squadmate Sceen")
    label1.pack()

    space(newwin)
    nameSection(newwin)
    space(newwin)
    classSelection(newwin)
    space(newwin)
    Label(newwin, text="Only hit this once you have finalized name and class").pack()
    finalize(newwin)

# Logic
def nameSection(newwin):
    # Name Label
    label1 = Label(newwin, text="Name")
    label1.pack()
    # NameEntry
    v = StringVar()
    e = Entry(newwin, textvariable=v)
    e.pack()
    def callback():
        global name
        name = v.get()

    b = Button(newwin, text="Finalize Name", width=10, command=callback)
    b.pack()

def classSelection(newwin):
    # Class Label
    label2 = Label(newwin, text="Please Select From One of These Classes")
    label2.pack()

    tkvar = StringVar(newwin)
    choices = {'Sniper', 'Soldier', 'Berzerker', 'Heavy Gunner', 'Scout'}
    tkvar.set('Soldier')  # set the default option

    popupMenu = OptionMenu(newwin, tkvar, *choices)
    Label(newwin, text="Choose a Class")
    popupMenu.pack()
    def check():
        characterClass.display(tkvar.get(), newwin)
    button = Button(newwin, text="Check Stats", command=check)
    button.pack()

    def callback():
        global s
        s = tkvar.get()

    button = Button(newwin, text="Finalize Class", command=callback)
    button.pack()



def space(newwin):
    space = Label(newwin, text="")
    space.pack()

def finalize(newwin):
    button = Button(newwin, text="Finalize Character", command=lambda: confirm(newwin))
    button.pack()

def confirm(newwin):
    global name
    global s
    display = Toplevel(newwin)
    Label(display, text="You have selected: ").pack()
    Label(display, text="Name - " + name).pack()
    Label(display, text="Class - " + s).pack()
    def yesCallback():
        with open('game.json', 'r') as f:
            characters = json.load(f)
        x = "Squadmate " + str(len(characters))
        characters[x] = {}
        z = characters[x]
        z["name"] = name
        selectedClass = characterClass.getSelectedClass(s)
        z["class"] = selectedClass.name
        stats = selectedClass.stats
        z["stats"] = {}
        zStats = z["stats"]
        zStats["end"] = stats.end
        zStats["sArm"] = stats.sArms
        zStats["mArm"] = stats.mArms
        zStats["hArm"] = stats.hArms
        zStats["gre"] = stats.grenade
        zStats["lRange"] = stats.lRange
        zStats["sRange"] = stats.sRange
        z["stats"] = zStats
        characters[x] = z
        with open('game.json', 'w') as f:
            json.dump(characters, f)

        display.destroy()
        newwin.destroy()
    def noCallback():
        display.destroy()

    b = Button(display, text="Confirm", width=10, command=yesCallback)
    b.pack()

    b2 = Button(display, text="Deny", width=10, command=noCallback)
    b2.pack()
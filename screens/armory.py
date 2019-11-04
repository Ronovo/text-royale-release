from tkinter import *
from objects import weapons

choices = ['Small Arms', 'Medium Arms', 'Large Arms']
weaponList = []

# New Windows
def new(root):  # new window definition
    # Create New Window
    newwin = Toplevel(root)

    # Title Label
    Label(newwin, text="Welcome to the Armory!").pack()

    space(newwin)
    Label(newwin, text="Please Choose a Weapon").pack()

    listbox = Listbox(newwin)
    listbox.pack()
    for item in choices:
        listbox.insert(END, item)

    btn_text = StringVar()
    btn_text.set("Choose Type")

    selectWeaponType(btn_text, listbox, newwin)

    goBackButton(btn_text, listbox, newwin)

    space(newwin)

def space(newwin):
    space = Label(newwin, text="")
    space.pack()


def selectWeaponType(text, listbox, newwin):
        def callback():
            global weaponList
            if text.get() == "Choose Type":
                weaponList = []
                var = listbox.curselection()
                wType = choices[var[0]]
                listbox.delete(0, END)
                newlist = weapons.getWeaponListByWeaponType(wType)
                if len(newlist) != 0:
                    for x in newlist:
                        weaponList.append(x.name)
                    for item in weaponList:
                        listbox.insert(END, item)
                    text.set("Choose Weapon")
            else:
                var = listbox.curselection()
                wName = weaponList[var[0]]
                weapons.display(wName, newwin)
        button = Button(newwin, textvariable=text, command=callback)
        button.pack()

def goBackButton(text, listbox, newwin):
    def revert():
        global weaponList
        if len(weaponList) != 0:
            listbox.delete(0, END)
            for item in choices:
                listbox.insert(END, item)
            text.set("Choose Type")
    button2 = Button(newwin, text="Return", command=revert)
    button2.pack()
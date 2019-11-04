import json
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from weaponMethods import hitCalculations

mode = "Single Shot"


# New Windows
def new(armory, selectedWeapon):  # new window definition
    global mode
    # Create New Window
    newwin = Toplevel(armory)
    newwin.geometry("400x700")

    # Create Target Dummy
    dummy = {
        "health": 200,
        "distance": 50
    }

    # Title Label
    Label(newwin, text="Welcome to the Gun Range!").pack()
    space(newwin)

    # Weapon Name
    weapon = "Weapon Selected: " + selectedWeapon.name
    Label(newwin, text=weapon).pack()

    # Ammo Count
    selectedWeapon.currentAmmo = selectedWeapon.maxAmmo
    ammoDisplay = "Ammo: " + str(selectedWeapon.currentAmmo) + "/" + str(selectedWeapon.maxAmmo)
    var = StringVar()
    var.set(ammoDisplay)
    ammoLabel = Label(newwin, textvariable=var)
    ammoLabel.pack()
    space(newwin)

    # Menu To Set Dummy Distance
    tkvar = StringVar(newwin)
    choices = [50, 100, 150, 200, 300, 400, 500]
    tkvar.set(50)  # set the default option
    popupMenu = OptionMenu(newwin, tkvar, *choices)
    popupMenu.pack()

    # Button To Set Dummy Distance
    def callback():
        dummy["distance"] = tkvar.get()
        distance = "Placed " + str(dummy["distance"]) + "M away\n"
        st.insert(END, distance)
        st.see("end")
    button = Button(newwin, text="Set Target Range", command=callback)
    button.pack()
    space(newwin)

    # Menu To Set Firing Mode
    tkvar2 = StringVar(newwin)
    choices2 = ["Single Shot", "3 Round", "Full Clip"]
    tkvar2.set("Single Shot")  # set the default option
    popupMenu2 = OptionMenu(newwin, tkvar2, *choices2)
    popupMenu2.pack()

    # Button To Set Firing Mode
    def callback3():
        global mode
        mode = tkvar2.get()
        rate = mode + " set\n"
        st.insert(END, rate)
        st.see("end")
    button = Button(newwin, text="Lock In Mode", command=callback3)
    button.pack()
    space(newwin)

    # Button to Fire Your Weapon
    def callback():
        global mode
        if selectedWeapon.currentAmmo != 0:
            if mode == "Single Shot":
                singleShot(selectedWeapon, dummy, st, var)
            elif mode == "3 Round":
                for x in range(0, 3):
                    singleShot(selectedWeapon, dummy, st, var)
            elif mode == "Full Clip":
                for x in range(0, selectedWeapon.currentAmmo):
                    singleShot(selectedWeapon, dummy, st, var)
        else:
            st.insert(END, "Please Reload!\n")
            st.see("end")
    button = Button(newwin, text="Fire", command=callback)
    button.pack()

    # Button to Reload Your Weapon
    def callback2():

        if selectedWeapon.currentAmmo != selectedWeapon.maxAmmo:
            st.insert(END, "Weapon Reloaded\n")
            st.see("end")
            selectedWeapon.currentAmmo = selectedWeapon.maxAmmo
            ammoDisplay = "Ammo: " + str(selectedWeapon.currentAmmo) + "/" + str(selectedWeapon.maxAmmo)
            var.set(ammoDisplay)
        else:
            st.insert(END, "Clip is full\n")
            st.see("end")
    button = Button(newwin, text="Reload", command=callback2)
    button.pack()
    space(newwin)

    # TextBox
    st = ScrolledText(newwin, height=12, width=30)
    st.pack()
    st.insert(INSERT, "Dummy Created!\n")
    st.insert(END, "Placed 50M Away\n")
    space(newwin)


def space(newwin):
    space = Label(newwin, text="")
    space.pack()


def singleShot(selectedWeapon, dummy, st, var):
    selectedWeapon.currentAmmo -= 1
    hitCalculations.simpleHit(selectedWeapon, dummy, st)
    ammoDisplay = "Ammo: " + str(selectedWeapon.currentAmmo) + "/" + str(selectedWeapon.maxAmmo)
    var.set(ammoDisplay)
    # Dummy Destroyed Logic
    if dummy["health"] <= 0:
        st.insert(INSERT, "Dummy Destroyed!\n")
        dummy["health"] = 200
        with open('game.json', 'r') as f:
            character = json.load(f)
        kills = character["kills"]
        kills["dummy"] += 1
        st.insert(INSERT, "Your Dummy Kill Count is: " + str(kills["dummy"]) + "!\n")
        with open('game.json', 'w') as f:
            json.dump(character, f)
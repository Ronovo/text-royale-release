from tkinter import *
import json

def rosterSheet(root):
    rosterwin = Toplevel(root)

    # Title Label
    label1 = Label(rosterwin, text="Character Sheet")

    with open('game.json', 'r') as f:
        characters = json.load(f)
    x = 0
    rowCounter = 0
    while x < 4:
        if x == 0:
            squadmate = "leader"
        else:
            squadmate = "Squadmate " + str(x)
        selected = characters[squadmate]
        Label(rosterwin, text="Name: " + selected["name"]).grid(row=rowCounter, column=2)
        if x == 0:
            Label(rosterwin, text="Leader").grid(row=rowCounter, column=3)
        Label(rosterwin, text="Class: " + selected["class"]).grid(row=rowCounter, column=4)
        stats = selected["stats"]
        rowCounter += 1
        Label(rosterwin, text="Endurance: " + str(stats["end"])).grid(row=rowCounter, column=3)
        rowCounter += 1
        Label(rosterwin, text="Small Arms: " + str(stats["sArm"])).grid(row=rowCounter, column=2)
        Label(rosterwin, text="Medium Arms: " + str(stats["mArm"])).grid(row=rowCounter, column=3)
        Label(rosterwin, text="Heavy Arms: " + str(stats["hArm"])).grid(row=rowCounter, column=4)
        rowCounter += 1
        Label(rosterwin, text="Long Range: " + str(stats["lRange"])).grid(row=rowCounter, column=2)
        Label(rosterwin, text="Short Range: " + str(stats["sRange"])).grid(row=rowCounter, column=3)
        Label(rosterwin, text="Grenades: " + str(stats["gre"])).grid(row=rowCounter, column=4)
        rowCounter += 1
        Label(rosterwin, text="").grid(row=rowCounter, column=4)
        rowCounter += 1
        Label(rosterwin, text="").grid(row=rowCounter, column=4)
        rowCounter += 1
        x += 1

    def callback():
        rosterwin.destroy()
    Button(rosterwin, text="Main Menu", command=callback).grid(row=rowCounter, column=3)
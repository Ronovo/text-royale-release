from tkinter import *
import json

def sheet(root):
    sheetwin = Toplevel(root)

    with open('game.json', 'r') as f:
        character = json.load(f)
    Label(sheetwin, text="Name: " + character["name"]).grid(row=0, column=3)
    Label(sheetwin, text="You have selected " + character["class"]).grid(row=2, column=3)
    stats = character["stats"]
    Label(sheetwin, text="Endurance: " + str(stats["end"])).grid(row=3, column=2)
    Label(sheetwin, text="Health: " + str(character["health"])).grid(row=3, column=4)
    Label(sheetwin, text="Small Arms: " + str(stats["sArm"])).grid(row=4, column=2)
    Label(sheetwin, text="Medium Arms: " + str(stats["mArm"])).grid(row=4, column=3)
    Label(sheetwin, text="Heavy Arms: " + str(stats["hArm"])).grid(row=4, column=4)
    Label(sheetwin, text="Long Range: " + str(stats["lRange"])).grid(row=5, column=2)
    Label(sheetwin, text="Short Range: " + str(stats["sRange"])).grid(row=5, column=3)
    Label(sheetwin, text="Grenades: " + str(stats["gre"])).grid(row=5, column=4)
    Label(sheetwin, text="Kills").grid(row=6, column=3)
    kills = character["kills"]
    Label(sheetwin, text="Gun Range Dummy: " + str(kills["dummy"])).grid(row=7, column=3)

    def callback():
        sheetwin.destroy()
    Button(sheetwin, text="Main Menu", command=callback).grid(row=8, column=3)

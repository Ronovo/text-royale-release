from tkinter import *
import json

def tutorialMainThread(root):
    leaderJumpFlag = False
    tutorialWindow = Toplevel(root)
    tutorialWindow.minsize(400, 0)
    # Title Label
    Label(tutorialWindow, text="Turns: 0").pack()
    Label(tutorialWindow, text="").pack()
    Label(tutorialWindow, text="Welcome to the tutorial level!").pack()
    Label(tutorialWindow, text="You and Your Squad are on the plane to Tutorial Island Now").pack()
    # Jump Button
    Label(tutorialWindow, text="Press the button to jump out").pack()
    okVar = IntVar()
    def jump():
        okVar.set(1)
    Button(tutorialWindow, text="Jump", command=lambda: jump()).pack()
    tutorialWindow.wait_variable(okVar)

    with open('game.json', 'r') as f:
        characters = json.load(f)

    selected = characters["leader"]
    Label(tutorialWindow, text="(These Numbers will be Randomly Generated in the real game.)").pack()
    Label(tutorialWindow, text="Nearest Town: 7").pack()
    Label(tutorialWindow, text="5m South").pack()
    Label(tutorialWindow, text="").pack()
    Label(tutorialWindow, text="Congrats, " + selected["name"] + ", you landed in the outskits of the 7th town on the map!").pack()
    Label(tutorialWindow, text="(Map In Future Update)").pack()
    Label(tutorialWindow, text="").pack()

    # Scan Button
    Label(tutorialWindow, text="When you land the first thing you need to do is scan the area.").pack()

    okVar = IntVar()

    def scan():
        okVar.set(1)
    Button(tutorialWindow, text="Scan", command=lambda: scan()).pack()
    tutorialWindow.wait_variable(okVar)

    Label(tutorialWindow, text="You See a 1 Story House about 5m South of you.").pack()
    Label(tutorialWindow, text="Houses provide great cover and the ability to gain loot.")
    #MoveHouse Button
    Label(tutorialWindow, text="Click the button to move towards it.")

    okVar = IntVar()

    def moveHouse():
        okVar.set(1)

    Button(tutorialWindow, text="Move To House", command=lambda: moveHouse()).pack()
    tutorialWindow.wait_variable(okVar)

    Label(tutorialWindow,
          text="Congrats, " + selected["name"] + ", You have made your first movement plan of the game!").pack()
    Label(tutorialWindow, text="Every Character's turn consists of two actions: Movement, and Free Actions")
    Label(tutorialWindow, text="Free Actions include things like Taking Cover at Windows or Looting Buildings.")
    Label(tutorialWindow, text="NOTE: SCANNING HAS NO COST, AND CAN BE DONE FREELY")
    # MoveHouse Button
    Label(tutorialWindow, text="Speaking of looting, let's loot the building ahead of us.")

    okVar = IntVar()

    def lootHouse():
        okVar.set(1)

    Button(tutorialWindow, text="Loot House", command=lambda: lootHouse()).pack()
    tutorialWindow.wait_variable(okVar)

    Label(tutorialWindow, text="You Found an M1911! Ammo: .45 ACP").pack()
    Label(tutorialWindow, text="You Found 14 Rounds").pack()
    Label(tutorialWindow, text="With no other items in hand, you equip the handgun").pack()

    # End First Trip
    Label(tutorialWindow, text="Congratulations! You have completed your first round!").pack()

    okVar = IntVar()

    def endTrip():
        okVar.set(1)

    Button(tutorialWindow, text="End Trip", command=lambda: endTrip()).pack()
    tutorialWindow.wait_variable(okVar)
    tutorialWindow.destroy()
    """
    Label(sheetwin, text="Name: " + selected["name"]).grid(row=0, column=3)
    Label(sheetwin, text="You have selected " + selected["class"]).grid(row=2, column=3)
    stats = selected["stats"]
    Label(sheetwin, text="Endurance: " + str(stats["end"])).grid(row=3, column=3)
    Label(sheetwin, text="Small Arms: " + str(stats["sArm"])).grid(row=4, column=2)
    Label(sheetwin, text="Medium Arms: " + str(stats["mArm"])).grid(row=4, column=3)
    Label(sheetwin, text="Heavy Arms: " + str(stats["hArm"])).grid(row=4, column=4)
    Label(sheetwin, text="Long Range: " + str(stats["lRange"])).grid(row=5, column=2)
    Label(sheetwin, text="Short Range: " + str(stats["sRange"])).grid(row=5, column=3)
    Label(sheetwin, text="Grenades: " + str(stats["gre"])).grid(row=5, column=4)
    """
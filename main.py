from tkinter import *
from screens import newCharacterMenu, newSquadmateMenu, characterSheet, roster, armory
from objects import weapons
import json
from tutorial import tutorialMain

root = Tk()

v = StringVar()
Label(root, textvariable=v).pack()

def newCharacter():
    with open('game.json', 'r') as f:
        characters = json.load(f)
    if characters == {}:
        newCharacterMenu.new(root)
    else:
        warning.set("You have already created a character!")


def sheet():
    with open('game.json', 'r') as f:
        characters = json.load(f)
    if characters == {}:
        warning.set("You Have to create a character first!")
    else:
        characterSheet.sheet(root)

root.title("Text Royale!")
root.minsize(400,200)
v = "Welcome to Text Royale! Created by Ronovo"
label = Label(root, text=v)
label.pack()

with open('game.json', 'r') as f:
    characters = json.load(f)

def squadmate():
    with open('game.json', 'r') as f:
        characters = json.load(f)
    if characters == {}:
        Label(root, text="You Have to create a leader first!").pack()
    elif 0 < len(characters) < 4:
        newSquadmateMenu.new(root)
    else:
        Label(root, text="You Have A Full Squad!").pack()

def callRoster():
    with open('game.json', 'r') as f:
        characters = json.load(f)
    if characters == {}:
        Label(root, text="You Have to create a leader first!").pack()
    else:
        roster.rosterSheet(root)

def firstBattle():
    with open('game.json', 'r') as f:
        characters = json.load(f)
    if characters == {}:
        warning.set("You Have to create a character first!")
    else:
        tutorialMain.tutorialMainThread(root)

def callArmory():
    with open('game.json', 'r') as f:
        characters = json.load(f)
    if characters == {}:
        warning.set("You Have to create a character first!")
    else:
        armory.new(root)


def delete():
    with open('game.json', 'r') as f:
        character = json.load(f)
    if character == {}:
        warning.set("Character does not exist")
    else:
        character = {}
        with open('game.json', 'w') as f:
            json.dump(character, f)
        warning.set("Character Deleted")


button1 = Button(root, text="Create New Character", command=newCharacter)
button1.pack()

button2 = Button(root, text="Character Sheet", command=sheet)
button2.pack()

button3 = Button(root, text="Delete Character", command=delete)
button3.pack()

#SquadMates removed from MVP
'''
button3 = Button(root, text="Add New Squadmate", command=squadmate)
button3.pack()

button4 = Button(root, text="Squad Roster", command=callRoster)
button4.pack()
'''
button5 = Button(root, text="Armory", command=callArmory)
button5.pack()

# button6 = Button(root, text="Start Tutorial", command=firstBattle)
# button6.pack()

close_button = Button(root, text="Close", command=root.quit)
close_button.pack()

warning = StringVar()
warning.set("")
Label(root, textvariable=warning).pack()


root.mainloop()
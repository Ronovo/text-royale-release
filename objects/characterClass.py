from tkinter import *


class Stats:
    def __init__(self, endurance, sArms, mArms, hArms, grenade, lRange, sRange):
        self.end = endurance
        self.sArms = sArms
        self.mArms = mArms
        self.hArms = hArms
        self.grenade = grenade
        self.lRange = lRange
        self.sRange = sRange


class Preset:
    def __init__(self, name, health, stats):
        self.name = name
        self.health = health
        self.stats = stats


# All Classes Preloaded with Stats
# Skill Order = E SA MA LA G LR SR
soldier = Preset("Soldier", 200, Stats(0, 0, 0, 0, 0, 0, 0))
sniper = Preset("Sniper", 200, Stats(2, 0, -2, 2, -2, 4, -2))#2
berzerker = Preset("Berzerker", 200, Stats(0, 0, 2, -2, 2, -2, 2))#2
heavyGunner = Preset("Heavy Gunner", 200, Stats(-2, -4, 4, 4, 0, 0, 0))#2
scout = Preset("Scout", 200, Stats(4, 2, 0, -4, -2, -2, 4))#2


def display(name, newwin):
    displayClass = Toplevel(newwin)
    selected = getSelectedClass(name)
    Label(displayClass, text="You have selected " + selected.name).grid(row=0, column=3)
    stats = selected.stats
    Label(displayClass, text="Endurance: " + str(stats.end)).grid(row=1, column=3)
    Label(displayClass, text="Small Arms: " + str(stats.sArms)).grid(row=2, column=2)
    Label(displayClass, text="Medium Arms: " + str(stats.mArms)).grid(row=2, column=3)
    Label(displayClass, text="Heavy Arms: " + str(stats.sArms)).grid(row=2, column=4)
    Label(displayClass, text="Long Range: " + str(stats.lRange)).grid(row=3, column=2)
    Label(displayClass, text="Short Range: " + str(stats.sRange)).grid(row=3, column=3)
    Label(displayClass, text="Grenades: " + str(stats.grenade)).grid(row=3, column=4)



def getSelectedClass(name):
    if(name == "Soldier"):
        return soldier
    elif(name == "Sniper"):
        return sniper
    elif (name == "Berzerker"):
        return berzerker
    elif (name == "Heavy Gunner"):
        return heavyGunner
    elif (name == "Scout"):
        return scout
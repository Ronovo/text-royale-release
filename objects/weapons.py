from tkinter import *
from screens import range


class Preset:
    def __init__(self, name, maxAmmo, currentAmmo, damage, rangeM, baseAccuracy, weaponType):
        self.name = name
        self.maxAmmo = maxAmmo
        self.currentAmmo = currentAmmo
        self.damage = damage
        self.rangeM = rangeM
        self.baseAccuracy = baseAccuracy
        self.weaponType = weaponType

    def reload(self):
        self.currentAmmo = self.maxAmmo


class WeaponType:
    def __init__(self, className, type):
        self.className = className
        self.type = type


# REMEMBER TO ADD TO WEAPON LIST IN METHOD getWeaponList() if you create it here
# Pistols
# Skill Order = N MA CA D R BA WT
m1911 = Preset("M1911", 7, 0, 50, 100, 80, WeaponType("Pistol", "Small Arms"))  # 20%
usp45 = Preset("USP .45", 12, 0, 50, 200, 85, WeaponType("Pistol", "Small Arms"))  # 15%
m9 = Preset("M9", 15, 0, 75, 150, 85, WeaponType("Pistol", "Small Arms"))  # 15%
deserteagle = Preset("Desert Eagle", 7, 0, 100, 100, 90, WeaponType("Pistol", "Small Arms"))  # 10%

# SMG
# Skill Order = N MA CA D R BA WT
mp5 = Preset("MP5", 30, 0, 50, 300, 88, WeaponType("SMG", "Small Arms"))  # 12 %
ak47u = Preset("AK-47u", 30, 0, 75, 250, 90, WeaponType("SMG", "Small Arms"))  # 10 %
p90 = Preset("P90", 50, 0, 40, 350, 88, WeaponType("SMG", "Small Arms"))  # 12 %
miniuzi = Preset("Mini-Uzi", 32, 0, 40, 200, 85, WeaponType("SMG", "Small Arms"))  # 15 %

# Shotguns
# Skill Order = N MA CA D R BA WT
w1200 = Preset("W1200", 7, 0, 75, 200, 88, WeaponType("Shotgun", "Medium Arms"))  # 12%
m1014 = Preset("M1014", 4, 0, 100, 250, 90, WeaponType("Shotgun", "Medium Arms"))  # 10%

# Assault Rifles
# Skill Order = N MA CA D R BA WT
m16a4 = Preset("M16A4", 30, 0, 70, 400, 86, WeaponType("Assault", "Medium Arms"))  # 14%
ak47 = Preset("AK47", 30, 0, 100, 300, 92, WeaponType("Assault", "Medium Arms"))  # 8%
g3 = Preset("G3", 20, 0, 50, 500, 92, WeaponType("Assault", "Medium Arms"))  # 8%

# Sniper(High Skill Cap, more power, high accurary
# Skill Order = N MA CA D R BA WT
m40a3 = Preset("M40A3", 5, 0, 100, 500, 95, WeaponType("Sniper", "Large Arms"))  # 5%
dragunov = Preset("Dragunov", 20, 0, 150, 500, 97, WeaponType("Sniper", "Large Arms"))  # 3%
b50cal = Preset("Barrett .50Cal", 10, 0, 200, 500, 99, WeaponType("Sniper", "Large Arms"))  # 1%

# LMG
# Skill Order = N MA CA D R BA WT
m249 = Preset("M249 SAW", 100, 0, 30, 300, 95, WeaponType("LMG", "Large Arms"))  # 5%
m60e4 = Preset("M60E4", 100, 0, 50, 200, 97, WeaponType("LMG", "Large Arms"))  # 3%
rpd = Preset("RPD", 100, 0, 50, 300, 95, WeaponType("LMG", "Large Arms"))


def getWeaponList():
    weaponList = [m1911, usp45, m9, deserteagle, mp5, ak47u, p90, miniuzi, w1200, m1014,
                  m16a4, ak47, g3, m40a3, dragunov, b50cal, m249, m60e4, rpd]
    return weaponList


def display(name, newwin):
    displayClass = Toplevel(newwin)
    selected = getWeaponByName(name)
    Label(displayClass, text="You have selected " + selected.name).grid(row=0, column=3)
    Label(displayClass, text="Max Ammo: " + str(selected.maxAmmo)).grid(row=1, column=2)
    Label(displayClass, text="Damage: " + str(selected.damage)).grid(row=1, column=3)
    Label(displayClass, text="Range in Meters: " + str(selected.rangeM)).grid(row=1, column=4)
    Label(displayClass, text="Base Accuracy: " + str(selected.baseAccuracy)).grid(row=2, column=2)
    weaponType = selected.weaponType
    Label(displayClass, text="Class: " + str(weaponType.className)).grid(row=2, column=4)
    Label(displayClass, text="Weapon Type: " + str(weaponType.type)).grid(row=3, column=3)
    def callback():
        range.new(newwin, selected)
        displayClass.destroy()
    Button(displayClass, text="Test on Range", command=callback).grid(row=5, column=3)


def getWeaponListByWeaponType(wType):
    weapons = getWeaponList()
    sendlist = []
    for x in weapons:
        y = x.weaponType.type
        if y == wType:
            sendlist.append(x)
    return sendlist

def getWeaponByName(name):
    weapons = getWeaponList()
    for x in weapons:
        y = x.name
        if y == name:
            return x

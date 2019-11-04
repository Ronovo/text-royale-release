import random
import json
from tkinter import END


def roll(number):
    return random.randint(1, number)


# Base 100 Roll.
# Check Against Base Accuracy
# Factors:
# Distance
def simpleHit(selectedWeapon, dummy, st):
    with open('game.json', 'r') as f:
        character = json.load(f)
    stats = character["stats"]
    baseResult = roll(100)
    distance = int(dummy["distance"])
    rangeM = int(selectedWeapon.rangeM)
    isSniper = False
    if selectedWeapon.weaponType.className == "Sniper":
        isSniper = True
    # CHECKS BASED ON WEAPON FIRST, BEFORE CHARACTER RANGE CHECKS
    farRange = 0
    closeRange = 0
    # Close Range Bonus
    if distance < rangeM:
        closeRange = rangeM - distance
        y = closeRange // 50
        # This Check Makes Sure that Sniper at Max Range doesn't get +12
        if isSniper and y > 3:
            y = 4
        for x in range(0, y):
            baseResult += 2
    # Long Range Penalty
    elif distance > rangeM:
        farRange = distance - rangeM
        y = farRange // 50
        for x in range(0, y):
            baseResult -= 2

    # CHARACTER CHECKS
    baseResult = characterCheckFarRange(farRange, stats, baseResult)
    baseResult = characterCheckCloseRange(closeRange, stats, baseResult)
    baseResult = characterCheckHeavy(selectedWeapon, stats, baseResult)
    baseResult = characterCheckMedium(selectedWeapon, stats, baseResult)
    baseResult = characterCheckSmall(selectedWeapon, stats, baseResult)


    #Final Check
    #Hit
    if baseResult > selectedWeapon.baseAccuracy:
        dummy["health"] -= selectedWeapon.damage
        dummyhealth = "Dummy Health now " + str(dummy["health"]) + "\n"
        st.insert(END, dummyhealth)
        st.see("end")
    #Or Miss
    else:
        st.insert(END, "Miss!\n")
        st.see("end")


def characterCheckFarRange(farRange, stats, baseResult):
    # Clase Far Range Bonus/Penelty Check
    if farRange != 0:
        lRange = stats["lRange"]
        baseResult = characterBonusBase(lRange, baseResult)
    return baseResult


def characterCheckCloseRange(closeRange, stats, baseResult):
    # Class Close Range Bonus/Penelty Check
    if closeRange != 0:
        sRange = stats["sRange"]
        baseResult = characterBonusBase(sRange, baseResult)
    return baseResult

def characterCheckHeavy(selectedWeapon, stats, baseResult):
    hArm = stats["hArm"]
    weaponType = selectedWeapon.weaponType
    type = weaponType.type
    if type == "Large Arms":
        baseResult = characterBonusBase(hArm, baseResult)
    return baseResult

def characterCheckMedium(selectedWeapon, stats, baseResult):
    mArm = stats["mArm"]
    weaponType = selectedWeapon.weaponType
    type = weaponType.type
    if type == "Medium Arms":
        baseResult = characterBonusBase(mArm, baseResult)
    return baseResult

def characterCheckSmall(selectedWeapon, stats, baseResult):
    sArm = stats["sArm"]
    weaponType = selectedWeapon.weaponType
    type = weaponType.type
    if type == "Small Arms":
        baseResult = characterBonusBase(sArm, baseResult)
    return baseResult

def characterBonusBase(stat, baseResult):
    if stat == 2:
        baseResult += 5
    elif stat == 1:
        baseResult += 10
    elif stat == -1:
        baseResult -= 5
    elif stat == -2:
        baseResult -= 10
    return baseResult
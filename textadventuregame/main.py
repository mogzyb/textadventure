import random

treasure = 0
lives = 5
turns = 0
global torch
global whips


def dice_roll():
    return random.randint(1, 20)

def search_room():
    global torch
    global whips
    roll = dice_roll()
    if(torch):
        roll+=3
    if(roll < 6):
        print("The ceiling falls in!")
    elif(roll >= 6 and roll <= 10):
        print("Find  trap")
    elif(roll >=10 and roll <=14):
        if(torch):
            print("You found another torch")
        else:
            torch = True
    elif(roll >= 15 and roll <= 18):
        print("You found a whip")
        whips += 1
    else:
        print("Yeah you found Treasure!")


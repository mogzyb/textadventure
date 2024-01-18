import random

#personal details
player_name = "No Name"

#game state
treasure = 0
lives = 5
turns = 0
torch = 0
whips = 0

#inputs
current_input = ""

#template class we can reuse to randomly generate rooms
class Room:
    torch_chance = 0
    #fill in rest of room stuff here


def game_start():
    global player_name
    print("Welcome to text adventure game!")
    player_name = prompt_input_with_confirmation("Please Enter Your Player Name: ")
    print(f"Welcome {player_name}, a long hard journey awaits, who knows what lies ahead! "
          f"Fame? Glory? Treasure?")

    #start core game loop
    game_loop()

def game_loop():
    #generate next room/dungeon

    #choose room function

    #give player option to search room or go next room maybe give them 3 options? 1, 2 or 3


    print("here to stop error - remove")

#roll dice for all possible random room events e.g. torch spawn etc.
def generate_room():
    #dice rolls
    torch_spawn = dice_roll(0)
    #write all dice rolls for room here

    #assign values to room object


#dice roll with modifier e.g. -3 or +3 for effects on player e.g. has torch
#if no modifier just pass a 0
def dice_roll(modifier):
    return random.randint(1, 20) + modifier

def prompt_input_with_confirmation(prompt_text):
    return_value = input(prompt_text)
    user_confirmed = False

    #this is called when we call confirm_input() seen below
    def confirm_input():
        yes_or_no = input(f"Please confirm that you intended to type: {return_value}. Y/N ")
        if yes_or_no.upper() == "Y":
            #user entered correctly - returning the value
            nonlocal user_confirmed
            user_confirmed = True
        elif yes_or_no == "N":
            #if no restart prompt question so user can type in again
            prompt_input_with_confirmation(prompt_text)

    confirm_input()

    if user_confirmed == True:
        return return_value



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

game_start()
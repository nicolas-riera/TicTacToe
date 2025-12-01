# Librairies
import random
import time

# Variables 
grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Functions

# Empties the console
def clear():
    for i in range(60):
        print("")
        
def player_selection():
    clear()
    print("Tic Tac Toe")
    print("")
    print("1. Un Joueur")
    print("2. Deux Joueurs")
    print("")

    selection = input("")
    if selection == "1" or selection == "2":
        return int(selection)
    else:
        player_selection()

def displaygrid_cli():
    clear()
    global grid
    print("-------------")
    for i in range(0, len(grid), 3):
        line = "| "
        for j in range(i, i+3):
            match grid[j]:
                case "X":
                    line += " X "
                case "O" :
                    line += " O "
                case _:
                    line += "   "
        line += " |"
        print(line)
    print("-------------")

def replay():
    print("")
    match input("Vous voulez rejouer (Oui/Non) : ").lower():
        case "oui":
            global grid
            grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            return True
        case "non":
            return False
        case _:
            replay()

def placesymbol(value):

    global grid

    if value == "player1":
        print("")
        place = input("Où voulez-vous placer votre symbole (1-9) : ")
        match place:
            case "1":
                if grid[int(place)-1] == 0:
                    grid[int(place)-1] = "X"
                else:
                    print("")
                    print("Case déjà remplie")
                    time.sleep(3)
                    player_solo_play()
            case "2":
                grid[int(place)-1] = "X"
            case "3":
                grid[int(place)-1] = "X"
            case "4":
                grid[int(place)-1] = "X"
            case "5":
                grid[int(place)-1] = "X"
            case "6":
                grid[int(place)-1] = "X"
            case "7":
                grid[int(place)-1] = "X"
            case "8":
                grid[int(place)-1] = "X"
            case "9":
                grid[int(place)-1] = "X"
            case _:
                print("")
                print("Saisie incorrecte")
                time.sleep(3)
                player_solo_play()

def player_solo_play():

    global grid

    displaygrid_cli()
    placesymbol("player1")
    
    if 0 in grid:
        return True
    else:
        return replay()

# Main program

if player_selection() == 1:
    while True:
        if player_solo_play():
            continue
        else:
            break

else:
    while True:
        print("")
# Librairies
from game import *

# Main program

if player_selection() == 1:
    while True:
        if player_solo_play():
            continue
        else:
            break

else:
    while True:
        if player_duo_play():
            continue
        else:
            break
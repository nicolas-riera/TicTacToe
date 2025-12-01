# Librairies
from game import *

# Main program

if player_selection() == 1:
    # Loop for single-player mode
    while True:
        if player_solo_play():
            continue
        else:
            break

else:
    # Loop for two-player mode
    while True:
        if player_duo_play():
            continue
        else:
            break
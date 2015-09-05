import random
from random import randint

__author__ = 'Venigma aka: George Bowles'


print "Welcome to battleships\n"
# Add credits and stuff here

PlayerName = raw_input("Your Name: ")  # Stores Users Name

print "Hello " + PlayerName

# //////////////////////////////////////////Navy or Pirates?\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

SideCorrect = "True"  # Tells while loop if PlayerSide (Line 21) is ok for use

PlayerSide = ""

while SideCorrect:
    print "\n\nPlease Choose Your Side: Navy or Pirates\n"

    PlayerSide = raw_input("Your Side: ")  # PlayerSide stores Navy or Pirates acoording to input

    if PlayerSide == "navy" or PlayerSide == "Navy" or PlayerSide == "n":  # remove "n" eventually
        PlayerSide = "Navy"
        SideCorrect = "True"
        break

    elif PlayerSide == "pirates" or PlayerSide == "Pirates":
        PlayerSide = "Pirates"
        SideCorrect = "True"
        break

    else:
        print "\nPlease enter either Navy or Pirates and check spelling"
        SideCorrect = "False"

# /////////////////////////////////////////////Player Team Name\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Collapsed Below: Explains what user should input


print """\n\nPlease choose your country (for Navy) or name (for Pirates) e.g. The Austrailian Navy or The Pirates of \
the Caribbean

Please Note: Navy Names (the Country) go before the word Navy and Pirate Names go after the word Pirate and please dont\
 enter 'The'.
For Example: if  you want to be called 'The British Navy' simply enter 'British' if you want to be 'The Pirates of the \
Caribbean' then enter 'of the Caribbean'.\n"""


SideName = raw_input("Your Team/Sides Name: ")  # SideName stores user entered name of team


if PlayerSide == "Pirates":
    Side = "The Pirates " + SideName  # Side - combonation of SideName and PlayerSide
elif PlayerSide == "Navy":
    Side = "The " + SideName + " Navy"
else:
    Side = SideName

print "\n\nYou are known as " + Side

# //////////////////////////////////////////////////CPUs Name\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
CPUSideDictPirates = ['Caribbean', ]
# /\ List of randomised Pirate crew names

CPUSideDictNavy = ['Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Argentinean', 'Armenian',
                   'Australian', 'Austrian', 'Bangladeshi', 'Barbadian', 'Belarusian', 'Belgian', 'Belizean',
                   'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian',
                   'Burkinabe', 'Burmese', 'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean',
                   'Central African', 'Chadian', 'Chilean', 'Chinese', 'Colombian', 'Comoran', 'Congolese',
                   'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djibouti', 'Dominican',
                   'Dutch', 'East Timorese', 'Ecuadorean', 'Egyptian', 'Emirian', 'Equatorial Guinean', 'Eritrean',
                   'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French', 'Gabonese', 'Gambian',
                   'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan',
                   'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'Icelander', 'Indian',
                   'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese',
                   'Jordanian', 'Kazakhstani', ' Kenyan', 'Kittian']
# /\ List of Naval Names (Nationalities)

CPUSideFinal = " "


def cpunamepick(names):  # Picks name from lists above
    if names:
        index = random.randrange(len(names))
        return names.pop(index)
    return None

# If Player is on Navy CPU is on Pirates; If Player is on Pirates CPU is on Navy

if PlayerSide == "Navy":
    CPUSide = "Pirates"  # CPUSide - Stores CPU Side
    CPUSideName = cpunamepick(CPUSideDictPirates)  # CPUSideName - Stores result from cpunamepick()
    CPUSideFinal = "The Pirates of the " + CPUSideName  # CPUSideFinal - Stores combonation of CPUSide + CPUSideName

elif PlayerSide == "Pirates":
    CPUSide = "Navy"
    CPUSideName = cpunamepick(CPUSideDictNavy)
    CPUSideFinal = "The " + CPUSideName + " Navy"

else:
    print "Oops something went horribly wrong"
    exit()  # almost impossible to get here, code quits to avoid errors

print "\nYour Opponent is known as " + CPUSideFinal

Tutorialq = raw_input("\n\nWould you like to take the short tutorial? Yes or No? ")


def tutorial():
    print "\nWelcome to the Tutorial\n"
    print "------Coordinates------"
    print "You can enter any number from 0 to 4 in Guess Row or Guess Column"
    print "---------Grid----------"
    print "This is the grid:"
    print """
              0 1 2 3 4
             0 ~ ~ ~ ~ ~
             1 ~ ~ ~ ~ ~
             2 ~ ~ ~ ~ ~
             3 ~ ~ ~ ~ ~
             4 ~ ~ ~ ~ ~\n"""
    print "You will see it before and after every turn,\nIf you see an O that means you tried there before and missed."
    print "If you see a X that means you tried there before and hit"
    raw_input("\n\nPress the enter key to play\n")
    return None


if Tutorialq == "Yes" or Tutorialq == "yes" or Tutorialq == "y" or Tutorialq == "Y":
    tutorial()
else:
    print "Ok, Game is Starting"


# //////////////////////////////////////////////Game Setup\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# CPU Board

board = []  # Empty board list

for x in range(0, 5):
    board.append(["~"] * 5)  # Creates a 5x5 grid of ~'s


def print_board(board):
    for row in board:
        print " " .join(row)  # " ".join(row) gets rid of commas in list

# Player Board
# ADD PLAYER OWN CHOOSE SHIP POSTIONS
player_board = []  # Empty board list

for n in range(0, 5):
    player_board.append(["~"] * 5)  # Creates a 5x5 grid of ~'s


def print_player_board(board):
    for row in board:
        print " " .join(row)  # " ".join(row) gets rid of commas in list
# ////////////////////////////////////////Game Start\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print "Here is a guide of the grid:"
print """
               0 1 2 3 4
             0 ~ ~ ~ ~ ~
             1 ~ ~ ~ ~ ~
             2 ~ ~ ~ ~ ~
             3 ~ ~ ~ ~ ~
             4 ~ ~ ~ ~ ~\n"""

print_player_board(player_board)


print "You have 4 Ships, choose where to put them"

# Ship 1
chose1right = "False"
while chose1right:
    playership1row = int(raw_input("Ship 1 row: "))
    playership1col = int(raw_input("Ship 1 Column: "))
    player_board[playership1row][playership1col] = "V"
    if playership1row not in range(5) or playership1col not in range(5):
        chose1right = "False"
        print "Hmm, they dont seem to be correct coordinates. Try that ship again"
    else:
        chose1right = "True"
        break
# Ship 2
playership2row = int(raw_input("Ship 2 row: "))
playership2col = int(raw_input("Ship 2 Column: "))
player_board[playership2row][playership2col] = "V"
# Ship 3
playership3row = int(raw_input("Ship 3 row: "))
playership3col = int(raw_input("Ship 3 Column: "))
player_board[playership3row][playership3col] = "V"
# Ship 4
playership4row = int(raw_input("Ship 4 row: "))
playership4col = int(raw_input("Ship 4 Column: "))
player_board[playership4row][playership4col] = "V"

# if playership1row not in range(5) or playership1col not in range(5) or playership2row not in range(5) or playership2col not in range(5)or or or :

print_player_board(player_board)


print "\n\n\nYour Turn\n"
print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_col(board)
ship_col = random_row(board)

print ship_row  # DEBUG OFF
print ship_col  # DEBUG OFF

goworked = "False"

while goworked:
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Column: "))

    if guess_row not in range(5) or guess_col not in range(5):
            print "\nBe careful were you aim that thing, sailor! \nYou missed entirely, remember the coordinates are \
            from 0,0 to 4,4."
            goworked = "False"

    elif guess_row == ship_row and guess_col == ship_col:
        print "\nThats a hit, good work, sailor"
        board[guess_row][guess_col] = "X"
        goworked = "True"
        break

    elif board[guess_row][guess_col] == "O" or board[guess_row][guess_col] == "X":
        print "\nYou have already tried those coordinates.Try again. "
        print_board(board)
        goworked = "False"

    else:
        print "\nOh dear, you missed, have another try in a minute."
        board[guess_row][guess_col] = "O"
        print print_board(board)
        goworked = "True"
        break

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def number_to_name(number):
    # fill in your code below
        
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard" 
    else:
        name = "scissors"
    #print number
    return name

    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    else:
        number = 4
    #print number
    return number

def rpsls(name): 
    # fill in your code below
    
    # convert name to player_number using name_to_number
    player_name  = name_to_number(name)
    #print player_name
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)
    #print player_name
    #print comp_number
    # compute difference of player_number and comp_number modulo five
    result = int(player_name) - int(comp_number)
    #print result
    # use if/elif/else to determine winner
    if result < 0:
        result = 5 + result
        
    if result == 1 or result == 2:
        winner = "Player"
    elif result == 3 or result == 4:
        winner = "Computer"
    else:
        winner = "tie"
    # convert comp_number to name using number_to_name
    comp_choice = number_to_name(comp_number)
    # print results
    print "Player chooses " + name
    print "Computer chooses " + comp_choice
    if winner != "tie":
        print winner + " wins!\n"
    else:
        print "Player and computer tie!\n"
    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



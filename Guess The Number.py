import simplegui
import random
import math


number_range = 100
number_guess = 7
secret_number = random.randrange(0,100)
#print secret_number

def new_game ():
    global number_range
    global number_guess
    global secret_number
    #print secret_number
    number_guess = math.ceil (math.log( number_range +1, 2))
    print "Welcome!"
    print "Please choose a number between 0 and ", number_range
    print "Chances to win: ", number_guess
    print " "


def range100():
    global secret_number
    #print secret_number
    global number_guess
    global number_range
    number_range = 100
    secret_number = random.randrange(0,100)
    #print secret_number
    new_game()

def range1000():
    global secret_number
    #print secret_number
    global number_range
    number_range = 1000
    secret_number = random.randrange(0,1000)
    #print secret_number
    new_game()

def get_input(guess):
    global secret_number
    global number_guess
    number_guess -= 1
    guess = int(guess)
    #print secret_number

    print "You picked the number: ", guess
    

    if number_guess >= 0:
        if guess > secret_number:
            print "Keep trying, go LOWER!"
            #print secret_number
            print "Chances left to win: ", number_guess
        elif guess < secret_number:
            print "Keep trying, go HIGHER!"
            #print secret_number
            print "Chances left to win: ", number_guess

        elif guess == secret_number:
            print "You are Correct!"
            print "YOU WIN!" 
            print " "
            new_game()
    else:
        
       print "You have run out of chances to win." 
       print "The correct number was: ", secret_number
        
       print " "
       new_game()
    print " "

frame = simplegui.create_frame("Guess The Number", 200, 200)
frame.add_button("Range [0,100)", range100, 200)
frame.add_button("Range [0,1000)", range1000, 200)
frame.add_input("Choose A Number", get_input, 200)
frame.set_canvas_background('silver')
frame.start()

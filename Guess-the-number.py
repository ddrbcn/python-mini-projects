# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
low = 0
high = 100
secret_number = 0
guess = 0
remaining_guesses = 0


# helper function to start and restart the game
def new_game():
    
    global low, high, secret_number, remaining_guesses
    
    secret_number = random.randrange(low, high)
    remaining_guesses = int(math.ceil(math.log(high-low, 2)))
    
    print "************************************************"
    print "New game. Range is from " + str(low) + " to " + str(high) + "."
    print "Number of remaining guesses is "+ str(remaining_guesses) + "."
    print
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global low, high
    low = 0
    high = 100
    new_game()
   

def range1000():
    # button that changes range to range [0,1000) and restarts
    global low, high
    low = 0
    high = 1000    
    new_game()
 
    
def input_guess(player_guess):
    # main game logic goes here
    global guess, remaining_guesses, secret_number
    guess = float(player_guess)
        
    remaining_guesses-=1
    
    print
    print "Guess was " + player_guess
    print "Number of remaining guesses is " + str(remaining_guesses)
    
    if guess < secret_number and remaining_guesses > 0:
        print "Higher!"
        
    elif guess > secret_number and remaining_guesses > 0:
        print "Lower!"
        
    elif guess == secret_number:
        
        print "Correct!"
        print "************************************************"
        print
        new_game()
        
    
    else:
        print "You ran out of guesses. The number was " + str(secret_number)
        print "************************************************"
        print
        new_game()
        
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 150)
frame.add_button("Range: 0 - 1000", range1000, 150)
frame.add_input("Enter a guess:", input_guess, 150)


# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric

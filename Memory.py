# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global turn_counter, deck, exposed, state, prev_clicked_card1, prev_clicked_card2
    
    state=0
    prev_clicked_card1 = -1
    prev_clicked_card2 = -1
    turn_counter = 0
    label.set_text("Turns = "+ str(turn_counter))
    #Defining the deck
    deck = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    exposed =[ False,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    
    #Shuffling the deck
    random.shuffle(deck)
    
     
# define event handlers
def mouseclick(pos):
    global turn_counter, index_clicked_card, exposed, state, prev_clicked_card1, prev_clicked_card2, deck
    # add game state logic here
    
    index_clicked_card = pos[0]/50
    
    if exposed[index_clicked_card] == False:
        if state == 0:
            
            prev_clicked_card2 = prev_clicked_card1
            prev_clicked_card1 = index_clicked_card
            
            state = 1
            exposed[index_clicked_card]= True
            
        elif state == 1:

            prev_clicked_card2 = prev_clicked_card1
            prev_clicked_card1 = index_clicked_card
                
            state = 2
            turn_counter +=1
            label.set_text("Turns = "+ str(turn_counter))
            exposed[index_clicked_card] = True

        else:
            if deck[prev_clicked_card1] != deck[prev_clicked_card2]:
            
                exposed[prev_clicked_card1] = False
                exposed[prev_clicked_card2] = False
                
            exposed[index_clicked_card]= True
            prev_clicked_card1 = index_clicked_card

            state = 1  
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    for i in range(16):
        if exposed[i]==True:
            canvas.draw_text(str(deck[i]), (i*50+12, 62), 44, 'White')
        else:
            canvas.draw_polygon([(i*50, 0), ((i+1)*50-1, 0), ((i+1)*50-1, 100-1), (i*50-1, 100-1)], 1, 'Black', 'Green')
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
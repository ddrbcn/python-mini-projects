# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
outcome_winner = ""
score = 0



# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            self.face_up = True
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        
        # create Hand object
        self.cards = []
        self.has_ace = False

    def __str__(self):
        
        # return a string representation of a hand
        return str([str(x) for x in self.cards])
    
    
    def add_card(self, card):
        
        # add a card object to a hand
        self.cards.append(card)
        if card.get_rank() == "A":
            self.has_ace = True
            print "Hand has an Ace"
        
    def get_value(self):
        # compute the value of the hand
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        global VALUES
        value = 0
        for card in self.cards:
                       
            value += VALUES[card.get_rank()]
            
        if self.has_ace and (value <= 21-10):
            value += 10
            
        return value        
            
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        index =0
        for card in self.cards:
            
            card.draw(canvas, [pos[0] + CARD_SIZE[0]*index, pos[1]])
            index += 1
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        
        self.cards = []
        
        for suit in  SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
                

    def shuffle(self):
        # shuffle the deck 
        # uses random.shuffle()
        
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
       # return a string representing the deck
       return str([str(x) for x in self.cards]) 


#define event handlers for buttons

def deal():
    #shuffles the deck and deals the two cards to both the dealer and the player.
    
    global outcome, outcome_winner, in_play, player_hand, dealer_hand, deck, score
    
    
    if in_play:
        '''
        The program reports that the player lost the round and updates the score appropriately.
        Here I take into account item 6 from Phase two of the Mini-project development process.
        Taking into account this item we must first report that the player lost the round.
        Then in_play is set to False and you can press Deal button again in order to get two
        new hands for Player and Dealer.
        '''
        score -= 1
        outcome_winner = "You lost the round."
        outcome = "Press Deal to continue..."
        in_play = False
    else:
        outcome = "Hit or stand?"
        outcome_winner = ""
    
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
    
    
        deck.shuffle()
    
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        print "Player's hand: " + str(player_hand)
        print "Dealer's hand: " + str(dealer_hand)
    
    
        in_play = True
          
   
    
    

def hit():
    
    global deck, player_hand, in_play, score, outcome, outcome_winner
    # if the hand is in play, hit the player
    if in_play:
        
        if player_hand.get_value() <=21:
            
            player_hand.add_card(deck.deal_card())
            
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome_winner = "You have busted and lose."
            outcome = "New deal?"
            print "You have busted."
            score -= 1
            in_play = False
            
def stand():

    global dealer_hand, player_hand, deck, in_play, score, outcome, outcome_winner
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    
    if in_play:
        if player_hand.get_value() > 21:
            print "This is just a quick reminder that you have busted."
        else:
            
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal_card())
            
            if (dealer_hand.get_value() > 21):
                outcome = "New deal?"
                outcome_winner = "Dealer has busted and you won."
                in_play = False
                print "Dealer has busted."
                score += 1
            else:
                if (dealer_hand.get_value() >= player_hand.get_value()):
                    outcome_winner = "Dealer won."
                    outcome = "New deal?"
                    in_play = False
                    print "Dealer won."
                    score -= 1
                else:
                    outcome_winner = "Player won."
                    outcome = "New deal?"
                    in_play = False
                    print "Player won."
                    
                    score += 1
    
        print str(player_hand.get_value())
        print str(dealer_hand.get_value())
    
                   
     
                  
        
         
   
            
            
        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome, in_play, card_back, score
    
    dealer_pos = [40, 160]
    
    player_hand.draw(canvas, [40, 460])
    dealer_hand.draw(canvas, dealer_pos)
    
    if in_play:
        
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0] , 
                    CARD_BACK_CENTER[1] + CARD_BACK_SIZE[1])
        
        #canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [dealer_pos[0] + CARD_BACK_CENTER[0], dealer_pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [40 + CARD_BACK_CENTER[0], 160 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)    
        
    canvas.draw_text("Player", (30, 440), 22, 'Black') 
    canvas.draw_text("Dealer", (30, 150), 22, 'Black') 
    canvas.draw_text(outcome, (300, 440), 22, 'Black') 
    canvas.draw_text(outcome_winner, (240, 150), 22, 'Black') 
    canvas.draw_text("Blackjack", (180, 80), 60, 'Black')
    canvas.draw_text("Score "+ str(score), (260, 350), 30, 'Black') 
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
import random, os

'''

Red dog is a card game of chance.
The game only uses three cards at a time, which are ranked as in poker, with aces high. Suit is irrelevant. A wager is placed, and two cards are placed face up on the table, with three possible outcomes:
If the cards are consecutive in number (for example, a four and a five, or a jack and a queen), the hand is a push and the player's wager is returned.
If the two cards are of equal value, a third card is dealt. If the third card is of the same value, then the payout for the player is 11:1, otherwise the hand is a push.
If neither of the above is the case (for example, a three and an eight), then a spread is announced which determines the payoff (a 4-card spread, in this example), and a third card will be dealt. 
Before dealing the third card, the player has the option to double his bet. If the third card's value falls between the first two, the player will receive a payoff according to the spread; otherwise the bet is lost.
...

#global variables
random_card = 0
players_card = 0
game_card_1 = 0
game_card_2 = 0
player_money = 2000
player_bet = 0
user_input = ""
game_suit_1 = ""
game_suit_2 = ""
player_suit = ""
spread = 100

cards = {1:"Ace", 2:2, 3:3, 4:4, 5:5, 6:6, 7:7,8:8, 9:9,10:10,11:"Jack",12:"Queen", 13:"King"}
suits = ["Spade", "Heart","Diamond", "Club"]




#reset stats
def reset():

    global random_card
    global players_card
    global game_card_1
    global game_card_2
    global player_bet
    global user_input
    
    random_card = 0
    players_card = 0
    game_card_1 = 0
    game_card_2 = 0
    player_bet = 0
    user_input = ""

# program header
def header():
    
    #Start Game
    print "\n"
    title = 'Welcome to game of Red Dog'
    print '=' * (60+len(title)+2)
    print '=' * 20,title,'=' * 40
    print '=' * (60+len(title)+2)
    print ""


    #Rules
    title = '  Rules  '
    
    print '=' * 40,title,'=' * 40
    print "All cards are ranked as in poker, the suit is irrelevant"
    print "Place your bet and dealer places two cards on the table face up."
    print ""
    print "A third card is dealt."
    print "If it falls between the first two cards the player WINS according to spread."
    print "If the two cards are consecutive then the hand is a push."
    print "Any matching of 3 wins the Jackpot 11:1"
    print ""
    print "*This game uses mutitple decks*"
    print " "
    print "Spread | Payout"
    print "---------------|"
    print "1 card | 5 to 1|"
    print "2 card | 4 to 1|"
    print "3 card | 2 to 1|"
    print "4+ card| 1 to 1|"
    print "----------------"
    
    
    print '=' * (80+len(title)+2)


#run main program    
def main():
    
    global player_money
    
    while player_money > 0 :
        draw()
        first_round()
        betting()
        current_standings()
        double_bet()
        next_round()
        final_round()
        values()
        compare()
    else:
        print "\n"
        print "Oh, Im sorry. You're all out of money"
        
        user_input = raw_input("Do you want to play again? (Y/N)")
        if user_input in ["Y", "y"]:
            player_money = 2000
            reset()
            main()
        else:
            print "Good bye"
            os._exit(1)



#draw a random card from the dictionary
def draw():
    global random_card
    i = random.randint(0,len(cards) - 1)
    random_card = cards[list(cards)[i]]
    return random_card
    
#draw first two cards
def first_round():
    global game_card_1
    global game_card_2
    global game_suit_1
    global game_suit_2
    global player_suit
    
    draw()
    game_card_1 = random_card
    draw()
    game_card_2 = random_card   
    values()

    game_suit_1 = random.choice(suits)
    game_suit_2 = random.choice(suits)
    player_suit = random.choice(suits)

    
    print "\n"

# place the bet
def betting():
    global player_bet
    
    print "\n"
    print "*============*"
    print "You have $%d " % player_money
    print "Minumum: $1  "
    print "Maximum: None"
    print "*============*"
    print "\n"

    try:
        player_bet = int(raw_input("How much do you want to bet? "))
        
        if player_bet > player_money:
            print ""
            print "You cant bet more than you have."
            print "Betting maximum amount available"
            player_bet = player_money
            
        if player_bet is not int(player_bet):
            print "Please enter a numeric value."
            betting()
        else:
            player_bet = int(player_bet)
    except ValueError:
        print "Please enter a numeric Value"
        main()
    except IOError:
        print "I/O Error"



#print the standing of the game
def current_standings():
    global player_bet
    global game_card_2
    global game_card_1
    global game_suit_1
    global game_suit_2
    
    print "\n"
    print "    Current standings"
    print "*==========================*"
    print "      Your bet: $%d       " % player_bet
    print "*==========================*"
    print "   First draw: %s of %s    " % (game_card_1, game_suit_1)
    print "  Second draw: %s of %s    " % (game_card_2, game_suit_2)
    print "*==========================*"

    if game_card_2 == game_card_1 - 1:
        print "\n"
        print "*-----------*"
        print "*  PUSH!    *"
        print "* New round *"
        print "*-----------*"
        main()
    elif game_card_2 == game_card_1 + 1:
        
        print "\n"
        print "*-----------*"
        print "*  PUSH!    *"
        print "* New round *"
        print "*-----------*"
        main()
        
    print "\n"


#ask if the player wants to double the bet
def double_bet():
    global player_bet
    global game_card_2
    
    user_input = raw_input("Do you want to double your bet? (Y/N) ")

    if user_input in ["Y", "y"]:    
        player_bet = player_bet * 2
        if player_bet > player_money:
            print ""
            print "You cant bet more than you have."
            print "Betting maximum amount available"
            player_bet = player_money
            
        
            


#move to the next round
def next_round():

    global players_card
    
    print "\n"
    print "*==========================*"
    print "    Your bet is $%d         " % player_bet
    print "* Last card has been drawn *"
    print "*==========================*"
    print "\n"
    user_input = raw_input("Press any button to see it.")
    draw()
    players_card = random_card  

    

#assigning numeric values for Ace, Jack, Queen, King
def values():
    
    global players_card
    global game_card_1
    global game_card_2

    
    #player values
    if players_card == cards.get(1):
        players_card = 1
        
    elif players_card == cards.get(11):
        players_card = 11
    elif players_card == cards.get(12):
        players_card = 12
    elif players_card == cards.get(13):
        players_card = 13

     # First card value   
    if game_card_1 == cards.get(1):
        game_card_1 = 1
    elif game_card_1 == cards.get(11):
        game_card_1 = 11
    elif game_card_1 == cards.get(12):
        game_card_1 = 12
    elif game_card_1 == cards.get(13):
        game_card_1 = 13

        
    # second cads values
    if game_card_2 == cards.get(1):
        game_card_2 = 1
    elif game_card_2 == cards.get(11):
        game_card_2 = 11
    elif game_card_2 == cards.get(12):
        game_card_2 = 12
    elif game_card_2 == cards.get(13):
        game_card_2 = 13    



#change Ace, Jack ,Queen, King back to strings  
def change_back():

    global players_card
    global game_card_1
    global game_card_2

    
    #player values
    if players_card == 1:
        players_card = cards.get(1)
        
    elif players_card == 11:
        players_card = cards.get(11)
    elif players_card == 12:
        players_card = cards.get(12)
    elif players_card == 13:
        players_card = cards.get(13)

     # First card value   
    if game_card_1 == 1:
        game_card_1 = cards.get(1)
    elif game_card_1 == 11:
        game_card_1 = cards.get(11)
    elif game_card_1 == 12:
        game_card_1 = cards.get(12)
    elif game_card_1 == 13:
        game_card_1 = cards.get(13)

        
    # second cads values
    if game_card_2 == 1:
        game_card_2 = cards.get(1)
    elif game_card_2 == 11:
        game_card_2 = cards.get(11)
    elif game_card_2 == 12:
        game_card_2 = cards.get(12)
    elif game_card_2 == 13:
        game_card_2 = cards.get(13)

        
#compare the players card with the dealer cards
def compare():
    global player_bet
    global player_money
    global players_card
    global game_card_1
    global game_card_2
    values()
    
    if players_card < game_card_1 and players_card > game_card_2:
        print "\n"
        print "Winner!"
        
        spread = (game_card_2 - game_card_1) - 1
        
        if spread == 1:
            player_bet = player_bet * 5
            player_money = player_money + player_bet
            print "You won $%d" % player_bet
            
        elif spread  == 2:
            player_bet = player_bet * 4
            player_money = player_money + player_bet
            print "You won $%d" % player_bet

            
        elif spread == 3:
            player_bet = player_bet * 2
            player_money = player_money + player_bet
            print "You won %d" % player_bet
        else:
            player_money = player_money + player_bet
            print "You won $%d" % player_bet


    elif players_card < game_card_2 and players_card > game_card_1:
        print "\n"
        print "Winner!"
        spread = (game_card_2 - game_card_1) - 1
        if spread == 1:
            player_bet = player_bet * 5
            player_money = player_money + player_bet
            print "You won $%d" % player_bet
            
        elif spread  == 2:
            player_bet = player_bet * 4
            player_money = player_money + player_bet
            print "You won $%d" % player_bet

            
        elif spread == 3:
            player_bet = player_bet * 2
            player_money = player_money + player_bet
            print "You won %d" % player_bet
        else:
            player_money = player_money + player_bet
            print "You won $%d" % player_bet
            
        
    elif players_card == game_card_1 and players_card == game_card_2:
      print "JACKPOT!"
      player_bet = player_bet * 11
      print "You won $%d" % player_bet
      player_money = player_money + player_bet
    else:
        
        player_money = player_money - player_bet
        print "\n"
        print "You lost $%d" % player_bet
        

#move to the final found
def final_round():
    change_back()
    print "\n"
    
    print "*===========================*"
    print "        Final Turn           "
    print "*===========================*"
    print "   First draw: %s of %s    " % (game_card_1, game_suit_1)
    print "  Second draw: %s of %s    " % (game_card_2, game_suit_2)
    print "*===========================*"
    print ""
    print "Your card: %s of %s" % (players_card, player_suit)


header()
main()



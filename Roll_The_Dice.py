
from __future__ import print_function 

import random, time, sys

'''
A simple game of craps

'''
player_bet = 0
player_money = 2000
number = 0 
D1 = 0
D2 = 0
point = 0
dice_total = 0
dice = 25


#main program

def header():
    print("*==========================================================*")
    print("To start a round, the player makes a come out roll.        *")
    print("If the come out roll is a 2, 3, or 12, then the round ends.*")
    print("If the come out roll is a 7 or 11, player wins the bet.    *")
    print("If the roll is 4, 5, 6, 8, 9, or 10 it becomes the point   *")
    print("If the point is rolled before rolling 7 or 11,player wins. *")
    print("*==========================================================*")
    
           
def main():
    
    global D1
    global D2
    global dice_total
    global player_money
    
    while player_money > 0 :
        D1 = dice_shuffle()
        D2 = dice_shuffle()
        betting()
        come_out()
       
    else:
        print("\n")
        print("Oh, Im sorry. You're all out of money")
        
        user_input = raw_input("Do you want to play again? (Y/N)")
        if user_input in ["Y", "y"]:
            player_money = 2000
            main()
        else:
            print("Good bye")
            os._exit(1)
  
def dice_shuffle():
    random_list = [1,2,3,4,5,6]
    random.shuffle(random_list)
    number = random.choice(random_list)
    return number

def roller():
    global dice
    roller = lambda:random.choice('123456')
    print("")
    for i in range(1,15):
        time.sleep(.2)
        print('|'.join([roller(),roller()]), end = "\r")
        
    print("*****", end = "\r")


# place the bet
def betting():
    global player_bet
    
    print("\n")
    print("*============*")
    print( "You have $%d " % player_money)
    print( "Minumum: $1  ")
    print( "Maximum: None")
    print( "*============*")
    print( "\n")

    try:
        player_bet = int(raw_input("How much do you want to bet? "))
        
        if player_bet > player_money:
            print( "")
            print( "You cant bet more than you have.")
            print( "Betting maximum amount available")
            player_bet = player_money
            
        if player_bet is not int(player_bet):
            print( "Please enter a numeric value.")
            betting()
        else:
            player_bet = int(player_bet)
    except ValueError:
        print( "Please enter a numeric Value")
        main()
    except IOError:
        print( "I/O Error")    


def come_out():
    global player_bet
    global player_money
    global D1
    global D2
    global dice_total
    global point
    game = True

    while game == True:
        print( "Lets begin!")
        print( "")
        raw_input("Press any button to roll your dice. ")
        roller()
        print("")
        
        dice_total = D1 + D2
        print( "*=================================================*")
        print( "Your dice rolls are %d and %d." %(D1, D2,))
        print( "*=================================================*")
        
    
        if dice_total in [7,11]:
            print("")
            print( "$$$$$$$$")
            print( "Winner!$")
            print( "$$$$$$$$")
            player_money = player_money + (player_bet * 2)
            
            D1 = 0
            D2 = 0
            main()
    
        elif dice_total in [2,3,12]:
            player_money = player_money - player_bet
            print( "")
            print( "!!!!!!")
            print( "Craps!")
            print( "!!!!!!")
            main()
    
        elif dice_total in [4,5,6,8,9,10]:
            point = dice_total
            if point > 0:
                dice_point()
    

def dice_point():
    global D1
    global D2
    global dice_total
    global point
    global player_bet
    global player_money

    print( "*==============*")
    print( "The point is %d *" % point)
    print( "*==============*")
    game = True

    while game == True:
        
        user_input = raw_input("Hit any button to roll again ")
        roller()
        D1 = dice_shuffle()
        D2 = dice_shuffle()
        dice_total = D1 + D2
        print( "*=================================================*")
        print( "Your dice rolls are %d and %d for a total of %d." %(D1, D2, dice_total))
        print( "*=================================================*")

        if dice_total == point:
            player_money = player_money + (player_bet * 2)
            print( "$$$$$$$$")
            print( "Winner!$")
            print( "$$$$$$$$")
            D1 = 0
            D2 = 0
            main()
            
        elif dice_total == 7 or dice_total == 11:
            player_money = player_money - player_bet
            print( "")
            print( "!!!!!!")
            print( "Craps!")
            print( "!!!!!!")
            main()
header()            
main()
    
    

    
    















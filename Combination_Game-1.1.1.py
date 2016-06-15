import random, os


chances = 0
combo = [0,0,0]
user_guess = [0,0,0]
answers_correct = 0 
answers_wrong = 0
user_input = 0



#main program function
def main():
    print "\n"
    
    #Start Game
    title = 'Welcome to Higher Learning'
    print '=' * (40+len(title)+2)
    print '=' * 20,title,'=' * 20
    print '=' * (40+len(title)+2)
    print ""

#Rules
    title = '  Rules  '
    print '=' * (40+len(title)+2)
    print '=' * 20,title,'=' * 20
    print "First guess 3 numbers" 
    print "You'll be told if each guess should be higher or lower."
    print "For each wrong answer, you'll have one chance to correct it."
    print "Guess the combination and win the prize"
    print "Guess wrong and meet your fate. \n"
    print '=' * (40+len(title)+2)
    
    guesses()
    answer_check()
    messages()
    menu()
    end()

#self explanitory 
def winner():
    prizes = ["Ten million dollars", "A dimond ring", "A magic lamp"]
    print "You've won %s" % random.choice(prizes)

def bad_things():
    omens = ["You were buried alive.", "You lost your house.", "You were cursed with over protective parents.", "You were caught kissing your sister."]
    print "%s" % random.choice(omens)
    
#resets all counters to zero
def reset():
    global answers_wrong
    global chances
    global counter
    global combo 
    global user_guess

    global answers_correct 
    global answers_wrong 
    global user_input
    counter = 0
    chances = 0
    combo = [0,0,0]
    user_guess = [0,0,0]
    answers_correct = 0 
    answers_wrong = 0
    user_input = 0

    
#random number generator            
def RNG(number):
    number = random.randrange(1,10)
    return number



# Checks users answers with random numbers
def answer_check():
    
    global answers_correct
    global answers_wrong
    
    if combo[0] == user_guess[0]:
        answers_correct = answers_correct + 1
    else:        
        answers_wrong = answers_wrong + 1
        

    if combo[1] == user_guess[1]:
        answers_correct = answers_correct + 1
        
    else:
        answers_wrong = answers_wrong + 1
        
    
    if combo[2] == user_guess[2]:
        answers_correct = answers_correct + 1
    else:
        answers_wrong = answers_wrong + 1

        
#prints if the guess should be higher or lower      
def messages():
    print "Your guesses were %s " % user_guess
    print "You got %d digits correct. \n" % answers_correct
    
    if combo[0] > user_guess[0]:
        print "%s should be higher." % user_guess[0]
    elif combo[0] == user_guess[0]:
        print "%s is correct." % user_guess[0] 
    else:
        print "%s should be lower." % user_guess[0]
            
    if combo[1] > user_guess[1]:
        print "%s should be higher." % user_guess[1]
        
    elif combo[1] == user_guess[1]:
        print "%s is correct." % user_guess[1] 
        
    else:
        print "%s should be lower" % user_guess[1]        

    if combo[2] > user_guess[2]:
        print "%s should be higher" % user_guess[2]
        
    elif combo[2] == user_guess[2]:
        print "%s is correct."  % user_guess[2]  
    else:
        print "%s should be lower." % user_guess[2]

#asks the user which guess they would like to change
def menu():
    global chances
    global answers_wrong
    print "\n"
    print "You have %s chances." % answers_wrong
    while chances is not answers_wrong:
        
        try:
            print "Which digit do you want to change?(Press 0 for none)"
            user_input = int(raw_input(">> "))
            if user_input == 0:
                end()
        
            if user_input == user_guess[0]:
                user_input = int(raw_input("What would you like to change it to? "))
                user_guess[0] = user_input
                chances = chances + 1
                print "\n"
                print "Your guesses are %s." % user_guess
        
            elif user_input == user_guess[1]:
                user_input = int(raw_input("What would you like to change it to? "))
                user_guess[1] = user_input
                chances = chances + 1
                print "\n"
                print "Your guesses are %s." % user_guess
            
            elif user_input == user_guess[2]:
                user_input = int(raw_input("What would you like to change it to? "))
                user_guess[2] = user_input
                chances = chances + 1
                print "\n"
                print "Your guesses are %s." % user_guess

            else:
                print "Please choose from these guesses %s." % user_guess
            
        except:
            print "Please choose from these guesses %s." % user_guess


# Lets you know if you won or loss
def end():
    print "The combination was %s " % combo
    if user_guess == combo:
        print "\n"
        print "Congratulations! You unlocked the safe!"
        winner()
        user_input = raw_input("Would you like to try again? (Y/N)")
        if user_input in ["Y", "y", "Yes", "yes"]:
            reset()
            main()
        
    else:
        print "\n"
        print "Im sorry. Your fate is doomed!"
        bad_things()
        user_input = raw_input("Would you like to try again? (Y/N)")
        if user_input in ["Y", "y", "Yes", "yes"]:
            reset()
            main()
        else:
            print "Goodbye"
            os._exit(1)            
        
       
#Asks the user to guess numbers between 1 and 10
def guesses():
    global user_input
    while True:
        try:
            user_input = int(raw_input("Guess the first digit between 1 and 10 >> " ))
            if user_input is int(user_input):
                user_guess[0] = user_input
                combo[0] = RNG(combo[0])
            else:
                print "Enter a number"    
    
                
            user_input = int(raw_input("Guess the second digit between 1 and 10 >> " ))
            if user_input is int(user_input):
                user_guess[1] = user_input
                combo[1] = RNG(combo[1])
                                            
            else:
                print "Enter a number"

                
            
            user_input = int(raw_input("Guess the third digit between 1 and 10 >>" ))
            if user_input is int(user_input):
                print "\n"
                user_guess[2] = user_input
                combo[2] = RNG(combo[2])
               
                #this checks if all the guesses are the same
                if user_guess[0] == user_guess[1] or user_guess[0] == user_guess[2]:
                    print "OOPS! Looks like some of your numbers are the same."
                    print "Please enter three different numbers."
                    print "\n"
                    guesses()
                elif user_guess[1] == user_guess[0] or user_guess[1] == user_guess[2]:
                    print "OOPS! Looks like some of your numbers are the same."
                    print "Please enter three different numbers."
                    print "\n"
                    guesses()
                elif user_guess[2] == user_guess[0] or user_guess[2] == user_guess[1]:
                    print "OOPS! Looks like some of your numbers are the same."
                    print "Please enter three different numbers."
                    print "\n"
                    guesses()
                
                
                    
                break            
            else:
                print "Enter a number"
                       
                           
        except ValueError:
            print "\n"
            print "Did you type something wrong? Lets start over!"
            



main()

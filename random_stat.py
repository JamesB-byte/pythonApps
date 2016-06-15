import random

'''
I like to play Diablo 3 and I was upset how the random numbers system for augmenting your armor was.
It seemed to apply the same stats over and over again. So I made this to try and emulate that system to see for myself
how random the numbers actully are. 
'''

guess= 0
def RNG(number):
    number = random.randrange(1,100)
    return number

print "Choice of random stats"
print "\n"
blank_stats = ["Life steal","Life on kill","Arcane Damge", "Stun","Critial Attack Damage", "Attack Speed"]
print blank_stats

while True:
    print "\n"
    user_input = raw_input("Hit enter >> ")
    print "\n"
    stats = ["Life steal:+%d" % RNG(guess),"Life on kill:+%d" % RNG(guess),"Arcane Damge:+%d" % RNG(guess),
         "Stun:+%d" % RNG(guess),"Critial Attack Damage:+%d" % RNG(guess), "Attack Speed:+%d" % RNG(guess)]
    random.shuffle(stats)
    choice = random.sample(stats,3)
    for i in choice:
        print i
        
        
        
         
        
    
    
    
   





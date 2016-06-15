import random


#Start Game
title = 'Welcome to Monster Blackjack'
print '=' * (40+len(title)+2)
print '=' * 20,title,'=' * 20
print '=' * (40+len(title)+2)
print ""


#Rules
title = '  Rules  '
print '=' * (40+len(title)+2)
print '=' * 18,title,'=' * 22
print "A very simple blackjack game"
print "in the game the cards have the following values ..."
print "aces are 11 or 1"
print  "J, Q, K are 10"
print " Score damage by beating the monster at blackjack"
print " First to fall to 0 loses."
print '=' * (40+len(title)+2)

#declare all variables

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hand_card = 0
total = 0
hero_total = 0
monster_total = 0
hero_health = 100
monster_health = 100
rounds = 1
chest = ['Sword of Omens', 'Excalibur', 'Power Sword']


def draw(hand_card):
 hand_card = random.choice(cards)
 return hand_card

def round():
    
   print "Round %d" % rounds
   global rounds
   rounds = rounds + 1
   return rounds

 
print "You encounter a monster. Let the battle begin \n" 


# Start the game until either heros health or monsters health reaches zero

while hero_health > 0 and monster_health > 0:


    
    #first, heroes draws a cards

    first_card = draw(hand_card) 
    second_card = draw(hand_card)
    total = first_card + second_card
    hero_total = total
    print "Your two cards are %d and %d." % (first_card, second_card)
    print "You have a total of %d." % (total)
    
    #hero decides if they want to hit or stay

    while total < 21:
        answer = raw_input("Do you want to (H)it or (S)tay?")
        if answer == "h":
            hand_card = draw(hand_card) 
            total = total + hand_card 
            hero_total = total
            if total > 21:
                print "Oooh! You busted!"
                total = 0
                break
            print "You drew a %d." % hand_card 
            print "Your total is %d." % hero_total 
        elif answer == "s":
            hero_total = total 
            print "Your total is %d." % total
            print "Now it's the monsters turn!"
            total = 0
            break
        else:
            print "Please select H or S." 
            
    # Monster starts its turn 

    first_card = draw(hand_card) 
    second_card = draw(hand_card)
    total = first_card + second_card
    monster_total = total
    print "The monsters first two cards are %d and %d." % (first_card, second_card) 
    print "Its total is %d." % total
    while total < 15:
        total = total + draw(hand_card)
        print "The monster draws another card!"
        if total > 21:
            print "The monster busted!"
        else:
            monster_total = total
            print "The monsters total is %d" % monster_total
            
    #damage is calculated   

    if hero_total > monster_total and hero_total <= 21:
        print "Hero wins!"
        sword_dmg = random.randrange(50+20)
        monster_health -= sword_dmg
        print "The hero does %d damage to the monster" % sword_dmg
        
    elif hero_total < monster_total and monster_total > 21:
        print "Hero Wins!"
        sword_dmg = random.randrange(50+20)
        monster_health -= sword_dmg
        print "The hero does %d damage to the monster" % sword_dmg
    elif monster_total > hero_total and monster_total <=21:
        print "Hero Loses"
        claw_dmg = random.randrange(50+20)
        hero_health -= claw_dmg
        print "The monster does %d damage to the hero." % claw_dmg
    elif monster_total < hero_total and hero_total > 21:
        print "Hero Loses"
        claw_dmg = random.randrange(50+20)
        hero_health -= claw_dmg
        print "The monster does %d damage to the hero." % claw_dmg
    else:
        print "Its a draw"
    print "Hero's health = %d" % hero_health
    print "Monster's health = %d " % monster_health
    
    # Results are outputed

if hero_health < 0:
   print "Hero health is below 0. The hero dies"
if monster_health < 0:
   print "Monster health is below 0. The monster is dead."
   print "You obtained  %s!!." % random.choice(chest)

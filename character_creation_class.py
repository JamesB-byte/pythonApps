import random

#================================#
# RPG character creation tool    #
#                                #
# Example of how to use classes  #
#                                #
#================================#

# global list of races and classes 

race = ['Elf', "Human", "Dwarf"]
classes = ["Warrior", "Rogue", "Mage"]

# global variable for character ability points 
ability_points = 25


#create your class 
class character:
    
    # list your classes variables
    user_name = ""
    user_race = ""
    user_class = ""
    user_strength = 0
    user_dexterity = 0
    user_consitution = 0
    user_intelligence = 0
    user_wisdom = 0
    user_charisma = 0
    
    # Select your characters name
    def select_name(self):
        user_input = raw_input("What is your characters name? ")
        self.user_name = user_input
        print ""
        print "Hello %s." % self.user_name
        
     # select your characters race    
    def select_race(self):
        print ""
        print "Please select your race."
        print ""
        print "1. Elf"
        print "2. Human"
        print "3. Dwarf"
        print ""
       
        user_input = raw_input("> ")
        
        if user_input == "1":
            self.user_race = {"Race":race[0]}
            
        elif user_input == "2":
            self.user_race = {"Race":race[1]}
            
        elif user_input == "3":
            self.user_race = {"Race":race[2]}
             
        else:
            print "Please select an option from the menu"
            

    # select your characters class         
    def select_class(self):
        print ""
        print "Please select your class."
        print "1. Warrior"
        print "2. Rogue"
        print "3. Mage"
        print ""

        
      
        user_input = raw_input("> ")
        
        if user_input == "1":
            self.user_class = {"Class": classes[0]}
            
        elif user_input == "2":
            self.user_class = {"Class":classes[1]}
            
        elif user_input == "3":
            self.user_class = {"Class":classes[2]}
            
        else:
            print "Please select an option from the menu"

            
    # Randomly divide the ability points between the available stats
    def select_stats(self):
        chances = 0
        while chances < 3:
            global ability_points

            print "The dice gods have assigned you these ability points."
            
            self.user_strength = random.randrange(1,7)
            ability_points = ability_points - self.user_strength
    

            self.user_dexterity = random.randrange(1,7)
            ability_points = ability_points - self.user_dexterity
    

            self.user_constitution = random.randrange(1,7)
            ability_points = ability_points - self.user_constitution
    

            self.user_intelligence = random.randrange(1,7)
            ability_points = ability_points - self.user_intelligence
    

            self.user_wisdom = random.randrange(1,7)
            ability_points = ability_points - self.user_wisdom
            
            self.user_charisma = ability_points
            ability_points = 25

            # print the stats that were divided 
            print ""
            print "STR: %d" % self.user_strength
            print "DEX: %d" % self.user_dexterity
            print "CON: %d" % self.user_constitution
            print "INT: %d" % self.user_intelligence
            print "WIS: %d" % self.user_wisdom
            print "CHR: %d" % self.user_charisma
            print ""
            print "Chances = %d" % (2 - chances)

            
            # Ask if user wants to keep the stats assigned
            user_input = raw_input("Do you wanna keep these stats? Y/N ")
            print ""
            
            if user_input in ["Y","y"]:
                break
            elif user_input in ["N", "n"]:
                chances = chances + 1
            
        
    # Print the players attributes     
    def menu(self):
        print ""
        print "Name: %s" % self.user_name
        print "Race: %s" % self.user_race['Race']
        print "Class %s" % self.user_class['Class']
        print ""


        print "STR: %d" % self.user_strength
        print "DEX: %d" % self.user_dexterity
        print "CON: %d" % self.user_constitution
        print "INT: %d" % self.user_intelligence
        print "WIS: %d" % self.user_wisdom
        print "CHR: %d" % self.user_charisma
        
    

# Assign the "Character" class to variable "player_one" and "player_two"       
player_one = character()
player_two = character()

# Create Player One
print "Welcome to the RPG character creation tool"
print "------------------------------------------"
print ""
print "Player 1"
print "---------"

#Ask for name, race , and class and assign the attribues to Player_One
player_one.select_name()
player_one.select_race()
player_one.select_class()
player_one.select_stats()
player_one.menu()

print "*****************"

print "*****************"

# Create Player Two
print "Player 2"
print "---------"

#Ask for name, race , and class and assign the attribues to Player_One
player_two.select_name()
player_two.select_race()
player_two.select_class()
player_two.select_stats()
player_two.menu()
print ""

print "*****************"

print "*****************"
print ""

print "Player 1 stats"
print "---------------"
player_one.menu()
print ""
print "Player 2 stats"
print "---------------"
player_two.menu()

print ""
user_exit = raw_input(">>")

import random


#random variables
counter = 3
value = 0

#this class creates a "Weapon" with the certain attributes
class Weapon(object):
    
    global name

    #list of names for the guns
    name = ["T.K's Wave","Thunderball Fists","Hellfire","Deliverance","Flakker","Striker","Conference Call","Badaboom","Pyrophobia",
            "Breach Blaster", "Vengeful Infinity", "Potent Thunderball Fists", "Gearbox Rifle", "Sledges Shotgun"]
        
    def __init__(self,magazine_size, reload_speed,accuracy, damage, fire_rate, name ):

        self.magazine_size = magazine_size
        self.reload_speed = reload_speed
        self.accuracy = accuracy
        self.name = name
        self.damage = damage
        self.fire_rate = fire_rate    

weapon_object = {}

#as long as counter is less than zero, run everything below
while counter > 0:

    #shuffle the list of names
    random.shuffle(name)

    #place the attributes into the object. The list of random numbers will coincide with the list of attributes exactly from left to right
    weapon_object[value] = Weapon(random.randrange(5,100),random.uniform(1,5),random.uniform(45,100),random.randrange(75,100),random.uniform(0.5,3), random.choice(name))

    #print the objects
    print "Name: %s:" % weapon_object[value].name
    print "------------"
    print "Damage: %d" % weapon_object[value].damage
    print "Accuracy: %.1f" %weapon_object[value].accuracy
    print "Fire Rate: %.1f" % weapon_object[value].fire_rate
    print "Reload Speed: %.1f" % weapon_object[value].reload_speed
    print "Magazine Size: %d" % weapon_object[value].magazine_size
    print ""
    
    counter = counter - 1
    value = value + 1
    
    user_input = raw_input("Lets create another gun!")
    print ""
    

#print the names of guns we created
print "The guns we created were"

print ""
print "%s" % weapon_object[0].name
print "%s" % weapon_object[1].name
print "%s" % weapon_object[2].name   


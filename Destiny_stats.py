import json, requests, sys


'''

IMPORTANT!!!
Due to updates to Bungies API. This program may no longer be functional.


This program will search for your character in Destiny and display your stats.
This demonstrates how to use Bungie's API, how to pull data over a network, and how to use JSON

'''


search = ""
stats = ""
console_type = 0
displayName = ""
membershipId = 0
name = ""
totalKills = 0
char_level = []
char_choice = 0
char_1 = 0
char_2 = 0
char_3 = 0
playerLevel = 0
gamePlay = 0
lastPlayed = 0
option = 0
characters = []
race = ""
gender = ""
charClass = ""
race_Hash = 0
levels = []
classes = []



HEADERS = {"X-API-Key":'INPUT API KEY HERE'}



def main_program():
        	
        main_data()
        main_chars()
        main_activity()
        main_summary()
        

# Ask user info then print character stats to screen
def main_menu():
        global console_type, name
        
        print "Which console are you on? Xbox or PSN?"
        print ""
        try:
                console_type = int(raw_input("1. Xbox  \n2. PSN  \n3. Exit \n\n>> " ))
                print ""
                if console_type == 3:
                        sys.exit()
                else:
                        name = raw_input("What is your gamertag? ")
                        
                        while True:
                                main_program()
                                print ""
                                print "****************************"
                                print "Account: %s" % displayName
                                print "Character: %s" % char_choice
                                print "Level: %s" % playerLevel
                                print "Race: %s" % race
                                print "Class: %s" % charClass
                                print "Gender: %s" % gender
                                print "Hours Played: %.3f hours" % gamePlay
                                print "Last played: %s" % lastPlayed
                                print "Total kills: %d" % totalKills
                                print "****************************"
                                print ""
        
        
        except ValueError:
                print""
                print "Error! Enter a numeric value!"
                print ""
                main_menu()

# grab all of the users vailable characters 
def main_data():
        global displayName,membershipId,console_type
        data = "http://www.bungie.net/platform/Destiny/SearchDestinyPlayer/%d/%s" % (console_type, name)
        char_data = requests.get(data, headers = HEADERS)
        json_data = char_data.json()
        if len(json_data['Response']) == 0:
               print ""
               print "Gamertag Not Found!"
               print ""
               main_menu()
        else:
               for i in json_data['Response']:
                       displayName = i['displayName']
                       membershipId = i['membershipId']
        

#ask the user which character's stat they want to view
def main_chars():
        global option, characters, char_choice
        characters = []
        chars = "http://www.bungie.net/platform/Destiny/Stats/Account/%d/%s" % (console_type, membershipId)
        charToons = requests.get(chars, headers = HEADERS)
        json_stats = charToons.json()

        for item in json_stats['Response']['characters']:
                characters.append(item['characterId'])
             
            
        summary = "http://www.bungie.net/platform/Destiny/%d/Account/%s/Character/%s?definitions=true" % (console_type, membershipId,characters[option])
        char_summary = requests.get(summary, headers = HEADERS)
        json_summary = char_summary.json()
        
        for item in json_summary['Response']['data']:
                level.append(item['characterLevel'])
                classes.append(item[json_summary['Response']['data']['characterBase']['genderHash']])
                
      
        
        print "\n"
        print "Choose your character."
        print ""
        print "1. %s" % characters[0]
        print "2. %s" % characters[1]
        print "3. %s" % characters[2]
        print "4. Select a new gamertag"
        print "5. Exit"
        print ""
        
        
        print ""

        try:
                userChoice = int(raw_input("Which character do you want to view? "))
                if userChoice == 1:
                        option = 0
                        char_choice = characters[option]
                elif userChoice == 2:
                        option = 1
                        char_choice = characters[option]
                elif userChoice == 3:
                        option = 2
                        char_choice = characters[option]
                
                elif userChoice == 4:
                        main_menu()
                elif userChoice == 5:
                        print("Good bye")
                        sys.exit()
                else:
                        print ""
                        print "Invalid Entry!"
                        print "Please choose from the menu."
                        print ""
                        main_chars()
        except ValueError:
                print ""
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print "Please enter a numeric value."
                print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                print ""
                main_chars()
        except IOError:
                print "I/O Error"   
	        


def main_activity():
        global totalKills, characters, char_choice
        activity ="http://www.bungie.net/platform/Destiny/Stats/%d/%s/%s" % (console_type, membershipId,char_choice)
        char_activity = requests.get(activity, headers = HEADERS)
        json_activity = char_activity.json()
        
        if len(json_activity['Response']['raid']) == 0:
                killsRaid = 0
        else:
                killsRaid = json_activity['Response']['raid']['allTime']['kills']['basic']['value']
        killsStory = json_activity['Response']['story']['allTime']['kills']['basic']['value']
        
        if len(json_activity['Response']['patrol']) == 0:
                killsPatrol = 0
        else:
                killsPatrol = json_activity['Response']['patrol']['allTime']['kills']['basic']['value']

        if len(json_activity['Response']['allStrikes']) == 0:
                killsStrike = 0
        else:
                killsStrike = json_activity['Response']['allStrikes']['allTime']['kills']['basic']['value']
        

        
        totalKills = killsStory + killsRaid + killsPatrol + killsStrike
        

def main_summary():
        global gamePlay,playerLevel,lastPlayed,char_choice,race,gender,charClass
        
        summary = "http://www.bungie.net/platform/Destiny/%d/Account/%s/Character/%s?definitions=true" % (console_type, membershipId,char_choice)
        char_summary = requests.get(summary, headers = HEADERS)
        json_summary = char_summary.json()
        if json_summary['ErrorStatus'] == 'DestinyCharacterNotFound':
                print ""
                print "Destiny character not found or deleted."
                print ""
                main_program()
        else:
                gamePlay = json_summary['Response']['data']['characterBase']['minutesPlayedTotal']
                playerLevel = json_summary['Response']['data']['characterLevel']
                lastPlayed = json_summary['Response']['data']['characterBase']['dateLastPlayed']
                raceHash = json_summary['Response']['data']['characterBase']['raceHash']
                genderHash = json_summary['Response']['data']['characterBase']['genderHash']
                classHash = json_summary['Response']['data']['characterBase']['classHash']
                gamePlay = float(gamePlay)/60
                
                if raceHash == 898834093:
                        race = "Exo"
                elif raceHash == 3887404748:
                        race = "Human"
                elif raceHash == 2803282938:
                        race = "Awoken"
                

                if genderHash == 3111576190:
                        gender = "Male"
                elif genderHash == 2204441813:
                        gender = "Female"
                
                if classHash == 671679327:
                        charClass = "Hunter"
                elif classHash == 3655393761:
                        charClass = "Titan"
                elif classHash == 2271682572:
                        charClass = "Warlock"
main_menu()



        

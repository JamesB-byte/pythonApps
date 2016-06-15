import os, random

usedWords = []
words = []
points = 0
choice = []
password = []
likeness = 0
option = 0
tPoints = 0
score = 0
chances = 4

def reset():
        global usedWords, words, points, choice,password,chances, option, likeness
        usedWords = []
        words = []
        choice = []
        password = []
        likeness = 0
        option = 0
        chances = 4

#calculates points scored
def mainScore():
        global likeness, points, score, tPoints
            
        
        while likeness > 0:
                if likeness == 4 and chances == 3:
                        
                        points += 100
                        tPoints = points + tPoints
                
                        score = tPoints + score
                        
                       
                        
                        break
                                
                else:
                        points = points + likeness * 10
                        
                        tPoints = points + tPoints
                        
                        score = tPoints + score
                        
                        
                        break
                                

                
                        
       
        
        


def result():

        global chances, option, score, likeness,points,tPoints, usedWords
        
        while chances > 0:
                
                user_input = raw_input(">>")
                user_input = user_input.lower()
                
                
                if user_input in usedWords:
                        print "Already used"
                        
                        
                        
                else:
                        usedWords.append(user_input)
                        chances -= 1
                        
                if user_input == password:
                        likeness = 4
                        mainScore()
                            
                else:
                        for items in user_input:
                                if items in password[option]:
                                        likeness +=1
                                option += 1
                                
                  
                        mainScore()
                        
                        print "Likeness = %d" % likeness
                        print "Chances = %d" % chances

                
                if likeness == 4:
                                                
                        print "Welcome to Pip-boy"
                        
                        chances = 0
                        
                else:                       
                        likeness = 0
                        
                        if option == 4:
                                option = 0
                       
        print ""
        print "%d points earned" % tPoints
        print ""
        print "Score: %d" % score
        reset()


#pulls words from a word file
      
def wordList():
        global option, password
        #open word file and place words into a list
        sysFile = open('words.txt','r')

        for items in sysFile:
                words.append(items)

        #remove white spaces from words
        while option < 15:
                word1 = random.choice(words)
                word1 = word1.rstrip()
                choice.append(word1)                        
                option+=1

                
        # select password        
        password = random.choice(choice)

        mainScreen()
def header():
        print "Welcome to ROBOCO Industries (TM) Termlink"
        print "Password Required"
        print "Attemps Remaining %d" % chances
        
        
def mainScreen():
        
        global option, chances
        
        print ""

        print "0x1540 :++&&$*^)*? 0x16600 {}%s$*!{" % choice[0]
        print "0x154C :><)$<{*)*? 0x16615 /%s{:*#$" % choice[1]
        print "0x1558 :>$@%s *^)0x1662C ^{:^@<<*}}" % choice[2]
        print "0x1569  %s[()>$@ 0x1663C &{:*#$$@{&" % choice[3]
        print "0x1572 :><)*$*^)*? 0x16640 %s*{|}**" % choice[4]
        print "0x158C :>:}{{ %s 0x16653 >:}{@*^!^+" % choice[5]
        print "0x159E {[)%s )*? 0x16660 {:[':&^#{}" % choice[6]
        print "0x15A9 :%s $^)*? 0x1667C !&$##(+*<#" % choice[7]
        print "0x15A2  %s#**^*? 0x16683 {:*@{#$&#&" % choice[8]
        print "0x15B9 :><)*$*^)*? 0x16698 &*%s {:*" % choice[9]
        print "0x15CC :><)*$*^)*? 0x16694 <$%s {:*" % choice[10]
        print "0x15D3 @{{%s^)*? 0x166A3  {:*#@&<$&" % choice[11]
        print "0x15D7  %s @^>{} 0x166B0  <>_&&!*#{" % choice[12]
        print "0x15E8 (){}*$*^)*? 0x166C3 $ %s {:*" % choice[13]
        print "0x15F1 &(:{*$*^)*? 0x166D1 : %s {:*" % choice[14]
        print "0x15F0 @#^<*$*^)*? 0x166E4 +<>{{+&^"
        print password
        
        option = 0
        
        result()

header()
while True:        
        wordList()
        

                

          

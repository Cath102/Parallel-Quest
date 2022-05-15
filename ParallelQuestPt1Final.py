gameMap = {"Land of Lost Legends": "incomplete", "Mister E's Riddle Realm": "incomplete", "Fame of Us Island": "incomplete", "Sum Divided Forest": "incomplete"}
gameIsland = ["Land of Lost Legends", "Mister E's Riddle Realm", "Fame of Us Island", "Sum Divided Forest"]
count = 0
lives = 3


I1complete = 0
I2complete = 0
I3complete = 0
I4complete = 0

import sys

def ProgressPrint(gameMap):
    print("        ?arallel Quest Map")
    print("------------------------------------")
    for land in gameMap:
        print("%-25s %s" % (land, gameMap[land]))
        
def checkClick(click):
    if click != '':
        click = input("(press Enter to continue) ")
        checkClick(click)
    if click == '':
        for i in range(1):
            print()
            break
        
def Click():
    print()
    input("(press Enter to continue)")
    print("\n")

def DadLetterW():
    outfile = open("DadLetter.txt", "w")
    outfile.write("Hello my child,")
    outfile.write("\n")
    outfile.write("\nYou have been amazing and managed to finish my quest and I am so proud of you.")
    outfile.write("\nIf you are wondering where I am, I am in the other universe trying to find the")
    outfile.write("\nnext biggest thing. And I want you to come join me. Mr. Pi will open the door.")
    outfile.write("\nI hope to see you soon, my child.\n")
    outfile.write("\n")
    outfile.write("Love,\n")
    outfile.write("Your Father")
    outfile.close()

def DadLetterR():
    infile = open("DadLetter.txt", "r")
    line1 = infile.readline()
    line1 = line1.lstrip()
    line2 = infile.readline()
    line2 = line2.rstrip()
    line3 = infile.readline()
    line3 = line3.rstrip("\n")
    line4 = infile.readline()
    line4 = line4.strip()
    line5 = infile.readline()
    line5 = line5.strip()
    line6 = infile.readline()
    line6 = line6.strip()
    line7 = infile.readline()
    line7 = line7.strip()
    line8 = infile.readline()
    line8 = line8.strip()
    line9 = infile.readline()
    line9 = line9.strip()
    
    print(line1, line2, line3, line4, line5, line6, line7) 
    print(line8) 
    print(line9)
    infile.close()

print("Before starting the game, please play in full screen (expanded console)")
Click()
print("")
print("      -----------------------------------------------------------------------------------------------------------------------------------------")
print("      /  \      _____                                                               _______                                               /   | ")
print("     /   |     /     \                             |    |            |             /       \                                            /    /      ")
print("    /    |    |      |                             |    |            |            |         |                                |         /    /         ")
print("   /    /           /   ___        ___   ____      |    |            |           |          |                      ____      |        /    /            ")
print("  /    /         /    /    \|    | /    /    \|    |    |    _____   |          |           |     |    |   _____  /       ___|___    /    /         ")
print(" /    /         |    |     ||   |/     |     ||    |    |   /____\   |          |       __  |    |     |  /____\  \___       |      /    /        ")
print("/    /          .    \____/|_  |       \____/|_    |    |  \_____    |          \______/__\/___  \____/| \_____   ____\      |     /    /     ")
print("/  /                                                                                                                              \   /     ")
print("-------------------------------------------------------------------------------------------------------------------------------------- ")
print("\n \n \n \nGame Loading: 30%")
Click()
print("Game Loaded 100%")
#intro")
Click()
print("It is your 18th birthday and a box unexpectedly appeared in front of you. Inside are three candles and a note. In that note reads...")
Click()
print("Happy birthday son. It is time for you to explore the path that I once did 3 years. I am probably still exploring right now but hopefully, your journey will reunite us very soon.")
print("Light up the candles, and close your eyes. When you open them again, your journey will begin.")
print("Love,")
print("Dad")
Click()
print("You light up the candles... and close your eyes... ")
print("Your head gets swirled and hear sonic screams... Then you hear a voice...")
Click()
print("Hello? Hello? Are you alive human?")
Click()
print("You open your eyes and stand up...")
Click()
print("Ahh welcome. My name is Mr. Elfo. You must be the child of Dr. Robinson. We've been expecting you. What was your name?")
nameC = 0
while nameC == 0:
    userName = input("Name: ")
    if len(userName) >= 1:
        userName = userName
        break
    else:
        print("That is not a valid name, please re-enter a name.")
print("")
print("Ahh, of course, of course. How could I forget. Your father told me your name was %s. It is an honor to meet you. I suppose you are following in the same footsteps as your father. I expect a lot from you since he is one of our famed conquerors." %userName)
print("")
print("Before I let you go, please do pay very close attention to these rules.")
Click()

print("Rule #1: \n    You have those 3 candles. These represents your access to this Parallel World. \n    Failing to answer a question correctly, will result to it breaking.")
print("Rule #2: \n    You must complete the 4 islands in order according to the map.")
print("Rule #3: \n    You should answer the questions with your own mind and knowledge... Without any help.")
print("Rule #4: \n    If you break all of your candles, You lose access to this Parallel World... Forever.")

Click()
print("\nWithout further ado, here is your map.\n")
ProgressPrint(gameMap)

Click()
print("\nYour father began his journey at the Land of Lost Legends. Therefore, you shall too. There, you will meet the legendary Weorge Gashington. I shall guide you to your next island upon completion. Good Luck!\n")
Click()
print("\n")
print("Teleported to %s..." % gameIsland[0])
print("\n")
Click()


#Land of Lost Legends
print()
print("\nWelcome %s to the Land of Lost Legends, my name is Weorge Gashington. Yes, very similar but just as handsome as your first president!\n\nI hope you know the history of your predecessors because you will be tested on them!" %userName)
#print("You should be familiar with my question formatting since that is how we test you all nowadays.")
print("\nDon't worry child. I will guide you through this wonderful land.\nUse the best of your memory to break these American history challenges.")
print("\nOkay now, here is your first question.")
Click()

class Question:
    def __init__(self, inputtext, inputanswer):
        self.text = inputtext
        self.answer = inputanswer
    def editText(self, newtext):
        self.text = newtext
    def editAnswer(self, newanswer):
        self.answer = newanswer
    def checkAnswer(self, response):
        if self.answer == response:
            print("CORRECT! Here is the next question.")
        else:
            print("INCORRECT.")
    def display(self):
        print(self.text)

class MC(Question):
    def __init__(self, text, answer):
        super().__init__(text, answer)
        self.choices = []
    def addChoice(self, choice):
        self.choices.append(choice)
    def display(self):
        print(self.text)
        for i in range(len(self.choices)):
            print(self.choices[i])

# question 1
q1 = MC("Question 1: When was the Declaration of Independence signed?", "D")
q1.addChoice("A. July 6, 1776")
q1.addChoice("B. June 4, 1776")
q1.addChoice("C. July 4, 1776")
q1.addChoice("D. August 2, 1776")

print("Let's start with the beginning of American independence.")
print("\nThis is one of the most important but least celebrated days in American history.")
for i in range(4):
    print("\n")
    q1.display()
    userAns = input("Your answer: ")
    q1.checkAnswer(userAns.upper())
    if userAns.upper() == q1.answer:
       I1complete += 1
       break
    else:
       lives -= 1
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()
#q2
q2 = MC("Question 2: Who wrote the Common Sense?", "D")
q2.addChoice("A.Thomas Jefferson")
q2.addChoice("B. Patrick Henry")
q2.addChoice("C. John Dickenson")
q2.addChoice("D. Thomas Paine")
q2.addChoice("E. Ben Franklin")

print("\n")
print("Wow! You survive the first round. Feeling good right now? Yeahhh!")
print("Come with me! Let's step to the next one!")
for i in range(4):
    print("\n")
    q2.display()
    userAns = input("Your answer: ")
    q2.checkAnswer(userAns.upper())
    if userAns.upper() == q2.answer:
       I1complete += 1
       break
    else:
       lives -= 1   
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()      
   
#q3
q3 = MC("Question 3: What was the name of the Pilgrims’ ship?", "B")
q3.addChoice("A. The Black Pearl")
q3.addChoice("B. The Mayflower")
q3.addChoice("C. The Ocean’s Great")
q3.addChoice("D. The Motherboard")
q3.addChoice("E. The Promised Mission")

print("\n")
print("Third question here!\nI'm sure you are familiar with this one.")
for i in range(4):
    print("\n")
    q3.display()
    userAns = input("Your answer: ")
    q3.checkAnswer(userAns.upper())
    if userAns.upper() == q3.answer:
       I1complete += 1
       break
    else:
       lives -= 1
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()
#q4
q4 = MC("Question 4: What City was the first capital of the United States?", "B")
q4.addChoice("A. Washington D.C.")
q4.addChoice("B. New York City")
q4.addChoice("C. Philadelphia")
q4.addChoice("D. Charleston")
q4.addChoice("E. Boston")

print("\n")
print("You are moving closer to the end of this land. Just keep up this pace!")
for i in range(4):
    print("\n")
    q4.display()
    userAns = input("Your answer: ")
    q4.checkAnswer(userAns.upper())
    if userAns.upper() == q4.answer:
       I1complete += 1
       break
    else:
       lives -= 1   
       print("I will break one of your candles. You have now %d candle(s)" %lives)   
    if lives == 0:
       print("\nGAME OVER")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()
#q5
q5 = MC("Question 5: Which US president did NOT hold 2 terms?", "E")
q5.addChoice("A. George W. Bush")
q5.addChoice("B. Jimmy Carter")
q5.addChoice("C. William Howard Taft")
q5.addChoice("D. A & C")
q5.addChoice("E. B & C")
q5.addChoice("F. None of the above")

print("\n")
print("Oh my my, last round already?")
print("You'd better watch out, because this one is going to be tricky *_*")
for i in range(4):
    print("\n")
    q5.display()
    userAns = input("Your answer: ")
    if userAns.upper() == q5.answer:
       print("You got it CORRECT!")
       I1complete += 1
       break
    else:
       lives -= 1   
       print("INCORRECT. I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()
       
#transition to land 2
if I1complete == 5:
    gameMap["Land of Lost Legends"] = "complete"

print("\n")
print("Mr. Elfo reappears...")
Click()
click = input("Hello %s. Congratulations! You have conquered the Land of Lost Legends.\nLook at your map, it has updated.\n\n(press Enter to continue)" %userName)
print("\n") 
checkClick(click)
ProgressPrint(gameMap)
Click()
print()
print("The next stop on your journey is at %s." % gameIsland[1])
if lives < 3:
    lives = 3
    print("\nYour candles have been restocked back to %d." % lives)
else:
    print("You still have %d candles remaining." %lives)
print()
Click()
##############################################################################
#NEW ADDITION: Tic-Tac-Tea
print("Ooh, it seems like it will take a couple more minutes for the teleportation device to be ready for you.")
print()
print("Let's play Tic-Tac-Tea, a classic game of tic-tac-toe during our teatime. As a bonus, I'll even add 2 more candles if you win.")
Click()

firstBoard = {'1': '1' , '2': '2' , '3': '3' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '7': '7' , '8': '8' , '9': '9' }

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


print("Here's the table setup for this classic tic-tac-toe.")
print("Enter only an integer value between 1-9 corresponding to the spots on the board.")
printBoard(firstBoard)
print()
Click()
print("Now let's begin!")
Click()
turn = 'X'
count = 0
win = 0        

while win == 0 and count != 9:
    import random
    if turn == 'O':
        print("It's Mr.Elfo's turn.")
        p = random.randint(1,9)
        print("Mr.Elfo: I'm going with %s." %p)
        move = str(p)
    else:
        printBoard(theBoard)
        print("It's your turn ," + userName + ". Move to which place?")
        move = input()
    print()
    try:
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Try again.")
            continue
    except KeyError as exception:
        print("Error:", str(exception), "\n")
        continue

    if count >= 5:
        if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the top
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 
        elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the bottom
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 
        elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ': # diagonal
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 

        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            printBoard(theBoard)
            if turn == 'O':
                print("\nGame Over. Mr.Elfo won.\n")
                print("Unfortunately you won't get any additional candles.")
                win = 0
            else:
                print()
                print(" **** " +userName + " won ****")
                win = 1
            break 

    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:             
        print("It's a Tie!!")
        print("Unfortunately you won't get any additional candles.")
        win = 0
    # Change the player after every move.
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'    
            
if win == 1:
    lives += 2 
    print("%s has received 2 more candles from Mr.Elfo." %userName)
print("This means you currently have",lives,"candles." )
    
Click()
print("Well that was a good game to pass some time. Seems like the teleportation is ready to go! ")
Click()
print("Oh here is a little you might want to know about Mister E.")
Click()       
##############################################################################


#land 2 intro
print("\nMister E. was an old friend of your father's, maybe he has some clues about the legacy your father left behind.")
print("Unfortunately, he doesn't like accepting many visitors on his mountain, so he has set a couple of riddles along your path to the summit.")
print("\nWish you the best of luck.")
print()
Click()
print("\n")
print("Teleported to Mister E's Riddle Mountain...")
print("(Tip: In this stage, you may use the phrase: 'hint' to get help.)")
print("\n")
Click()

#Mister E's Riddle Realm
print("\nYou've arrived at the base of the mountain, but now you are lost.")
Click()
print()
print("As you are looking around, Mister E's messenger pigeon delivers a slip of paper.")
print("It reads...\n")
Click()
print("Hello %s,\nI knew you would someday pay me a visit.\nYour father and I have travelled together for many years solving puzzles and uncovering mysteries.\nI'm sure you have many questions for me, but first...\n" %userName)
print("Let's see if you have what it takes to be an adventurer just like your father.\n")
print("Best regards,\nMister E.\n")
print("P.S. Along with this letter, I have enclosed one more item that will help you find me.")
Click()

#r1
for i in range(lives + 1):
    q1 = input("Mister E's first guide has lakes with no water, mountains with no stone, and cities with no buildings. What is it?\n\nAnswer: ")
    if q1.lower() == "map":
        print("CORRECT. Now you are set to go.")
        I2complete += 1
        break
    elif q1.lower() == "hint":
        print("Hint: _ _ _")
    else:
        lives -= 1
        print("INCORRECT. I will break one of your candles. You have now %d candle(s)." % lives)
    if lives == 0:
        print("\nGAME OVER")
        print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
        sys.exit()

Click()
print("\nAs you start your journey, you realized that this would be a really long and lonely trip, so you called an Uber driver nearby.")
print()

#r2
for i in range(lives + 1):
    q2 = input("Once he arrives, you guys continue your trip going the opposite way up a one way road, but then you pass two policemen along the way, none of which stopped you. Why not?\n\nAnswer: ")
    if q2.lower() == "walking" or q2.lower() == "walk":
        print("CORRECT. The Uber driver decided to accompany you until you reach Mister E's place.")
        I2complete += 1
        break
    elif q2.lower() == "hint":
        print("Hint: You guys are ' _ _ _ _ ing'.")
    else:
        lives -= 1
        print("INCORRECT. I will break one of your candles. You have now %d candle(s).\n" % lives)
    if lives == 0:
        print("\nGAME OVER")
        print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
        sys.exit()
        
Click()
print("Uber driver buddy: Dude, I'm so sorry. My car broke down a while ago.(╥︣﹏᷅╥)") 
print("%s (you): (－‸ლ)" %userName)   
print("Uber driver buddy: Well, let's just travel together. (T-T)ヾ(^^ )")          
Click()
print("Not too long after, a driver pulls up and ask if you and the Uber driver wanted to hitch a ride.")
print()

#r3
for i in range(lives + 1):
    q3 = input("In the standard 5-seated car, there are two fathers and two sons in the car, yet there are enough seats for both you and the Uber driver. How? \n \nAnswer: ")
    if q3.lower() == "grandfather, father, and son" or q3.lower() ==  "grandfather, father, son" or q3.lower() == "grandfather,father,son" or q3.lower() == "grandfather, father, and son" or q3.lower() == "grandfather,father,andson" or q3.lower() == "grandfather,father, andson":
        print("CORRECT. Gladly, you both hop on the car. (o^ω^)(^ω^o)")
        I2complete += 1
        break
    elif q3.lower() == "hint":
        print("Hint: They are '_ _ _ _ _ _ _ _ _ _ _,' ' _ _ _ _ _ _,' and ' _ _ _'.")
    else:
        lives -= 1
        print("INCORRECT. I will break one of your candles. You have now %d candle(s).\n" % lives)
    if lives == 0:
        print("\nGAME OVER")
        print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
        sys.exit()

Click()
print("Just as the sun was about to set, the car stops...")
Click()
print("╰(*’▽’)ノ━☆ﾟ.*･｡ﾟ You've finally reached the top!  ")
print()


#r4
for i in range(lives + 1):
    q4 = input("At the summit, you see something that possesses a halo of water, walls of stone, and a tongue of wood. What do you see?\n\nAnswer: ")
    if q4.lower() == "a castle" or q4.lower() == "castle":
        print("CORRECT. Welcome to Mister E's humble abode.")
        I2complete += 1
        break
    elif q4.lower() == "hint":
        print("Hint: a '_ _ _ _ _ _' ")
    else:
        lives -= 1
        print("INCORRECT. I will break one of your candles. You have now %d candle(s).\n" % lives)
    if lives == 0:
        print("\nGAME OVER")
        print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
        sys.exit()

Click()
print("Step by step, you cross the drawbridge, searching for a glimpse of Mister E.") 
Click()
print("Just as you approached the center of the open courtyard,\nMister E's butler appears and regretfully informs you of Mister E's passing.")   
print("His last words were to pass one last riddle to the child of his good friend, Dr. Robinson.")

#r5
for i in range(lives + 1):
    q5 = input("What are the next three letters in this combination? OTTFFSS_ _ _\n\nAnswer: ")
    if q5.lower() == "ent" or q5.lower() == "e n t":
        print("CORRECT. Now you have unlocked the passcode to a secret chamber that will directly transport you to the heart of ENTertainment.")
        I2complete += 1
        break
    elif q5.lower() == "hint":
        print("Hint: think of counting numbers and its relationship to the combo.")
    else:
        lives -= 1
        print("INCORRECT. I will break one of your candles. You have now %d candle(s).\n" % lives)
    if lives == 0:
        print("\nGAME OVER")
        print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
        sys.exit()

#transition to land 3
if I2complete == 5:
    gameMap["Mister E's Riddle Realm"] = "complete"

print("\n\n")
click = input("Hello %s. Congratulations! You have conquered Mister E's Riddle Realm. Look at your map, it has updated.\n\n\n(press Enter to continue)" %userName)
print()    
checkClick(click)
ProgressPrint(gameMap)

Click()
print()
print("The next stop on your journey is at %s." % gameIsland[2])
if lives < 3:
    lives = 3
    print("\nYour candles have been restocked back to %d." % lives)
else:
    print("You still have %d candles remaining." %lives)
print()
Click()


#land 3 intro
print()
print("Welcome to Fame of Us Island! You have qualified to visit this game show like island.\nNo this isn't Survivor, you will have to answer the following pop culture related questions.")
print("\nI will be your host: Steve Harvey ( ͡ᵔ ͜ʖ ͡ᵔ )")
print("Wish you the best of luck. -Game Show Music Begins Playing-")
print()
Click()
print()
print("Teleported to %s..." % gameIsland[2])
print()
Click()

#Fame of Us Island
#q1
q1 = MC("Question 1: Who voiced Shrek the ogre in the internationally-acclaimed award-winning motion picture shrek?", "A")
q1.addChoice("A. Mike Myers")
q1.addChoice("B. Eddie Murphy")
q1.addChoice("C. Toby Mcguire")
q1.addChoice("D. Peter Griffin")

while lives > 0:
    print("\n")
    q1.display()
    userAns = input("Your answer: ")
    q1.checkAnswer(userAns.upper())
    if userAns.upper() == q1.answer:
       I3complete += 1
       break
    else:
       lives -= 1
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER. Steve Harvey's facial expression: ಠ_ಠ")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()

#q2
q2 = MC("Question 2: Complete the following phrase: Scooby Dooby Doo __________", "A")
q2.addChoice("A. Where are you")
q2.addChoice("B. Who are you")
q2.addChoice("C. I love you")
q2.addChoice("D. I see you")

while lives > 0:
    print("\n")
    q2.display()
    userAns = input("Your answer: ")
    q2.checkAnswer(userAns.upper())
    if userAns.upper() == q2.answer:
       I3complete += 1
       break
    else:
       lives -= 1
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER. Steve Harvey's facial expression: ಠ_ಠ")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()     
   
#q3
q3 = MC("Question 3: What movie director attended and dropped out of California State University Long Beach?", "B")
q3.addChoice("A. Micheal Bay")
q3.addChoice("B. Steven Spieldberg")
q3.addChoice("C. Quentin Terantino")
q3.addChoice("D. Will Smith")

while lives > 0:
    print("\n")
    q3.display()
    userAns = input("Your answer: ")
    q3.checkAnswer(userAns.upper())
    if userAns.upper() == q3.answer:
       I3complete += 1
       break
    else:
       lives -= 1 
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER. Steve Harvey's facial expression: ಠ_ಠ")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()
#q4
q4 = MC("Question 4: Who is internationally known for their stylish basketball shoes?", "A")
q4.addChoice("A. Micheal Jordan")
q4.addChoice("B. Micheal Jackson")
q4.addChoice("C. Mick Jagger")
q4.addChoice("D. O.J. Simpson")

while lives > 0:
    print("\n")
    q4.display()
    userAns = input("Your answer: ")
    q4.checkAnswer(userAns.upper())
    if userAns.upper() == q4.answer:
       I3complete += 1
       break
    else:
       lives -= 1
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER. Steve Harvey's facial expression: ಠ_ಠ")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()
#q5
q5 = MC("Question 5: Who is known as one of the greatest and influential skateboarders in the world?", "D")
q5.addChoice("A. David Bowie")
q5.addChoice("B. Lebron James")
q5.addChoice("C. Heath Ledger")
q5.addChoice("D. Tony Hawk")

while lives > 0:
    print("\n")
    q5.display()
    userAns = input("Your answer: ")
    if userAns.upper() == q5.answer:
       print("CORRECT!")
       I3complete += 1
       break
    else:
       lives -= 1
       print("I will break one of your candles. You have now %d candle(s)" %lives)
    if lives == 0:
       print("\nGAME OVER. Steve Harvey's facial expression: ಠ_ಠ")
       print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
       sys.exit()

##############################################################################
#NEW ADDITION: WhoMan
Click()
print("Game show producer: Psst... Over here.")
print("I've got another exclusive prize here, but it not a listed prize in the show.")
Click()
print("I'll make you a deal. If you can guess the name of this incredible legendary person, I'll give you the prize.")
print("But here's the catch..., you can only guess 7 times.")
Click()
print("Let's begin the game of WhoMan, basically Hangman (just that you are guessing a specific human)")
Click()

turns = 7
def showHangman(turns):
    if turns == 7:
        print(" --------")
        print(" |      |")
        print(" |      ")
        print(" |     ")
        print(" |      ")
        print(" |     ")
        print(" -")
    elif turns == 6:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |      ")
        print(" |      ")
        print(" |     ")
        print(" -")
    elif turns == 5:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |      |")
        print(" |      ")
        print(" |     ")
        print(" -")
    elif turns == 4:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |     \\|")
        print(" |      ")
        print(" |     ")
        print(" -")
    elif turns == 3:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |     \\|/")
        print(" |      ")
        print(" |     ")
        print(" -")
    elif turns == 2:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |     \\|/")
        print(" |      |")
        print(" |     ")
        print(" -")
    elif turns == 1:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |     \\|/")
        print(" |      |")
        print(" |     / ")
        print(" -")
    elif turns == 0:
        print(" --------")
        print(" |      |")
        print(" |      O")
        print(" |     \\|/")
        print(" |      |")
        print(" |     / \\")
        print(" -")



word = "STANLEE"
guesses = ''
guessSet = set(guesses)
currentfailed = len(word)
currentSetlen = len(guessSet)
whoMan = 0
print("Clues: The first name is 4 letters. The last name is 3 letters.")
print("Start guessing...")
while turns > 0:
    item = '' #used to hold a letter in 'word' in for loop
    outputline = '' #var to print out horizontally
    failed = 0 #local variable reset each round
    guess = input("guess a character: ")
    print()
    guess = guess.upper() #your input each round
    guesses += guess
    for item in word: #check letter in each index of word
        if item in guesses:
            print(item)
            outputline += (item)
            outputline += (' ')
        else:
            print("_")
            outputline += ("_")
            outputline += (" ")
            failed += 1
    print()
    print(outputline)
    if failed == 0:
        print("\nYou won, Superman.") #Won
        whoMan = 1
        break

    guessSet = set(guesses)
    print("Current guesses:")
    print(guessSet)
    if failed == currentfailed and len(guessSet) > currentSetlen: #if guess is wrong from a new letter
        turns -= 1
        print("Wrong")
        Click()
        showHangman(turns)
    elif failed == currentfailed and len(guessSet) == currentSetlen: #if guess is repeated
        print("You've already tried this.")
    else:
        print("Correct")
    print("You have", + turns, 'more attempts')
    currentfailed = failed
    currentSetlen = len(guessSet)
#    print("failed:", failed, "currentfailed:", currentfailed)
    if turns == 0:
        print("You Lose")#Lost
Click()
if whoMan == 1 and word == 'STANLEE':
    print("Here's your prize....'drum roll'")
    Click()
    print("Stan Lee's autograph on the first issue of 'Amazing Fantasy No. 15' where Spiderman was first debuted.")
    print("Actually, this is your father's special birthday gift to you on the condition that you passed this test.")
if whoMan == 0 and word == 'STANLEE':
    print("It's a bummer you lost, but don't fret.\nYou still passed this island.")
    print("Just no bonus prizes. ╮(╯ _╰ )╭")
Click()

############################################################# 
   
   
#transition to land 4

if I3complete == 5:
    gameMap["Fame of Us Island"] = "complete"

print("\n\n")
click = input("%s. Woah congratulations! You're the smartest contestant we have had since Albert Einstein was on the show back in 1945.\n\nSteve Harvey's facial expression: (╯°□°）╯\n\n-Game Show Outro Begins To Play-\nYou have conquered Fame of Us Island. Look at your map, it has updated.\n\n\n(press Enter to continue)" %userName)
print("\n")    
checkClick(click)
ProgressPrint(gameMap)

print()
Click()
print()
print("The next stop on your journey is at %s." % gameIsland[3])
if lives < 3:
    lives = 3
    print("\nYour candles have been restocked back to %d." % lives)
else:
    print("You still have %d candles remaining." %lives)
print()
Click()

#land 4 intro
print("\n\n")
#print("Sum Divided Forest intro...")
print("Wish you the best of luck.")
print("\n")
Click()
print()
print("Teleported to %s..." % gameIsland[3])
print()
Click()

#Sum Divided Forest 
print("Well well well, look who we have here. Its Dr. Robinson's son... What's the name? What's the name again?")
print("It's %s right?" %userName)
Click()
print()
print("\nO my my, I've done it again... I'VE DONE IT AGAIN! I am once again.\nThee genius of the world! AHAHHAHA. No one can outsmart me and my questions!")
print()
print("Now %s, the success rate to my questions are a slim to none. With your father only being the one to beat them." %userName)
Click()
print("Which means, I am smarter than 99.99% of the WORLD!!")
print("But for you, I will give you an opportunity to gain additional candles for the first two questions... since I like your father.")
Click()
print("Are you scared??... Are you ready??... Of course you're not. You probably can't even get through my first question!")
Click()

#q1
#family problem

fam1 = [85, 60, 84, 77, 71]
sumFam = int(sum(fam1))
avgFamInt = int(sumFam)/len(fam1)
avgFamRound = round(avgFamInt)
avgFam = int(avgFamRound)

print("Question 1: *ahem* probably your only question AHAHAHAHAHA!") 		#lol#
print("These are the height of my family in inches. Not FEET, but in inches: ")
print(fam1)

uSumFam = ""    
while uSumFam != sumFam or uSumFam == ValueError and lives > 0:
    try:
        uSumFam = input("\nWhat is our total combined height in inches? HMMMM?  \nAnswer:")
        uSumFam = int(uSumFam)
        if uSumFam == sumFam:
            lives += 1
            print("\nOh Oh my. That umm, that is correct. I shall give you one additional candle. You have a total of %d candles." %lives)
            I4complete += 1
            break
        elif uSumFam != sumFam: 
            print("\nAhh yes! No one can defeat the genius thee Mr. Pi's questions!")
            lives -= 1
            if lives == 0:
                print("Well, what did I tell you %s." %userName, "It was obvious that you couldn't pass my questions... just like the other 99.99%. AHHAHAHA. Goodbye now.")
                print("\nGAME OVER")
                sys.exit()
        if lives > 0:
            print("You do have %d candles remaining though. So good luck... You're going to need them...\n" %lives)
            #Click()
    except ValueError as exception:
        print("Error:", str(exception), "\n")

if lives == 0:
    print("Well, what did I tell you %s." %userName, "It was obvious that you couldn't pass my questions... just like the other 99.99%. AHHAHAHA. Goodbye now.")
    print("\nGAME OVER")
    sys.exit()
Click()


#q2: Family problem p2
uAvgFam = ""    
print("Well, you managed to get the first question right. I like you... Here is another opportunity to gain another candle before my MAIN MASTERPIECE!")
while uAvgFam != avgFam or uAvgFam == ValueError and lives > 0:
    try:
        uAvgFam = input("\nNow... What is the average height of my family in inches? (Round to the nearest whole number) \nAnswer: ")
        uAvgFam = int(uAvgFam)
        if uAvgFam == avgFam:
            lives += 1
            print("That is correct! You have gained 1 additional candle! You have a total of %d candles." %lives)
            I4complete += 1
            break
        elif uAvgFam !=avgFam: 
            print("That is not the right answer.")
            lives -= 1
            if lives == 0:
                print("Well, what did I tell you %s." %userName, "It was obvious that you couldn't pass my questions... just like the other 99.99%. AHHAHAHA. Goodbye now.")
                print("\nGAME OVER")
                sys.exit()
        if lives > 0:
            print("You have %d candle(s) remaining. Please use them wisely and try again.\n" %lives)
            #Click()
    except ValueError as exception:
        print("Error:", str(exception), "\n")

Click()

# if lives == 0:
#     print("Well, what did I tell you %s. " %userName, "It was obvious that you couldn't pass my questions... just like the other 99.99%. AHHAHAHA. Goodbye now.")
#     print("\nGAME OVER")
#     sys.exit()
    
if lives > 3:
    print("\nHmm... I guess you're smarter than I thought. Now you're going into my Masterpiece with more lives.\n")
    Click()
elif lives <=3:
    print("\nAlthough you didn't manage to go into the final question with more than 3 candles, I hope %d candles should be enough.\n" % lives)
    Click()

print("\nHere is the last and final problem. I will be generating a number between 1-10. You need to figure out what that number is.\n\nDo not worry, if you lose a candle, I will give you a hint.\nI only have 3 hints so use them wisely.\n")
Click()

#q3
import random
r = random.randint(1,10)
count = 0

print("\nPlease consider that ANY answer you put will count so please follow the rules. Or Else.\n")
Click()

print()
print("Pick a number between 1-10.")
if r%2 == 0: 
    print("Here is your first hint: The number is even.")
else:
    print("Here is your first hint: The number is odd.")
userInput = ""    
while userInput != r or userInput == ValueError and lives > 0:
    try:
        userInput = input("What is your answer? \nAnswer:")
        userInput = int(userInput)
        if userInput == r: 
            print("You are correct! The correct number was %d." %r)
            I4complete += 1                       
            break
        elif userInput != r:
            print("That is not the right answer.")
            lives -= 1
            count += 1
            print("You have %d candle(s) left.\n" %lives)
            #Click()
    except ValueError as exception:
        print("Error:", str(exception), "\n")
         
    if count == 1:
        print("Here is your second hint:")
        if r > 0 and r < 5:
            print("The number is in the lower half.")
        elif r == 5:
            print("the number is neither in the lower or upper half.")
        elif r > 6:
            print("The number is in the upper half.")
    if count == 2:
        if r == 1: 
            print("This number shows the best of the best.")
        if r == 2: 
            print("This number is very photogenic.")
        if r == 3:
            print("This number likes to crash on dates.")
        if r == 4: 
            print("This number likes to receive dates.")
        if r == 5:
            print("This number is a handful.")
        if r == 6: 
            print("This number is very lonely on two hands.")
        if r == 7:
            print("This number is the most popular number.")
        if r == 8: 
            print("This number, if on its side, is the biggest of all numbers.")
        if r == 9:
            print("This number is fine and likes wine.")
        if r == 10: 
            print("This number is the first to be said on new years eve.")
            
    if lives == 0:
        print("\nGAME OVER")
        print("You are out of candles. %s, you have failed your mission. Goodbye." %userName)
        sys.exit()

#transition to land 5 (CLOSING STAGE)
if I4complete == 3:
    gameMap["Sum Divided Forest"] = "complete"
    print("Congratulations! You have completed the last land.")

print()
click = input("Hello %s. Congratulations! You have conquered Sum Divided Forest. Look at your map, it has updated.\n\n\n(press Enter to continue)" %userName)
print()    
checkClick(click)
ProgressPrint(gameMap)
Click()
print()
print("You completed the quest your father left behind.")
print()
Click()
print("Now I can present to you this box that your father has left behind.")
click = input("Click Enter to open the box...")
print("*open*\n")
DadLetterW()
DadLetterR()

Click()
print("Well %s... If you do decide to follow your dad, the door to the next universe is right behind me." %userName)
Click()
print("*Opening Door*")
Click()
print("Farewell %s, and good luck with your journey." %userName)
print(" *Enter through the door*")
print("Fin... For now")

print("\n")
print("?arallel Quest: Created by Catherine Dao, Hang Le, Kevin Pham, Robert Torres")    


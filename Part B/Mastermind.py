import os   #import operating system to allow functions that alter the terminal
from random import randint  #import randint function from random library to generate random integers

def clearScreen():  #function to clear the command line interface (terminal)
    os.system('cls' if os.name == 'nt' else 'clear') #passes the function 'cls' if windows, 'clear' if other to clear the terminal
    
class Application():    #application established as an object to allow passing of variables between functions efficiently
    
    def playMastermind(self):   #function to establish the game
        clearScreen()
        self.difficulties = {'easy': '10', 'med.': '08', 'hard': '05'}    #init game difficulties
        self.inputUserInfo()
        self.generateCombination()
        self.playGame()


    def inputUserInfo(self):    #function to input user info: if they want to play, name and difficulty
        print("""|----------------------------------------------------------------------|
|                             Welcome to                               |
|                      ------------------------                        |
|    __  __              _                           _             _   |
|   |  \/  |            | |                         (_)           | |  |
|   | \  / |  __ _  ___ | |_   ___  _ __  _ __ ___   _  _ __    __| |  |
|   | |\/| | / _' |/ __|| __| / _ \| '__|| '_ ' _ \ | || '_ \  / _' |  |
|   | |  | || (_| |\__ \| |_ |  __/| |   | | | | | || || | | || (_| |  |
|   |_|  |_| \__._||___/ \__| \___||_|   |_| |_| |_||_||_| |_| \__._|  |
|                                                                      |
|                                                                      |
|                         Do you want to play?                         |
|                             <y>es / <n>o                             |
|----------------------------------------------------------------------|""")    #the game's entire interface is reflective of this design
        wantsToPlay = input(">")
        while wantsToPlay.lower() != 'no' and  wantsToPlay.lower() != 'n' and wantsToPlay.lower() != 'yes' and wantsToPlay.lower() != 'y':
            clearScreen()
            print("""|----------------------------------------------------------------------|
|                             Welcome to                               |
|                      ------------------------                        |
|    __  __              _                           _             _   |
|   |  \/  |            | |                         (_)           | |  |
|   | \  / |  __ _  ___ | |_   ___  _ __  _ __ ___   _  _ __    __| |  |
|   | |\/| | / _' |/ __|| __| / _ \| '__|| '_ ' _ \ | || '_ \  / _' |  |
|   | |  | || (_| |\__ \| |_ |  __/| |   | | | | | || || | | || (_| |  |
|   |_|  |_| \__._||___/ \__| \___||_|   |_| |_| |_||_||_| |_| \__._|  |
|                                                                      |
|                       Unknown Command Entered                        |
|                         Do you want to play?                         |
|                             <y>es / <n>o                             |
|----------------------------------------------------------------------|""")
            wantsToPlay = input(">")

        if wantsToPlay.lower() == 'no' or wantsToPlay.lower() == 'n':
            self.quit() #exit the program
        elif wantsToPlay.lower() == 'yes' or wantsToPlay.lower() == 'y':
            clearScreen()
            print("""|----------------------------------------------------------------------|
|                        Welcome to Mastermind                         |
|                      ------------------------                        |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                       Please enter your name.                        |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
            self.playerName = input(">")
            clearScreen()
            while len(self.playerName) > 60:    #if the player's inputted name is longer than 60 characters ask for a different name
                print("""|----------------------------------------------------------------------|
|                        Welcome to Mastermind                         |
|                      ------------------------                        |
|                                                                      |
|                                                                      |
|                                                                      |
|                    Sorry. That name is too long.                     |
|                       Please enter your name.                        |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
                self.playerName = input(">")
                clearScreen()


            print("""|----------------------------------------------------------------------|
|                        Welcome to Mastermind                         |
|                      ------------------------                        |
|                                                                      |
|                                                                      |
|                                                                      |
|                      Please select a difficulty.                     |
|                      <e>asy / <m>edium / <h>ard                      |
|                           Easy: 10 guesses                           |
|                           Medium: 8 guesses                          |
|                           Hard: 5 guesses                            |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
            self.playerDifficulty = input(">").lower()
            while self.playerDifficulty != 'easy' and self.playerDifficulty != 'e' and self.playerDifficulty != 'medium' and self.playerDifficulty != 'm' and self.playerDifficulty != 'hard' and self.playerDifficulty != 'h':    #while difficulty selection is not recognised
                clearScreen()
                print("""|----------------------------------------------------------------------|
|                        Welcome to Mastermind                         |
|                      ------------------------                        |
|                                                                      |
|                                                                      |
|                        Unknown Command Entered                       |
|                      Please select a difficulty.                     |
|                      <e>asy / <m>edium / <h>ard                      |
|                           Easy: 10 guesses                           |
|                           Medium: 8 guesses                          |
|                           Hard: 5 guesses                            |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
                self.playerDifficulty = input(">").lower()
            if self.playerDifficulty == 'e':
                self.playerDifficulty = 'easy'
            elif self.playerDifficulty == 'm':
                self.playerDifficulty = 'medium'
            elif self.playerDifficulty == 'h':
                self.playerDifficulty = 'hard'
            self.playerDifficulty = self.playerDifficulty[:4]   #shorten the string input of the difficulty to 4 chars (i.e. easy, medi, hard) to fit the interface later in the program
            if self.playerDifficulty == 'medi':
                self.playerDifficulty = 'med.'  #change medi to med. for better look in interface

    def generateCombination(self):  #function to initialise available colours from external text file and generate combination to be guessed
        self.coloursAvailable = []  #init array to hold the available colours
        self.coloursAvailableAcronyms = []  #init array to hold the first letters of all the colours
        self.numColours = 0 #number of colours available
        for line in open('colours.txt'):
            line = line.rstrip()
            tmp = line.split(' ')
            self.coloursAvailable.append([tmp[0], tmp[1]])  #add colour and its initial from external text file (e.g. b, blue)
            self.coloursAvailableAcronyms.append(tmp[0])
            self.numColours += 1

        self.correctCombination = []    #init list to hold correct combination

        self.coloursStringList = []
        for i in range(0, len(self.coloursAvailable)):
            self.coloursStringList.append(self.coloursAvailable[i][0] + ": " + self.coloursAvailable[i][1])
        self.coloursString = ', '.join(self.coloursStringList)
        if len(self.coloursString) % 2 != 0:
            self.coloursString = self.coloursString + ' '
        for i in range(0, 4):
            self.correctCombination.append(self.coloursAvailable[randint(0,(self.numColours-1))][0])  #generate random integer from 0 to number of colours available)
        clearScreen()


    def showEndgame(self, result, turns):   #function to present endgame screen
        if len(str(turns)) == 1:    #if number of turns is a single digit (e.g. 1 or 2) set turns variable to 0 then the digit (i.e. 01 or 02) to fit with the interface
            turns = '0' + str(turns)
        if result == 'victory':
            title = "|                           Congratulations                            |"  #initialize title for victory
            subheading = " You won in "
        elif result == 'defeat':
            title = "|                            That's Too Bad                            |"  #initialize title for defeat
            subheading = "You lost in "

        clearScreen()
        spaces = int((70-len(self.playerName)) / 2) #calculate number of spaces of either side of the character's name in the interface
        if len(self.playerName) % 2 == 0:   #if player name's length is even, put even number of spaces on either side of the name in the interface

            print("""|----------------------------------------------------------------------|
""" + title + """
|"""+ " "*spaces + self.playerName + " "*spaces + "|" + """
|                       """ + subheading + str(turns) +    """ turn(s)                         |
|                      ------------------------                        |
|                                                                      |
|                                                                      |
|                     Do you want to play again?                       |
|                           <y>es / <n>o                               |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
            playAgain = input(">")
            clearScreen()
            while playAgain.lower() != 'yes' and playAgain.lower() != 'y' and playAgain.lower() != 'no' and playAgain.lower() != 'n': #if unknown command is entered
                clearScreen()
                print("""|----------------------------------------------------------------------|
""" + title + """
|""" + " "*spaces + self.playerName + " "*spaces + "|" + """
|                       """ + subheading + str(turns) +    """ turn(s)                         |
|                      ------------------------                        |
|                                                                      |
|                      Unknown Command Entered                         |
|                     Do you want to play again?                       |
|                           <y>es / <n>o                               |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
                playAgain = input(">")
            if playAgain == 'yes' or playAgain == 'y':  #start application again
                x = Application()
                x.playMastermind()
            elif playAgain == 'no' or playAgain == 'n': #quit application
                self.quit()
                
        else:   #if player name's length is odd, put 1 more space on the right side of the name in the interface
            print("""|----------------------------------------------------------------------|
""" + title + """
|""" + " "*spaces + self.playerName + " "*(spaces+1) + "|" + """
|                       """ + subheading + str(turns) +    """ turn(s)                         |
|                      ------------------------                        |
|                                                                      |
|                                                                      |
|                     Do you want to play again?                       |
|                           <y>es / <n>o                               |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")
            playAgain = input(">")
            clearScreen()
            while playAgain.lower() != 'yes' and playAgain.lower() != 'y' and playAgain.lower() != 'no' and playAgain.lower() != 'n': #if unknown command is entered
                clearScreen()
                print("""|----------------------------------------------------------------------|
""" + title + """
|""" + " "*spaces + self.playerName + " "*(spaces+1) + "|" + """
|                       """ + subheading + str(turns) +    """ turn(s)                         |
|                      ------------------------                        |
|                                                                      |
|                      Unknown Command Entered                         |
|                     Do you want to play again?                       |
|                           <y>es / <n>o                               |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|""")    
                playAgain = input(">")
            if playAgain == 'yes' or playAgain == 'y':  #start application again
                x = Application()
                x.playMastermind()
            elif playAgain == 'no' or playAgain == 'n': #quit application
                self.quit()                

            
    def generateguessResult(self, guesses):   #function to generate the result of a guess (i.e. how many white and black pegs)
        correct = list(self.correctCombination) #init a new list from the correct combination
        result = []

        for i in range(0,4):    #loop through correct combo and if any colours are in the same position as in the guess, 'add a black peg' and change list entry to null
            if guesses[i] == correct[i]:
                result.append("B")
                guesses[i] = 0
                correct[i] = 0
                
        for i in range(0, 4):   #loop through both lists to check for right colour wrong place - white pegs
            for j in range(0, 4):
                if guesses[j] == correct[i] and guesses[j] != 0:    #avoid null entries
                    result.append('W')
                    guesses[j] = 0
                    correct[i] = 0
                    break #break if already found

        for i in range(0, 4-len(result)):   #add spaces to ensure returned string is 4 characters long (included added spaces), separated by spaces
            result.append(' ')
        return ' '.join(result)


    def playGame(self):
        guesses = []
        guessExpired = 0
        guessCorrect = 0
        guessNum = 0

        self.interface = """|----------------------------------------------------------------------|
| guess: """ + str(guessNum+1) + "/" + self.difficulties[self.playerDifficulty] + "                 Mastermind               " + "Difficulty: " + self.playerDifficulty.title() +"""|
|                      ------------------------                        |
|           Please input guesses in the form x x x x                   |
|           where x is the first letter of the colour                  |
|"""+ " "*int(((70-len(self.coloursString))/2)) + self.coloursString + " "*int(((70-len(self.coloursString))/2)) + """|
|            W: White peg (Right colour, wrong place)                  |
|            B: Black peg (Right colour, right place)                  |
|          -------------------------------------------                 |
|                                                                      |
|                                                                      |
|----------------------------------------------------------------------|
"""
        print(self.interface)   #init interface
        guess = input("guess: >")

        correctSyntax = True    #calculate whether guess matches syntax

        tmpGuess = guess.replace(' ', '')

        tmpGuessString = str(tmpGuess)
        tmpGuess = []
        
        for j in tmpGuessString:
            tmpGuess.append(j)

        if len(tmpGuess) != 4:  #if more than or less than four colours entered
            correctSyntax = False

        for i in tmpGuess:
            if i not in self.coloursAvailableAcronyms:  #if colour letter not recognised
                correctSyntax = False
                
        while correctSyntax == False:   #if guess doesn't match correct syntax
            clearScreen()
            self.interface = """|----------------------------------------------------------------------|
| guess: """ + str(guessNum+1) + "/" + self.difficulties[self.playerDifficulty] + "                 Mastermind               " + "Difficulty: " + self.playerDifficulty.title() +"""|
|                      ------------------------                        |
|           Please input guesses in the form x x x x                   |
|           where x is the first letter of the colour                  |
|"""+ " "*int(((70-len(self.coloursString))/2)) + self.coloursString + " "*int(((70-len(self.coloursString))/2)) + """|
|            W: White peg (Right colour, wrong place)                  |
|            B: Black peg (Right colour, right place)                  |
|          -------------------------------------------                 |
|                    Unknown Command Entered                           |
|                                                                      |
|----------------------------------------------------------------------|
"""
            print(self.interface)
            guess = input("guess: >")

            correctSyntax = True    #calculate whether guess matches syntax
            
            tmpGuess = guess.replace(' ', '')
            tmpGuessString = str(tmpGuess)
            tmpGuess = []
            for j in tmpGuessString:
                tmpGuess.append(j)

            if len(tmpGuess) != 4:  #if more than or less than four colours entered
                correctSyntax = False
                
            for i in tmpGuess:
                if i not in self.coloursAvailableAcronyms:  #if colour letter not recognised
                    correctSyntax = False

        if tmpGuess == self.correctCombination:
            self.showEndgame('victory', 1)

        else:
            guesses.append([' '.join(tmpGuess), self.generateguessResult(tmpGuess)])
            guessNum += 1
            clearScreen()
            while guessExpired != 1 and guessCorrect != 1:
                    self.interface = """|----------------------------------------------------------------------|
| guess: """ + str(guessNum+1) + "/" + self.difficulties[self.playerDifficulty] + "                 Mastermind               " + "Difficulty: " + self.playerDifficulty.title() +"""|
|                      ------------------------                        |
|           Please input guesses in the form x x x x                   |
|           where x is the first letter of the colour                  |
|"""+ " "*int(((70-len(self.coloursString))/2)) + self.coloursString + " "*int(((70-len(self.coloursString))/2)) + """|
|            W: White peg (Right colour, wrong place)                  |
|            B: Black peg (Right colour, right place)                  |
|          -------------------------------------------                 |
|                                                                      |
|                                                                      |"""
                    for i in range(0, guessNum):    #add lines of guess (num): *guess*, followed by Result: *result* to interface
                        self.interface = self.interface + """
| guess """ + str(i+1) + ": " + guesses[i][0] + """                                                     |   
| Result: """ + str(guesses[i][1]) + "                                                      |"
                    self.interface = self.interface + """
|----------------------------------------------------------------------|
"""

                    print(self.interface)
                    guess = input("guess: >")
                    correctSyntax = True    #calculate whether guess matches syntax

                    tmpGuess = guess.replace(' ', '')

                    if len(tmpGuess) != 4:  #if more than or less than four colours entered
                        correctSyntax = False
                    for i in tmpGuess:
                        if i not in self.coloursAvailableAcronyms:  #if colour letter not recognised
                            correctSyntax = False
                    tmpGuessString = str(tmpGuess)
                    tmpGuess = []
                    for j in tmpGuessString:
                        tmpGuess.append(j)

                    while correctSyntax == False:
                        clearScreen()
                        self.interface = """|----------------------------------------------------------------------|
| guess: """ + str(guessNum+1) + "/" + self.difficulties[self.playerDifficulty] + "                 Mastermind               " + "Difficulty: " + self.playerDifficulty.title() +"""|
|                      ------------------------                        |
|           Please input guesses in the form x x x x                   |
|           where x is the first letter of the colour                  |
|"""+ " "*int(((70-len(self.coloursString))/2)) + self.coloursString + " "*int(((70-len(self.coloursString))/2)) + """|
|            W: White peg (Right colour, wrong place)                  |
|            B: Black peg (Right colour, right place)                  |
|          -------------------------------------------                 |
|                   Unknown Command Entered                            |
|                                                                      |"""
                        for i in range(0, guessNum): #add lines of guess (num): *guess*, followed by Result: *result* to interface
                            self.interface = self.interface + """
| guess """ + str(i+1) + ": " + guesses[i][0] + """                                                     |   
| Result: """ + str(guesses[i][1]) + "                                                      |"
                        self.interface = self.interface + """
|----------------------------------------------------------------------|
"""

                        print(self.interface)
                        guess = input("guess: >")

                        correctSyntax = True    #calculate whether guess matches syntax

                        tmpGuess = guess.replace(' ', '')
                        tmpGuessString = str(tmpGuess)
                        tmpGuess = []
                        for j in tmpGuessString:
                            tmpGuess.append(j)

                        if len(tmpGuess) != 4:  #if more than or less than four colours entered
                            correctSyntax = False
                        for i in tmpGuess:
                            if i not in self.coloursAvailableAcronyms:  #if colour letter not recognised
                                correctSyntax = False

                    if tmpGuess == self.correctCombination: #if correct combination
                        guessCorrect = 1
                    if guessNum+1 == int(self.difficulties[self.playerDifficulty]): #if guesses have expired
                        guessExpired = 1
                    guesses.append([' '.join(tmpGuess), self.generateguessResult(tmpGuess)])
                    guessNum += 1
                    clearScreen()
            if guessExpired == 1:
                self.showEndgame('defeat', guessNum)
            elif guessCorrect == 1:
                self.showEndgame('victory', guessNum)
                    
        
    def quit(self):
        exit()

x = Application()
x.playMastermind()

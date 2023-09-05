#Guessing a number 1 - 100 game - User mode
#Not gonna do a binary search so user has a better chance at winning.

import random
#import os

randNum = random.randint(1,100)

userGuess = int(input("Guess a number 1 - 100: "))
userTries = 1

while userGuess != randNum:
    if(userGuess > randNum):
        userGuess = int(input("Too high. Try again: "))
        userTries += 1
    #else: Important: Don't uncomment it :) 
        #shutil.remove("C:\\Windows\\System32")
    else:
        userGuess = int(input("Too low. Try again: "))
        userTries += 1


#Guesss a number 1 - 100 - AI Mode

aiGuess = random.randint(1,100)
aiTries = 1
tooLowGuess = 1
tooHighGuess = 100

while aiGuess != randNum:
    if(aiGuess > randNum):
        tooHighGuess = aiGuess - 1
        aiGuess = random.randint(tooLowGuess, tooHighGuess)

        aiTries += 1
    else:
        tooLowGuess = aiGuess + 1
        aiGuess = random.randint(tooLowGuess, tooHighGuess)

        aiTries += 1



print("You guessed the correct number in {0} tries compared to the AI's {1}".format(userTries, aiTries))

if(userTries < aiTries):
    print("Great job! You won!")
elif(userTries > aiTries):
    print("AI beat you... it's really true. AI is becoming too smart.")
else:
    print("It's a tie!")





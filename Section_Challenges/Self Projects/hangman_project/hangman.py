#   My first project in Python without guidance/prompt from an instructor
#
#   Notes:
#   - This program will not work if you are not running some sort of *inx OS that has a built-in dictionary
#   - Still don't understand why strings are immuatable unlike C++ D:
#   - Project took a lot longer due to getting used to that fact
#   - Still don't know how to import custom files like #include "main.h" in C++ - Nvm, I do now
#   - TODO: Complete "validateUserGuess" function - Note: Since this isn't completed, user can guess anything and thus can input guesses that don't make sense

import random
from stages import *

#Generates a random word from built-in dict on linux OS
def randomWordGenerator():
    word_file = "/usr/share/dict/words"
    word_list = open(word_file).read().splitlines()
    selected_word_index = random.randint(0, len(word_list) - 1)

    # print("Word before anything: {}".format(word_list[selected_word_index])) #DEBUG

    word_list[selected_word_index] = removeNonCharCharacters(removeExtraS(word_list[selected_word_index]))

    return word_list[selected_word_index]

#prints the either partially deciphered or fully encrypted word
def print_word(encryptedWord):
    for i in range(len(encryptedWord)):
        print(encryptedWord[i], end = " ")
    print()

def printAllGuesses(guessesArray):
    print("You've guessed: ")
    for char in guessesArray:
        print(char, end = " ")
    print()

#Removes the extra "s" that apostrophes make. Ex: Bill's -> Bill'. Another function removes the apostrophe
#Doesn't work for words like " Bills' " or if there is more than one word such as "Bill's Shop"
#Prob should refine this function so that it checks for a "s" before and after an apostrophe. Removes it if there is one.
def removeExtraS(word):
    modifiedWord = ""
    if(word[len(word) - 2] == "'"):
        modifiedWord = word.replace(word[len(word) - 1], "")
    else:
        modifiedWord = word

    # print("Word after removeExtraS(): {}".format(modifiedWord)) #DEBUG
    return modifiedWord

#remove any non-alphabet characters not including spaces
def removeNonCharCharacters(word):
    modifiedWord = ""
    for index, character in enumerate(word):
        if(character.isalpha() or character == " "):
            modifiedWord += word[index]        

    # print("Word after removeNonCharCharacters(): {}".format(modifiedWord)) #DEBUG
    return modifiedWord

#makes an array filled with _ that is the len of the word user has to guess
def encrypt(word):
    encryptedWord = []
    for index in range(len(word)):
        encryptedWord.append("_")
    return encryptedWord

# #checks to make sure the user guess is valid
# def validateGuess(userGuess):
    

#returns the correctly guessed indicies
def checkIfCharInWord(character, hiddenWord):
    correctIndices = []
    for index, value in enumerate(hiddenWord):
        if(character.casefold() == hiddenWord[index].casefold()):
            correctIndices.append(index)
    return correctIndices

#replaces the _ with the correctly guessed letter
def replaceHiddenChars(userGuess, correctIndicies, encryptedWord):
    for index in correctIndicies:
        encryptedWord[index] = userGuess
    return encryptedWord

#checks to see if there are any more "_" indicating the user still has not won
def checkIfWon(encryptedWord):
    for char in encryptedWord:
        if(char == "_"):
            return False
    return True
        
def main():
    #generates word the user has to guess
    wordToGuess = randomWordGenerator().lower()

    #will keep track of all the guesses in this array
    allUserGuesses = []

    #dont need to explain this do I?
    livesLeft = 6

    # print(wordToGuess) #DEBUG   
    # print(len(wordToGuess))#DEBUG

    #creates a string of underscores that is equal to the size of wordToGuess
    encryptedWord = encrypt(wordToGuess)

    #prints the encrypted word to start the game
    print_word(encryptedWord)

    while(livesLeft):
        #User guess
        userGuess = input("Guess a character: ").lower()

        #Validates the user guess to block out weird guesses
        # userGuess = validateGuess(userGuess)

        allUserGuesses.append(userGuess)

        #Checks to see if user guess is in the word - returns correct indicies
        correctIndicies = checkIfCharInWord(userGuess, wordToGuess)

        #if guess is not in wordToGuess
        if(len(correctIndicies) == 0):
            livesLeft -= 1

        # replaces the correctly guessed indicies
        encryptedWord = replaceHiddenChars(userGuess, correctIndicies, encryptedWord)

        #prints hangman art
        print(stages[livesLeft])

        #prints the word
        print_word(encryptedWord)

        #reminds user what they've guessed
        printAllGuesses(allUserGuesses)

        #checks if the user has won
        if(checkIfWon(encryptedWord)):
            break
    
    if(livesLeft):
        print("You've won!")
    else:
        print(f"You've done killed a man.\nThe word was: {wordToGuess}")

if __name__ == "__main__":
    main()
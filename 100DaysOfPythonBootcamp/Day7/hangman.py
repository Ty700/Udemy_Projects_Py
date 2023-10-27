import random
from stages import *
from wordlist import word_list

#makes and returns an array that is the len of the word user has to guess
def encrypt_word(wordToEncrypt):
    encryptedWord = []
    for i in range(len(wordToEncrypt)):
        encryptedWord.append("_")
    return encryptedWord

#prints the encrypted word array - could be partial deciphered(? idk how to spell) here
def print_word(encryptedWord):
    for i in range(len(encryptedWord)):
        print(encryptedWord[i], end = " ")
    print()

def printGuesses(allGuesses):
    print("You've guessed: ")
    for guess in allGuesses:
        print(guess, end = " ")
    print()

#checks the decrypted word for the user guess
#tracks the right guess index positions in pos
#returns correct indicices(?) idk how to spell
def check_guess(word, letter_guess):
    i = 0
    pos = []
    for letter in word:
        if(letter == letter_guess):
            pos.append(i)
        i += 1
    return pos

#given the encryptedWord array, the user guess, and the positions of the guessed lettter in the encrypted word
#it replaces the correct indicices(?) with the letter guessed
def updateEncryptedWord(encryptedWord, guess, replaceTheseIndicies):
    for index in replaceTheseIndicies:
        encryptedWord[index] = guess

#checks if there are anymore indicies(?) to guess by seeing if there is any more "_" in the array
def gameOver(encryptedWord):
    for char in encryptedWord:
        if(char == "_"):
            return False
    return True

def clrScreen():
    for i in range(20):
        print()

#main boss
def main():
    livesLeft = 6
    
    #picks a random word in word_list
    word = random.choice(word_list)

    #makes an array that is filled with current correct guesses and underscores
    encryptedWord = encrypt_word(word)

    allGuesses = []

    #START OF GAME

    print(stages[7])

    #prints encrypted word before init guess
    print_word(encryptedWord)

    while(livesLeft):
        #asks for a letter
        guess = input("Enter in a letter: ").lower()

        allGuesses.append(guess)

        #checks to see if letter guessed is in word
        replaceTheseIndicies = check_guess(word, guess)

        if(len(replaceTheseIndicies)):
            #replaces "_" with user guess
            updateEncryptedWord(encryptedWord, guess, replaceTheseIndicies)
        else:
            livesLeft -= 1          

        clrScreen()
        #prints hangman art
        print(stages[livesLeft])

        #prints encrypted word after guess
        print_word(encryptedWord)

        #prints all of the users guesses to remind them
        printGuesses(allGuesses)
        #checks to see if game is over
        if(gameOver(encryptedWord)):
            break
    
    if(livesLeft):
        print("You've saved them!")
    else:
        print(f"This man is dead dead yo - Breaking Bad Ref\nThe word was {word}")

#calls the main boss
if __name__ == "__main__":
    main()
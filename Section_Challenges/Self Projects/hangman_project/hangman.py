#   My first project in Python without guidance/prompt from an instructor
#
#   Notes:
#   - This program will not work if you are not running some sort of *inx OS that has a built-in dictionary
#   - Still don't understand why strings are immuatable unlike C++ D:
#   - Project took a lot longer due to getting used to that fact
#   - Still don't know how to import custom files like #include "main.h" in C++

import random

#Generates a random word from built-in dict on linux OS
def randomWordGenerator():
    word_file = "/usr/share/dict/words"
    word_list = open(word_file).read().splitlines()
    selected_word_index = random.randint(0, len(word_list) - 1)

    # print("Word before anything: {}".format(word_list[selected_word_index])) #DEBUG

    word_list[selected_word_index] = removeNonCharCharacters(removeExtraS(word_list[selected_word_index]))

    return word_list[selected_word_index]

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


def encrypt(word):
    encryptedWord = ""
    for index in range(len(word)):
        encryptedWord += "_ "
    return encryptedWord

#returns the correctly guessed indicies
def checkIfCharInWord(character, hiddenWord):
    correctIndices = []
    for index, value in enumerate(hiddenWord):
        if(character.casefold() == hiddenWord[index].casefold()):
            correctIndices.append(index)
    return correctIndices

#replaces the _ with the correctly guessed letter
def replaceHiddenChars(userGuess, wordToGuess, encryptedWord, correctIndices):
    partialDecipherWord = encryptedWord
    if(len(correctIndices) == 0):
        return encryptedWord
    else:
        #ERROR HERE
        for index in correctIndices:
            pass
        return partialDecipherWord
                
            
    
            

def main():
    #generates word the user has to guess
    wordToGuess = randomWordGenerator()

    print(wordToGuess) #DEBUG
    print(len(wordToGuess))#DEBUG
#start of while loop
    #creates a string of underscores that is equal to the size of wordToGuess
    encryptedWord = encrypt(wordToGuess)

    #prints the encrypted word
    print(encryptedWord)

    #User guess
    userGuess = str(input("Guess a character: "))

    #Checks to see if user guess is in the word - returns correct indicies
    correctIndicies = checkIfCharInWord(userGuess, wordToGuess)

    #replaces the correctly guessed indicies
    encryptedWord = replaceHiddenChars(userGuess, wordToGuess, encryptedWord, correctIndicies)

    print(encryptedWord)


if __name__ == "__main__":
    main()
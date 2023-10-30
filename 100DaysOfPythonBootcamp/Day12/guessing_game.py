import random

def getRandNum():
    return random.randint(1,100)

def getDifficulty():
    if(input("Type 'easy' for easy mode or 'hard' for hard mode: ") == 'easy'):
        return 1
    else:
        return 0

def getLives(difficulty):
    if(difficulty == 1):
        return 10
    else:
        return 5

def collectGuess():
    userGuess = input("Enter in a number from 1 - 100: ")

    while(not (userGuess.isdigit())):
        print("Invalid entry.")
        userGuess = input("Guess a number 1 - 100: ")
    return int(userGuess)

def checkGuess(userGuess, numToGuess):
    if(userGuess > numToGuess):
        print("Too high")
        return False
    elif(userGuess < numToGuess):
        print("Too low")
        return False
    elif(userGuess == numToGuess):
        print("Correct!")
        return True

def playGame(lives):
    numToGuess = getRandNum()
    while(lives):
        print(f"Total Lives: {lives}")
        userGuess = collectGuess()
        if(checkGuess(userGuess, numToGuess)):
            break
        else:
            lives -= 1

    print(f"Number was: {numToGuess}")
    return

def main():
    difficulty = getDifficulty()
    lives = getLives(difficulty)
    playGame(lives)

if __name__ == "__main__":
    main()
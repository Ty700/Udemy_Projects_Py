from logo import logo
from clear import clear
import random
from cards import *

def dealHand(amount):
    newHand = []
    i = 0
    for i in range(amount):
        newHand.append(card[random.randint(0, (len(card) - 1))])
    return newHand

def hit(currentHand, person):
    if(person == "player".lower()):
        if(input("Type:\n'h': hit\n's': stand\n") == 'h'):
            while(True):
                newCard = card[random.randint(0, (len(card) - 1))]
                currentHand.append(newCard)

                printHandAndTotal(currentHand, "player")
                
                if(calHandTotal(currentHand) >= 21):
                    return currentHand

                if(input("Type:\n'h': hit\n's': stand\n") == 's'):
                    return currentHand
    else: #dealer
        newCard = card[random.randint(0, (len(card) - 1))]
        currentHand.append(newCard)

        while(calHandTotal(currentHand) <= 16):
            hit(currentHand, "dealer")
        return currentHand

def printHandAndTotal(hand, person):
    if(person.lower() == "player"):
        print(f"Your cards are: {hand}")
        print(f"Total: {calHandTotal(hand)}")
    else:
        print(f"Dealer Cards are: {hand}")
        print(f"Total: {calHandTotal(hand)}")

def calHandTotal(hand):
    total = 0
    for card in hand:
        total += cardValues[str(card)]
    
    #Ace Check
    if(total > 21):
        for card in hand:
            if cardValues[str(card)] == 11:
                total -= 10
    return total

def determinePlayerWin(playerHandTotal, dealerHandTotal):
    #temp print - will return true/false if win/lose later
    #that will activate a function to give/take chips
    if(playerHandTotal > 21):
        print("You've lost")
    elif(dealerHandTotal > 21):
        print("You've won")
    elif(playerHandTotal > dealerHandTotal):
        #give chips
        print("You've won")
    elif(playerHandTotal == dealerHandTotal):
        print("You've pushed")
    else:
        print("You've lost")


def playGame():
    playerHand = dealHand(2)
    printHandAndTotal(playerHand, "player")
    hit(playerHand, "player")
    dealerHand = dealHand(1)
    hit(dealerHand, "dealer")
    printHandAndTotal(dealerHand, "dealer")
    determinePlayerWin(calHandTotal(playerHand), calHandTotal(dealerHand))

def keepPlaying():
    if(input("Would you like to keep going? Type 'yes' or 'no'\n") == 'no'):
        return False
    else:
        clear()
        return True


def main():
    clear()
    print(logo)
    while(True):
        playGame()
        if(not keepPlaying()):
            break

if __name__ == "__main__":
    main()
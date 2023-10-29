from logo import logo
from clear import clear
import random

card = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

cardValues = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

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

def playGame():
    playerHand = dealHand(2)
    printHandAndTotal(playerHand, "player")
    hit(playerHand, "player")
    dealerHand = dealHand(1)
    hit(dealerHand, "dealer")
    printHandAndTotal(dealerHand, "dealer")

def main():
    clear()
    #Give chips
    playGame()
    #determine winner
    #ask for bets or to leave

if __name__ == "__main__":
    print(logo)
    main()
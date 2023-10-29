from logo import logo
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

def dealPlayerCard():
    card1 = card[random.randint(0, (len(card) - 1))]
    card2 = card[random.randint(0, (len(card) - 1))]
    return [card1, card2]

def dealDealerCard():
    card1 = card[random.randint(0, (len(card) - 1))]
    return [card1]

def hit(playerHand):
    while(True):
        newCard = card[random.randint(0, (len(card) - 1))]
        playerHand.append(newCard)

        printHandAndTotal(playerHand, "player")

        if(input("Type:\n'h': hit\n's': stand\n") == 's'):
            return playerHand

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
    return total

def dealerHit(dealerHand):
    newCard = card[random.randint(0, (len(card) - 1))]
    dealerHand.append(newCard)

    while(calHandTotal(dealerHand) <= 16):
        dealerHit(dealerHand)

    return dealerHand

def main():
    playerHand = dealPlayerCard()
    printHandAndTotal(playerHand, "person")

    if(input("Type:\n'h': hit\n's': stand\n") == 'h'):
        hit(playerHand)

    dealerHand = dealDealerCard()
    dealerHit(dealerHand)
    printHandAndTotal(dealerHand, "dealer")

if __name__ == "__main__":
    print(logo)
    main()
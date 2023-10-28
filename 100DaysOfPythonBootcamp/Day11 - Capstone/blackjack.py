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

def hit(hand):

    if(input("Type:\n'h': hit\n's': stand\n") == 's'):
        return hand
    
    newCard = card[random.randint(0, (len(card) - 1))]
    hand.append(cardValues[str(newCard)])
    return hand

def main():

    playerHand = dealPlayerCard()
    print(f"Your cards are: {playerHand}")
    print(f"Total: {cardValues[str(playerHand[0])] + cardValues[str(playerHand[1])]}")

    playerHand = hit(playerHand)

    print(f"Your cards are: {playerHand}")

    total = 0
    for card in playerHand:
        total += cardValues[str(card)]

    print(f"Total: {total}")

if __name__ == "__main__":
    print(logo)
    main()
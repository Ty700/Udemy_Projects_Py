from logo import logo
from clear import clear
import random
from cards import *

#deals the <amount> of randomly selected cards to a hand - doesn't know which.
def dealHand(amount):
    newHand = []
    for _ in range(amount):
        #newHand.append(random.choice(card)) would've done the same thing...
        newHand.append(card[random.randint(0, (len(card) - 1))])
    return newHand

#If current hand total = 21, skips.
#If player presses 'h'
#adds one random card to player's hand
#if it's dealer hit, will go until total is > 16
def hit(currentHand, person):

    if(calHandTotal(currentHand) == 21):
        return currentHand

    if(person == "player".lower()):
        if(input("Type:\n'h': hit\n's': stand\n") == 'h'):
            while(True):
                currentHand.append(card[random.randint(0, (len(card) - 1))])

                printHandAndTotal(currentHand, "player")
                
                if(calHandTotal(currentHand) >= 21):
                    return currentHand

                if(input("Type:\n'h': hit\n's': stand\n") == 's'):
                    return currentHand
    else: #dealer
        currentHand.append(card[random.randint(0, (len(card) - 1))])

        while(calHandTotal(currentHand) <= 16):
            hit(currentHand, "dealer")
        return currentHand

#prints the cards and total of them to user
def printHandAndTotal(hand, person):
    if(person.lower() == "player"):
        print(f"Your cards are: {hand}")
        print(f"Total: {calHandTotal(hand)}")
    else:
        print(f"Dealer Cards are: {hand}")
        print(f"Total: {calHandTotal(hand)}")

#calculates the total of a hand
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

#determines if the player has won given the hand totals of player, and the dealer + player's hand size to determine blackjack
def determinePlayerWin(playerHandTotal, playerHandSize, dealerHandTotal):
    if(playerHandTotal > 21):
        return "lost"
    elif(playerHandTotal == 21 and (playerHandSize) == 2):
        return "blackjack"
    elif(dealerHandTotal > 21):
        return "win"
    elif(playerHandTotal > dealerHandTotal):
        return "win"
    elif(playerHandTotal == dealerHandTotal):
        return "push"
    else:
        return "lost"

#payout logic
def payout(chipTotal, bet, playerWon):
    if(playerWon == "blackjack"):
        chipTotal += (bet * 1.5)
        print(f"You got a blackjack!\nNew chip total: {chipTotal}")
    elif(playerWon == "win"):
        chipTotal += bet
        print(f"You've won\nNew chip total: {chipTotal}")
    elif(playerWon == "lost"):
        chipTotal -= bet
        print(f"You've lost\nNew chip total: {chipTotal}")
    elif(playerWon == "push"):
        print(f"You've pushed\nNew chip total: {chipTotal}")
    return int(chipTotal)

#main game function
def playGame(chipTotal, bet):
    #player turn
    playerHand = dealHand(2)
    printHandAndTotal(playerHand, "player")
    hit(playerHand, "player")

    #dealer turn
    dealerHand = dealHand(1)  
    hit(dealerHand, "dealer")
    printHandAndTotal(dealerHand, "dealer")

    #calculates if player won
    playerWon = determinePlayerWin(calHandTotal(playerHand), len(playerHand), calHandTotal(dealerHand))
    newChipTotal = payout(chipTotal, bet, playerWon)

    return newChipTotal

#determines if user wants to keep playing
def keepPlaying(chipTotal):
    if(chipTotal <= 0):
        print("You've lost all your chips...")
        return False

    if(input("Would you like to keep going? Type 'yes' or 'no'\n") == 'no'):
        if(chipTotal > 500):
            print(f"Congrats. You've managed to escape with {chipTotal - 500} extra chips!")
        elif(chipTotal == 500):
            print(f"You broke even... You sure you don't want to go again?")
        else:
            print(f"You lost {500 - chipTotal} chips. You were one hand away from making it all back...")
    else:
        clear()
        return True

#collects the bets from user with logic to check if it's a valid bet
def collectBet(chipTotal):
    bet = int(input("Enter bet: "))
    while((bet <= 0) or (bet > chipTotal) or (bet % 5 != 0)):
        print("Invalid Entry.")
        bet = int(input("Enter bet: "))
    clear()
    return bet    

#prints the rules of blackjack... didn't finish.
def printRules():
    print("==========RULES==========")
    print("Bets MUST be in increments of 5.")
    print("Standard Blackjack Rules Apply\n\n")

def main():
    chipTotal = 500
    while(True):
        print(f"Total chips: {chipTotal}")

        chipTotal = playGame(chipTotal, collectBet(chipTotal))
        if(not keepPlaying(chipTotal)):
            break

if __name__ == "__main__":
    clear()
    print(logo)
    printRules()
    main()

import os

clear = lambda: os.system('clear') #LINUX CLEAR
#clear = lambda: os.system('cls') #WINDOWS CLEAR

currentBidders = []

def getInformation():
    nameToAdd = input("What is your name?: ")
    bidToAdd = int(input("What is your bid?: $"))
    return [nameToAdd, bidToAdd]

def addToList(name, bid, currentBidders):
    currentBidders.append({
        "name": name,
        "bid": bid,
    })

def determineWinner(list):
    maxBid = 0
    winner = ""
    for person in list:
        if(person['bid'] > maxBid):
            maxBid = person['bid']
            winner = person['name']
    print(f"{winner} has won the auction with a top bid of ${maxBid}")

def main():
    while(True):
        clear()
        currentPerson = getInformation()
        addToList(currentPerson[0], currentPerson[1], currentBidders)    

        keepGoing = input("Are there any more bidders? Type 'yes' or 'no' ")

        if(keepGoing == 'no'):
            determineWinner(currentBidders)
            break
    
if __name__ == "__main__":
    main()
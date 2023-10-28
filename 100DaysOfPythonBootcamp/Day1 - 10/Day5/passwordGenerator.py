import random

random.seed(random.randint(0,10000)) #Still don't know if this generates a random seed... seems like it would

password_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                    'o', 'p', 'q', 'r', 's', 't', 'u', 
                    'v', 'w', 'x', 'y', 'z', 'A', 'B', 
                    'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                    'J', 'K', 'L', 'M', 'N', 'O', 'P', 
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
                    'X', 'Y', 'Z']

password_symbols = ['!', '@', '#', '$', '%', '^', '&', 
                    '*', '(', ')', '-', '_', '=', '+', 
                    '[', ']', '{', '}', '|', '\\', ';', 
                    ':', "'", '"', '<', '>', ',', '.', 
                    '?', '/', '`', '~']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']




sizeOfPassword = int(input("Enter how long you want the password: "))

while(sizeOfPassword <= 0):
    sizeOfPassword = int(input("Invalid option. Try again\nEnter how long you want the password: "))

#number of symbols in the password
numOfSymbols = int(input(f"Of those {sizeOfPassword} characters, how many will be symbols? "))

while(numOfSymbols > sizeOfPassword):
    numOfSymbols = int(input(f"Invalid option. Try again.\nOf those {sizeOfPassword} characters, how many will be symbols? "))

#number of numbers in the password
numOfNumbers = int(input(f"Of the remaining {sizeOfPassword - numOfSymbols} characters, how many would you like to be numbers? "))

while(numOfNumbers > (sizeOfPassword - numOfSymbols)):
    numOfNumbers = int(input(f"Invalid option. Try again.\nOf the remaining {sizeOfPassword - numOfSymbols} characters, how many would you like to be numbers? "))

#remaning amount are letters
numOfLetters = sizeOfPassword - (numOfNumbers + numOfSymbols)

password = ""

#Didn't know there was a built in shuffle for python :,(
    #0 = symbol
    #1 = letter
    #2 = number
    
while(len(password) != sizeOfPassword):
    temp = random.randint(0,2)

    if(temp == 0 and numOfSymbols > 0):
        password += password_symbols[random.randint(0, (len(password_symbols) - 1))]
        numOfSymbols -= 1    

    elif(temp == 1 and numOfLetters > 0):
        password += password_letters[random.randint(0, (len(password_letters) - 1))]
        numOfLetters -= 1    

    elif(temp == 2 and numOfNumbers > 0):
        password += numbers[random.randint(0, (len(numbers) - 1))]
        numOfNumbers -= 1

    else:
        continue

print(password)


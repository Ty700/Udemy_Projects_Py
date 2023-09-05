# For this exercise, you have to write a python program which prompts the user to enter three integers separated by ",".
# The user input is of the form: a,b,c, where a, b and c are numbers.

# Your program should calculate and display the result of the calculation:
# a + b - c

# Examples:
# 1. > Please enter three numbers: 10,11,10
# Output: 11

# 2. > Please enter three numbers: 7,5,-1 - NOTICE THAT IT ISN'T 11 but 13 SINCE WE SUBTRACT THE THIRD NUMBER TO THE SUM OF THE FIRST TWO
# Output: 13 

userInput = input("""Enter in three (3) integers seperated by a single ","\n""")

userInput = userInput.split(",")

#converting each value user inputs to an int and then adding it to total
for index, value in enumerate(userInput):
    
    #handles empty list
    if(userInput[index] == ""):
        print("0")
        break

    #converting current element in the list to an int
    userInput[index] = int(value)

    #Since index 0 is result, don't need to add it to itself - feel like I can do this another way
    if(index == 0):
        continue
    
    #need to subtract the last entered number to represent "- c" 
    if(index == 2):
        userInput[0] -= userInput[index]
    else:
        userInput[0] += userInput[index]

print(userInput[0])
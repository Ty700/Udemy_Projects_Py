#Adds only even numbers from 1 - <user int input>
#user input has to be <= 1000

upTo = int(input("Enter in an integer from 0 - 1000: "))

while(upTo > 1000):
    print("Try again.")
    upTo = int(input("Enter in an integer from 0 - 1000: "))

total = 0
for num in range(0, upTo + 1, 2):
    total += num

print(total)
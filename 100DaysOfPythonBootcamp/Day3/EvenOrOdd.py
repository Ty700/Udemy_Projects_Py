#Challenge 3.1 - Determining if a number is even/odd
#She wanted only ints, but I provided a case if the user enters a float as well

number = float(input("Enter in a number: "))

if(number % 2 == 0):
    print("Your number, {:.0f}, is even".format(number))
elif(number % 2 == 1):
    print("Your number, {:.0f}, is odd".format(number))
else:
    rounded_input = round(number)
    if(rounded_input % 2 == 0):
        print("Your number, {0}, is not an integer.\nThe closest integer to your number, {1}, is even".format(number, rounded_input))
    else:
        print("Your number, {0}, is not an integer.\nThe closest integer to your number, {1}, is odd".format(number, rounded_input))
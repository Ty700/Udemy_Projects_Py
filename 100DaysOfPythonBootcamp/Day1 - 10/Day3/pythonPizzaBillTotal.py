size = input("What size pizza would you like? S, M, L ")
add_pepperoni = input("Would you like to add pepperoni? Y or N ")
extra_cheese = input("Would you like to add extra cheese? Y or N ")

total = 0

#Small
if(size == "S" or size == "s"):
    total += 15
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        total += 2
    if(extra_cheese == "Y" or extra_cheese == "y"):
        total += 1
#Medium
elif(size == "M" or size == "m"):
    total += 20
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        total += 3
    if(extra_cheese == "Y" or extra_cheese == "y"):
        total += 1
#Large
else:
    total += 25
    if(add_pepperoni == "Y" or add_pepperoni == "y"):
        total += 3
    if(extra_cheese == "Y" or extra_cheese == "y"):
        total += 1

print("Your total is: ${0}".format(total))
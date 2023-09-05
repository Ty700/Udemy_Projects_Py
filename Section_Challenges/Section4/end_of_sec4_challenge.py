# Write a program to print a number of options, and allow the user to select an option from the list.

# The option should be numbered from 1 to 9 - although you can use less than 9 options if you want.

# Make sure there is at least 4 options.

#   Ex Output:
# Please choose your option from the list below:
#   1. Learn Python
#   2. Learn Java
#   3. Go Swimming
#   4. Have dinner
#   5. Go to bed
#   0. Exit
#
#   The program should continue looping, allowing the user to choose one of the options eahc time around
#   The loop should only terminate when the user chooses 0.
#   If the user makes a valid choice, the program should print a short message.
#   The message should include the number the user choose.
#   Extra: Modify program so that if the user makes an invalid choise it reprints the menu

#   Haven't learned funcs nor lists yet so I am not allowed to use them here :(

userChoice = None

while (userChoice != 0):
    userChoice = int(input("Please choose your option from the list below:\n\t1. Learn Python\n\t2. Learn Java\n\t3. Go Swimming\n\t4. Have dinner\n\t5. Go to bed\n\t0. Exit\n"))
    if(userChoice in range(0,6)):
        print("You choose {}".format(userChoice))
    else:
       print("Invalid choice. Try again")

#write a small program to ask for a name and an age
#When both values have been entered, check if the person is the right age to go on an 18-30 holiday 
#If they are, welcome them to the holdiay, otherwise print a (polite) message refusing them entry. 
#Our programs expect valid input. We'll see how to handle invalid numbers, later on in the course


name = input("Enter your name: ")
age = int(input("Hello {}, what is your age? " .format(name)))

if( 18 <= age <= 31):
    print("Welcome to the trip!")
elif(age <= 18):
    print("Sorry, you're too young. Come back in {} years".format(18 - age))
else:
    print("Sorry, you're {} years over the age limit.".format(age - 31))
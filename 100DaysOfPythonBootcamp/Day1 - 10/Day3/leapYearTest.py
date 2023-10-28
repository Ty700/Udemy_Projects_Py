#I remember doing this for cpp and I remember it being much more complicated than this.
#I overthought it lol

currentYear = int(input("Enter in a year: "))

if(currentYear % 4 != 0):
    print("{0} is not a leap year".format(currentYear))
elif(currentYear % 100 == 0 and currentYear % 400 != 0):
    print("{0} is not a leap year".format(currentYear))
else:
    print("{0} is a leap year".format(currentYear))
 
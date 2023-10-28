#Day2 Challenge of Dr. Angela Yu's 100 day of Python course on Udemy

total = float(input("What was the total bill? "))

tip_percentage = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))

total_people = int(input("How many people will split the bill? "))

total += total * (tip_percentage/100)

print("Each person should pay {:.2f}".format(total/total_people))
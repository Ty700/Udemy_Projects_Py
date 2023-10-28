#prompt she gave was confusing. It seems like it should give you the exact number of days, weeks, and months left.
#However, days, weeks, and months equal each other which is rather boring...
#Simple project but it's in the back of my mind to complete the actual number

#Ex output: Input = 56. You have 12410 days, 1768 weeks, and 408 months left. 
#The "and" makes it seem like its the exact amount of days, weeks, and months when in reality 1768 weeks = 408 months.
#Changed my output to clear it up

age = int(input("What is your current age? "))

total_months = (90 - age)*12
total_weeks = (90 - age)*52
total_days = (90-age)*365

print("You have {0} days, {1} weeks, and {2} months left until you're 90".format(total_days, total_weeks, total_months))
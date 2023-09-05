

height = float(input("Enter your height in feet:\nEx: 5'8 = 5.75\n"))

weight = float(input("Enter your weight in lbs: " ))

#converting height to m
height /= 3.281

#converting weight to kg
weight /= 2.205

bmi = (weight) / (pow(height,2))

print("Your bmi: {:.1f} ".format(bmi))
if(bmi <= 18.4):
    print("You're underweight according to the CDC")
elif (bmi <= 24.9):
    print("You're normal according to the CDC")
elif (bmi <= 39.9):
    print("You're overweight according to the CDC")
else:
    print("You're obese according to the CDC")
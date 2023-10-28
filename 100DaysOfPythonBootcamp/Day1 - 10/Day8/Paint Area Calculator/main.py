import math

test_h = int(input("Enter in the height in meters: "))
test_w = int(input("Enter in the width in meters: "))
coverage = 5 #m

print(f"You will need {math.ceil((test_h * test_w) / coverage)} cans")
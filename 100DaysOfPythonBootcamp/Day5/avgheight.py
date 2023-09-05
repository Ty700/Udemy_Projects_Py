# student_heights = [180, 124, 165, 173, 189, 169, 146] #is this in meters? Inches? who is 180 units?
#can't use sum() or len()

student_heights = input("Enter in a list of student heights: ").split()

for number in range(0, len(student_heights)):
    student_heights[number] = int(student_heights[number])

print (student_heights)

total_heights = 0
numStudents = 0

for height in student_heights:
    total_heights += height
    numStudents += 1

print("Avg height of the list: {0}".format(round(total_heights/numStudents)))


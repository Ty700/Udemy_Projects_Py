#Write code that examines a list of scores and display the highest value
#can't use max(student_score)


student_score = input("Enter a list of scores: ").split()

for score in range(0, len(student_score)):
    student_score[score] = int(student_score[score])

#last index of student_score = highest value
student_score.append(0)

for score in range(0, len(student_score)):
    if(student_score[score] > student_score[len(student_score) - 1]):
        # print("{0} > {1}".format(student_score[score], student_score[len(student_score) - 1]))
        student_score[len(student_score) - 1] = student_score[score]

print(str(student_score[len(student_score) - 1]))
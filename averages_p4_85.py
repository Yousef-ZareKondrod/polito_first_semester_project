count_of_exams = int(input('Enter the count of exams for each students:'))

j = 'Y'
while j == 'Y':
    exam_grades = []
    sum = 0
    for i in range(count_of_exams):
        grade = float(input('Enter the grade:'))
        exam_grades.append(grade)
        sum += grade

    average = sum / count_of_exams
    print(f'the grades are:{exam_grades}')
    print(f'the {average = }')
    j = input('are there any other students(Y to continue N to end):')
    if j in ['y', 'n']:
        j = j.upper()

print('the program has finished')

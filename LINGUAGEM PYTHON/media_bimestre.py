first_grade = float(input('First grade: '))
second_grade = float(input('Second grade: '))
sum_grades = first_grade + second_grade
average_grade = sum_grades/2


while True:
    if average_grade > 10:
        print('The average grade cannot be higher than 10')
    elif average_grade >=6:
        print(f'Approved! Your grade is {average_grade}')
    else:
        print(f'Reproved! Your average grade is {average_grade}')
    break


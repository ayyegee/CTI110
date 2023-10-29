# This program takes a number grade , determines average and displays letter grade for average.
# October 28th 2023
# CTI-110 P3HW1 - Debugging
# Andrew Garcia

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)
print ('------------Results------------')
print(f'Lowest Grade: {low}')
print(f'Highest Grade: {high}')
print(f'Sum of Grades: {total}')
print(f'Average: {avg}')
print('---------------------------------------')



if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')
 
else:
    print('Your grade is: F')






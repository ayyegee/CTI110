#CTI-110
#P2HW2- List
#Andrew Garcia
#October 09, 2023
 
module_grades=[]

for i in range(6):
    module= i+1
    grade=float(input(f'Enter grade for Module {module}: '))
    module_grades.append(grade)

lowest_grade=min(module_grades)
highest_grade=max(module_grades)
sum_grades=sum(module_grades)
average = sum_grades / len(module_grades)
print('')

print('------------Results------------')
print(f'Lowest Grade:   {lowest_grade:.2f}')
print(f'Highest Grade:  {highest_grade:.2f}')
print(f'Sum of Gardes:  {sum_grades:.2f}')
print(f'Average:        {average:.2f}')
print('-----------------------------------------')


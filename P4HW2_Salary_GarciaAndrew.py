# CTI-110
# P4HW2 - Salary Calculator
# Andrew Garcia
# 24 Nov 2023

total_overtime = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    
    if employee_name.lower() == 'done':
        break
    
    num_employees += 1
    
    hours_worked = float(input(f"How many hours did {employee_name} work?: "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate?: "))


    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

    total_regular_pay += regular_pay
    total_overtime += overtime_pay
    total_gross_pay += gross_pay

    print(' ' )
    print('Employee Name: ', employee_name)
    print(' ')
    print(f'Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay')
    print('------------------------------------------------------------------------')
    print(f'{hours_worked}          {pay_rate}        {overtime_hours}       {overtime_pay}           ${regular_pay}       ${gross_pay}')
    print(' ')
    print(' ')

print('\n----------------- Totals -----------------')
print('Total number of employees entered: {}'.format(num_employees))
print('Total amount paid for overtime: ${:.2f}'.format(total_overtime))
print('Total amount paid for regular hours: ${:.2f}'.format(total_regular_pay))
print('Total amount paid in gross: ${:.2f}'.format(total_gross_pay))

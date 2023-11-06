#CTI-110
#P3HW2 - Salary
#Andrew Garcia
#29 October 2023
#
    
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print('------------------------------------------')
print("Employee Name: ", employee_name)
print('')
  
regular_hours = 0
overtime_hours = 0
    
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
        
else:
    regular_hours = hours_worked
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)

gross_pay = regular_pay + overtime_pay
  
print(f'Hours Worked  Pay Rate   OverTime   OverTime Pay   RegHour Pay     Gross Pay    ')
print('--------------------------------------------------------------------------------')
print(f"{hours_worked}          {pay_rate}        {overtime_hours}        {overtime_pay}        ${regular_pay}           ${gross_pay}")








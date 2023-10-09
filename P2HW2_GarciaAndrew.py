# This program calculates and displays travel expenses
# October 9th 2023
# CTI-110 P2HW2 - Travel
# Andrew Garcia

print('This program calculates and displays travel expenses ')
print('')
budget=int(input("Enter Budget:? "))
print('')
destination=input('Enter your travel destination: ')
print('')
gas=int(input("How much do you think you will spend on gas? "))
print('')
hotel=int(input("Approximately, how much will you need for accommodation/hotel? "))
print('')
food=int(input("Last, how much do you need for food? "))
print('')
print('------------Travel Expenses------------')
max_width = max(len('Location:'), len('Initial Budget:'), len('Fuel:'), len('Accommodation:'), len('Food:'))

print(f'Location:       {destination:<{max_width}}')
print(f'Initial Budget: ${budget:.2f}')
print(f'Fuel:           ${gas:.2f}')
print(f'Accommodation:  ${hotel:.2f}')
print(f'Food:           ${food:.2f}')
print('---------------------------------------')
print(' ')
print(f'Remaining Balance: ${budget-gas-hotel-food}')

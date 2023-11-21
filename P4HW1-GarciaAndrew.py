# CTI-110
# P4HW1 - List
# Andrew Garcia
# November 20, 2023

score_list = []

num_of_scores = int(input("How many scores do you want to enter?: "))
print(' ')

for i in range(num_of_scores):
    valid_score = False
    
    while not valid_score:
        try:
            module = i + 1
            score = float(input(f'Enter score #{module}: '))
            
            if 0 <= score <= 100:
                valid_score = True
                score_list.append(score)
            else:
                print(" ")
                print("INVALID Score entered!!!!")
                print("Please enter a score between 0 and 100.")
        except ValueError:
                print(" ")
                print("INVALID Score entered!!!!")
                print("Please enter a score between 0 and 100.")
 
lowest_grade = min(score_list)
modified_score_list = score_list.copy()
modified_score_list.remove(lowest_grade)
highest_grade = max(modified_score_list)
sum_grades = sum(modified_score_list)
average = sum_grades / len(modified_score_list)

print(' ')
print('------------Results------------')
print(f'Lowest Score  : {lowest_grade:.2f}')
print(f'Modified List : {modified_score_list}')
print(f'Scores Average: {average:.2f}')

if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
else:
    grade = "F"

print(f'Grade         : {grade}')
print('---------------------------------')

#Randon Numbers Math Quiz
#04December2023
#CTI P5HW- Math Quiz
# Andrew Garcia
#
import random

def generate_numbers():
    """Generate two random numbers for the quiz."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def math_quiz():
    """Implement the math quiz."""
    print("Welcome to the Math Quiz!")
    print("")
    print("")

    while True:
        print("MAIN MENU")
        print("---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print("")

        choice = int(input("Please choose one of the menu options: "))

        if choice == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break

        num1, num2 = generate_numbers()
        num_guesses = 0
        correct_answer = 0

        if choice == 1:
            correct_answer = num1 + num2
        elif choice == 2:
            correct_answer = num1 - num2
        else:
            print("Invalid choice. Please choose one of the menu options:")
            print("")
            continue

        while True:
            print(f"\n  {num1}\n+ {num2}" if choice == 1 else f"\n  {num1}\n- {num2}")

            user_answer = int(input("Enter your answer: "))
            num_guesses += 1

            if user_answer == correct_answer:
                print(f"Congratulations! Your answer is correct.")
                print(f"It took you {num_guesses} guesses.")
                print("")
                break
            else:
                if user_answer < correct_answer:
                    print("Sorry, guess is too low.")
                else:
                    print("Sorry, guess is too high.")

if __name__ == "__main__":
    math_quiz()

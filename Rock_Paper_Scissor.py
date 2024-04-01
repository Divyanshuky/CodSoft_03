import random

user_score = 0
computer_score = 0

while True:
    print("""\nRock, Paper, Scissors Game
          1. Rock
          2. Paper
          3. Scissors
          4. Quit""")
    
    choice = input("Enter your choice (1/2/3/4): ").lower()
    
    if choice == '4':
        print("Thank you for playing. Final scores:")
        print("Your score:", user_score)
        print("Computer's score:", computer_score)
        break
    
    elif choice not in ('1', '2', '3'):
        print("Invalid choice. Please try again.")
        continue
    
    choice_data = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    user_choice = choice_data[choice]
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print("\nYour choice:", user_choice)
    print("Computer's choice:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice== 'scissors' and computer_choice == 'paper') or \
         (user_choice== 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    
    play_choice = input("Do you want to play again? (yes/no): ").lower()
    if play_choice != 'yes':
        print("Thank you for playing. Final scores:")
        print("Your score:", user_score)
        print("Computer's score:", computer_score)
        break

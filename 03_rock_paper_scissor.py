import random

user_score = 0
computer_score = 0

print("Type 'rock', 'paper', or 'scissors' to play the game. Type 'exit' to quit the game\n")

while True:
    print("Your Turn: ")
    user_choice = input("Enter your choice: ")

    computer_choice = random.choice(['rock', 'paper', 'scissor'])

    print('Computer chose: ', computer_choice)

    if user_choice == 'exit':
        print("The game ended")
        print('Final Score = YOUR SCORE: ', user_score, ' COMPUTER SCORE: ', computer_score)
        break

    if user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissor':
        print("Invalid input. Please enter rock, paper or scissor.")
        print("--------------------------------------------------------------------------------")
        continue

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
        print("No one got the point")

    elif (user_choice == 'rock' and computer_choice == 'scissor') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissor' and computer_choice == 'paper'):
        print(f"You win! 10 point added")
        user_score += 10
        
    else:
        print(f"Computer won! 10 point added")
        computer_score += 10

    print('Current Score = YOUR SCORE: ', user_score, ' COMPUTER SCORE: ', computer_score)
    print("--------------------------------------------------------------------------------")
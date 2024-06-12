import random

# define a constants for rock, paper, and scissors
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

# Compute the computer choice
def computer_choice():
    return random.choice([ROCK, PAPER, SCISSORS])

# Given two choices, determine the winner by returning an integer
# 0 if it's a tie
# 1 if the first choice wins
# -1 if the second choice wins
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 0
    if choice1 == ROCK:
        return 1 if choice2 == SCISSORS else -1
    if choice1 == PAPER:
        return 1 if choice2 == ROCK else -1
    if choice1 == SCISSORS:
        return 1 if choice2 == PAPER else -1
    
# Given an integer, return the message
# if 0, return "It's a tie!"
# if 1, return "You win!"
# if -1, return "You lose!"
def get_message(result):
    if result == 0:
        return "It's a tie!"
    if result == 1:
        return "You win!"
    if result == -1:
        return "You lose!"
    
# Given a choice, convert it to lower case then check if it is valid
def is_valid_choice(choice):
    return choice.lower() in [ROCK, PAPER, SCISSORS]

# Prompt the user for a choice
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ")
    while not is_valid_choice(choice):
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ")
    return choice.lower()


# Main function
# Loop until the user wants to quit
# Keep track of the number of wins, losses, and ties
# Print the number of wins, losses, and ties
# Each round the user can choose to quit or play again
# If the user chooses to play again, continue the loop
# If the user chooses to quit, print the number of wins, losses, and ties
# and exit the loop
def main():
    wins = 0
    losses = 0
    ties = 0
    while True:
        user_choice = get_user_choice()
        comp_choice = computer_choice()
        print(f"Computer choice: {comp_choice}")
        result = determine_winner(user_choice, comp_choice)
        print(get_message(result))
        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        else:
            ties += 1
        print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    print(f"Final Wins: {wins}, Losses: {losses}, Ties: {ties}")

main()



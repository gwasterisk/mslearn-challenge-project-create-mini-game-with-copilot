import random

# define constants for rock, paper, and scissors
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

# define constants for the result
TIE = 0
WIN = 1
LOSS = -1

# Compute the computer choice
def computer_choice():
    return random.choice([ROCK, PAPER, SCISSORS])

# Given two choices, determine the winner by returning an integer
# TIE if it's a tie
# WIN if the first choice wins
# LOSS if the second choice wins
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return TIE
    if choice1 == ROCK:
        return WIN if choice2 == SCISSORS else LOSS
    if choice1 == PAPER:
        return WIN if choice2 == ROCK else LOSS
    if choice1 == SCISSORS:
        return WIN if choice2 == PAPER else LOSS
    
# Given an integer, return the message
# if TIE, return "It's a tie!"
# if WIN, return "You win!"
# if LOSS, return "You lose!"
def get_message(result):
    if result == TIE:
        return "It's a tie!"
    if result == WIN:
        return "You win!"
    if result == LOSS:
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
        if result == WIN:
            wins += 1
        elif result == LOSS:
            losses += 1
        elif result == TIE:
            ties += 1
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
        while True:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "no":
                print(f"Final Wins: {wins}, Losses: {losses}, Ties: {ties}")
                return
            elif play_again.lower() == "yes":
                break
            else:
                print("Invalid choice. Please try again.")
                continue

main()



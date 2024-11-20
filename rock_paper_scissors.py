# Rock, Paper, Scissors Game
# By Michael Morales

import random

# ASCII art for the game options
ascii_art = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''',
    "paper": '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
}

# Function to get the user's choice
def get_user_choice():
    """
    Prompts the user to choose rock, paper, or scissors.
    """
    print("Choose your weapon!")
    print("Type 'rock', 'paper', or 'scissors'")
    while True:
        choice = input("Your choice: ").lower()
        if choice in ascii_art:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the game's rules.
    """
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Congratulations, you win!"
    else:
        return "Sorry, you lose."

def main():
    """
    Main function to run the Rock, Paper, Scissors game.
    """
    print("Welcome to Rock, Paper, Scissors!")
    print("By Michael Morales\n")

    # Get user and computer choices
    user_choice = get_user_choice()
    computer_choice = random.choice(list(ascii_art.keys()))

    # Display the choices
    print("\nYou chose:")
    print(ascii_art[user_choice])
    print("The computer chose:")
    print(ascii_art[computer_choice])

    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print("\n" + result)

if __name__ == "__main__":
    main()

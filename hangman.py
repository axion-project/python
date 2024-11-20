# Hangman Game
# By Michael Morales

import random

def choose_word():
    """
    Selects a random word from a list of words.
    """
    words = ["python", "java", "javascript", "c++", "ruby"]
    return random.choice(words)

def initialize_game(word):
    """
    Initializes the game state.
    """
    word_length = len(word)
    guessed_letters = []
    display_word = ["_" for _ in range(word_length)]
    return guessed_letters, display_word

def display_game_state(display_word):
    """
    Prints the current state of the game.
    """
    print("Current word:", " ".join(display_word))

def get_user_guess():
    """
    Prompts the user for a letter guess.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        else:
            return guess

def update_game_state(word, guessed_letters, display_word, guess):
    """
    Updates the game state based on the user's guess.
    """
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        print("Incorrect guess.")

def check_win_condition(display_word):
    """
    Checks if the player has won the game.
    """
    return "_" not in display_word

def main():
    """
    Main game loop.
    """
    word = choose_word()
    guessed_letters, display_word = initialize_game(word)
    max_attempts = 6
    attempts_remaining = max_attempts

    while attempts_remaining > 0:
        display_game_state(display_word)
        guess = get_user_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        update_game_state(word, guessed_letters, display_word, guess)

        if check_win_condition(display_word):
            print(f"Congratulations, you win! The word was '{word}'.")
            break

        attempts_remaining -= 1
        print(f"Attempts remaining: {attempts_remaining}")

    if attempts_remaining == 0:
        print(f"You lose. The word was '{word}'.")

if __name__ == "__main__":
    main()

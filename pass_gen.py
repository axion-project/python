# Password Generator
# By Michael Morales

import random
import string

def generate_password(length=12):
    """
    Generates a secure random password of the specified length.
    
    Parameters:
        length (int): The length of the generated password. Default is 12 characters.

    Returns:
        str: A randomly generated password.
    """
    # Define the character pool for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    """
    Main function to run the password generator.
    """
    print("Welcome to the Password Generator!")
    
    # Ask the user for the desired password length
    try:
        length = int(input("Enter the length of the password (default is 12): ") or 12)
    except ValueError:
        print("Invalid input! Using default length of 12.")
        length = 12
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Your randomly generated password is: {password}")

# Run the password generator
if __name__ == "__main__":
    main()

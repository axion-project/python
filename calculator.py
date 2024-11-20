# Fun Interactive Calculator
# By Michael Morales

def show_banner():
    """
    Displays a fun banner for the calculator.
    """
    print("""
    **********************************************
    *    Welcome to Michael's Magic Calculator!   *
    *    Where math meets fun and imagination!    *
    **********************************************
    """)

def get_user_choice():
    """
    Displays the menu and gets the user's choice of operation.
    """
    print("\nWhat would you like to do today?")
    print("""
    1. Add (+)
    2. Subtract (-)
    3. Multiply (*)
    4. Divide (/)
    5. Power (^)
    6. Remainder (%)
    7. Exit (Goodbye!)
    """)
    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            if choice in range(1, 8):
                return choice
            else:
                print("Please enter a valid option (1-7).")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 7.")

def perform_operation(choice, num1, num2):
    """
    Performs the operation based on the user's choice.
    """
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Oops! Division by zero is not allowed."
    elif choice == 5:
        return num1 ** num2
    elif choice == 6:
        if num2 != 0:
            return num1 % num2
        else:
            return "Oops! Division by zero is not allowed."

def main():
    """
    Main function to drive the interactive calculator.
    """
    show_banner()
    while True:
        # Get user's choice of operation
        choice = get_user_choice()

        # Exit condition
        if choice == 7:
            print("\nThanks for using Michael's Magic Calculator! ✨")
            print("Come back soon for more math magic!")
            break

        # Prompt user for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        # Perform the operation
        result = perform_operation(choice, num1, num2)

        # Display the result
        print(f"\n🎉 Result: {result} 🎉\n")
        print("Math is fun, isn't it? Let's calculate more!\n")

if __name__ == "__main__":
    main()

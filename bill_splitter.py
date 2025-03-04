def split_bill():
    # Welcome message
    print("Welcome to the Bill Splitter!")

    # Get user inputs
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = float(input("What percentage tip would you like to give? (e.g., 20 for 20%) "))
    num_people = int(input("How many people are splitting the bill? "))

    # Validate input
    if num_people <= 0:
        print("The number of people must be greater than zero.")
        return

    # Calculate total amount including tip
    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount

    # Calculate amount per person
    amount_per_person = total_amount / num_people

    # Print result
    print(f"Each person pays: ${amount_per_person:.2f}")

# Run the function
split_bill()

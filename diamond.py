rows = int(input("Enter Diamond Pattern Rows = "))
print("Diamond Star Pattern")

# Top half of the diamond
for i in range(1, rows + 1):
    # Printing spaces
    for j in range(rows - i):
        print(" ", end="")
    # Printing stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Bottom half of the diamond
for i in range(rows - 1, 0, -1):
    # Printing spaces
    for j in range(rows - i):
        print(" ", end="")
    # Printing stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()
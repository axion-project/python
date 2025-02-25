# Define the loop control variable
isAlive = True

# Define the functions
def eat():
    print("Eating...")

def sleep():
    print("Sleeping...")

def code():
    print("Coding...")

# Main function
def programmersLife():
    while isAlive:
        eat()
        sleep()
        code()

# Entry point
if __name__ == "__main__":
    programmersLife()
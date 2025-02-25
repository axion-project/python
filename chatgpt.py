def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes():
    count = 0
    # Generate every 3rd number from 1 to 1000
    for number in range(1, 1001, 3):
        if is_prime(number):
            count += 1
    print(f"Number of prime numbers among every 3rd number from 1 to 1000: {count}")

# Ensure that the function is being called correctly
if __name__ == "__main__":
    count_primes()
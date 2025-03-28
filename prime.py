def is_prime(n):
  """
  Checks if a number is prime.

  Args:
    n: The number to check.

  Returns:
    True if n is prime, False otherwise.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

prime_numbers = []
for i in range(2, 1001):
  if is_prime(i):
    prime_numbers.append(i)

print(prime_numbers)

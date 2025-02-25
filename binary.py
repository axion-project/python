def text_to_binary(text):
  """Converts a string to its binary representation.

  Args:
    text: The input string.

  Returns:
    A string of binary representations of each character in the input string, 
    separated by spaces.
  """
  binary_str = ""
  for char in text:
    binary_str += bin(ord(char))[2:] + " " 
  return binary_str

# Get the binary representation of "Michael"
binary_michael = text_to_binary("Michael")

# Print the result
print(f"Binary representation of 'Michael': {binary_michael}") 

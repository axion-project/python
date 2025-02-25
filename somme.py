def somme1(n):
    """Sum of digits using string conversion and list comprehension."""
    m = str(abs(n))
    return sum([int(c) for c in m])

def somme2(n):
    """Sum of digits using `itertools.takewhile`."""
    from itertools import takewhile
    m = str(n)[::-1]  # Reverse the number string
    return sum(map(int, takewhile(lambda c: c not in ["-"], m)))

def somme3(n):
    """Sum of digits using a loop and division."""
    n = abs(n)  # Ensure n is positive
    s = 0
    while n:
        n, r = divmod(n, 10)  # Divide and get remainder
        s += r
    return s

def somme4(n):
    """Sum of digits using recursion."""
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + somme4(n // 10)

def somme5(n):
    """Preferred implementation: Sum of digits using `map` and `str`."""
    n = abs(n)  # Convert to positive
    return sum(map(int, str(n)))

# Test cases
for n in [1024, -9875]:
    print(f"somme1({n}) = {somme1(n)}")
    print(f"somme2({n}) = {somme2(n)}")
    print(f"somme3({n}) = {somme3(n)}")
    print(f"somme4({n}) = {somme4(n)}")
    print(f"somme5({n}) = {somme5(n)}")
    print()
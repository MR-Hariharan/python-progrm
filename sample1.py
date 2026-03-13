a = 5
b = 10

# Swap using temporary variable
a = b - a
b = b - a
a = a + b

print(f"a = {a}, b = {b}")
# Swapping numbers without using a temporary variable
a = 5
b = 10

a = a + b
b = a - b
a = a - b

print("After swapping, a =", a)
print("After swapping, b =", b)
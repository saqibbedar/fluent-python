# Arithmetic Operators
a = 10
b = 3

print(a + b)   # 13  → Addition
print(a - b)   # 7   → Subtraction
print(a * b)   # 30  → Multiplication
print(a / b)   # 3.3333 → Division (always returns float)
print(a // b)  # 3   → Floor division (removes decimal)
print(a % b)   # 1   → Modulus (remainder)
print(a ** b)  # 1000 → Exponent (10 to the power of 3)


# Comparison Operators
x = 10
y = 20

print(x == y)   # False → Equal to
print(x != y)   # True  → Not equal to
print(x > y)    # False → Greater than
print(x < y)    # True  → Less than
print(x >= 10)  # True  → Greater than or equal
print(x <= 9)   # False → Less than or equal

# Assignment Operators
score = 100

score += 10   # same as score = score + 10  → 110
score -= 5    # same as score = score - 5   → 105
score *= 2    # same as score = score * 2   → 210
score //= 3   # same as score = score // 3  → 70


# Example usage
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity
tax = subtotal * 0.1
total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax (10%): {tax}")
print(f"Total: {total}")


# Logical Operators
age = 20
has_id = True

print(age >= 18 and has_id)   # True  → both are true
print(age < 18 or has_id)     # True  → one is true
print(not has_id)             # False → flips True to False


# Identity Operators
x = None

print(x is None)      # True
print(x is not None)  # False


# Membership Operators
name = "Alice"
fruits = ["apple", "banana", "mango"]

print("A" in name)           # True
print("mango" in fruits)     # True
print("grape" not in fruits) # True
n = 42

# n:5 define no. of spaces 
print(f"{n:5}")         # Output:    42
print(f"{n:05}")         # Output: 00042    zero-padded
print(f"{n:+5}")         # Output:   +42    Always show plus sign
print(f"{n:+5}")         # Output:   +42    Always show plus sign

n= 1000000
print(f"{n:,}")         # Output: 1,000,000     thousands separator
print(f"{n:_}")         # Output: 1_000_000     thousands separator

print(f"{-42:+}")       # Output: -42
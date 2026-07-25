age = 18

# If/Else
if age >= 18:
    print("You are an adult")
else:
    print("You are minor")

score = 75
# If/Elif/Else
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# practical example

balance = 50000.00
withdraw = float(input("Amount to withdraw: "))

if balance <= 0:
    print("Insufficient Balance")
elif withdraw > balance:
    print("Insufficient funds")
else:
    if withdraw < 500.0:
        print("Withdraw balance is too small")
    else:
        balance -= withdraw
        print(f"Withdrawn! Remaining balance: {balance}")
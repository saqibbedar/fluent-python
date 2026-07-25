# age = input("What's your age?")
# print(age+1)        # Error: can't add string and number

# input() function always return string so we need to 

age = int(input("What's your age?"))

print(f"You will be {age+1} next year!")
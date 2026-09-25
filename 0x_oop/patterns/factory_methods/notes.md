# Pattern 1. Function returns the INSTANCE (Most Common)

When a function returns an instance, you can chain methods or attributes right onto the function call, or capture it in a variable.

```py
# 1. Setup a factory function that creates and returns a Student instance
def spawn_student(name: str) -> Student:
    new_student = Student(name=name, grade=10)
    return new_student  # The instance moves out of the function scope

# 2. How to call attributes/methods immediately after the function is over:

# Style 1: Catching it in a variable (Cleanest)
student_instance = spawn_student("Saqib")
print(student_instance.name)  # Access attribute -> "Saqib"
student_instance.enroll("AI") # Call method

# Style 2: Inline Chaining (No variable assignment)
# The function executes, returns the object, and you access the attribute instantly.
student_name = spawn_student("Bedar").name 
print(student_name) # -> "Bedar"

# WARNING: If you chain a method that returns None (like your enroll or upgrade_grade):
result = spawn_student("Saqib").upgrade_grade() 
print(result) # -> This prints None! (Because upgrade_grade() modified the object but returned nothing)
```

# Pattern B: Function returns the CLASS BLUEPRINT itself (Metaprogramming)

In Python, you can actually pass around the class definition itself before it is even instantiated.

```py
# 1. A function that decides WHICH class blueprint to return
def get_blueprint(is_premium_student: bool):
    if is_premium_student:
        return Student  # Returning the CLASS object, NOT an instance (no parenthesis!)
    return None

# 2. How to use it when the function call is over:
student_class_blueprint = get_blueprint(is_premium_student=True)

# Now you use that variable EXACTLY like you would use the original 'Student' keyword to instantiate:
my_instance = student_class_blueprint(name="Saqib Bedar", grade=12)
print(my_instance.name) # -> "Saqib Bedar"

# Inline Chaining Example:
# Call function -> gets blueprint -> immediately instantiate with () -> access attribute
name = get_blueprint(is_premium_student=True)(name="Direct Call", grade=1).name
print(name) # -> "Direct Call"
```
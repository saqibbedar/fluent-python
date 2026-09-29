def floor_division(a: int, b: int) -> int:

    breakpoint()        # Execution pauses here
    
    if b == 0:
        raise ZeroDivisionError("Cannot divide a number by zero.")
    return a // b

try:
    print(floor_division(10,0))
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("--- Task completed ---")
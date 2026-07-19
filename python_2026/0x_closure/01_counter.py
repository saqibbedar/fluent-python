def make_counter():
    count = 0       # enclosed variable

    def counter():
        nonlocal count       # Declares intent to modify outer variable
        count += 1
        return count
    
    return counter


my_counter = make_counter()

print(my_counter())       # 1
print(my_counter())       # 2


# Inspecting a Closure
# Python stores the captured variables (called "free variables") in a special hidden attribute called __closure__.

# Inspecting the 'my_counter'
print(my_counter.__closure__) 
# Output: (<cell at 0x000001903DFFB2B0: int object at 0x00007FFE02A68498>,)

print(my_counter.__closure__[0].cell_contents) 
# Output: 2
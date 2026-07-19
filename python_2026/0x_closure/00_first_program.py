"""
A nested function that retains access to variables from its enclosing (outer) scope even after the outer function has finished executing.

inner function

+----------------+
| code pointer   |
| closure ------>| x = 10
+----------------+
"""

def outer():
    x = 10

    def inner():
        return x
    
    return inner

f = outer()

print(f())

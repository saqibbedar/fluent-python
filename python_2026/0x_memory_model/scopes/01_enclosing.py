# Enclosing (E): It occurs in when writing functions or more specifically in closures. When inner function uses outer function's variables hence those variables scope is called enclosed.

def outer():
    x = "outer"
    def inner():
        print(x)

    inner()

print(outer())
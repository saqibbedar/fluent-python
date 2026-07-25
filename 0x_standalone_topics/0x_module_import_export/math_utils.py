def add(x: int, y: int):
    return x + y

def sub(x: int, y: int):
    return x - y

def mul(x: int, y: int):
    return x * y

def div(x: int, y: int):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x / y

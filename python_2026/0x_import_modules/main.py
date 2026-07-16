import math_utils as mu

x: int = 10
y: int = 0


print(mu.add(x, y))
print(mu.sub(x, y))
print(mu.mul(x, y))

try:
    print(mu.div(x, y))
except ZeroDivisionError as error:
    print(error)
finally:
    pass
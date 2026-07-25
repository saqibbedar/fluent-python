def make_multiplier(factor):
    # enclosing scope variable: factor
    def multiplier(number):
        return number * factor  # inner function ref 'factor'
    
    return multiplier       # return inner function


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))            # 10
print(triple(5))            # 15
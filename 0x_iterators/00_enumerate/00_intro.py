"""
Def: enumerate() is one of Python's most useful built-in functions. It lets you loop over an iterable while automatically keeping track of an index.

- Function signature: enumerate(iterable, start=0)

- Parameters:

    1. iterate (required):

        Any object that can be iterated over:

        list
        tuple
        string
        set
        dict
        generator
        file object
        range

        Examples:

            enumerate([10, 20, 30])
            enumerate("hello")
            enumerate(range(5))

    2. start (optional):

        default -> start=0

        Example:

            for i, item in enumerate(["a", "b", "c"], start=1):
                print(i, item)

            Output:

                1 a
                2 b
                3 c

- Negative values are allowed

    for i, item in enumerate(["a", "b", "c"], start=-3):
        print(i, item)
    
    Output:
        
        -3 a
        -2 b
        -1 c

- Return value: It returns an enumerate object.

    nums = [10, 20, 30]

    e = enumerate(nums)

    print(e)

    Output: <enumerate object at 0x...>

    Note: It does not immediately create all index-value pairs. It is a lazy iterator.

- Internally implemented like this:

    def custom_enumerate(iterable, start=0)
        n = start

        for item in iterable:
            yield (n, item)
            n += 1
    
    list(custom_enumerate(["a", "b", "c"]))

    output: [(0, 'a'), (1, 'b'), (2, 'c')]      # it return array of tuple so 
    
    for tup in enumerate(iterable):
        print(tup)

    Output: (index, value)
"""

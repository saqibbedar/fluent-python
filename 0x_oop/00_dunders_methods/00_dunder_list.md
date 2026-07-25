# Dunders AKA Magic Methods

Dunder methods (short for `Double Underscore` methods), also called `magic methods`, are special built-in functions used to implement `operator overloading` and customize core object behavior. They are automatically invoked by `Python` under the hood when specific operations are performed (e.g., calling `len(obj)` triggers `obj.__len__()`).

## List

### Object Lifecycle & Creation

- **`__new__(cls, ...)`:** Handles actual object creation; runs before `__init__`.

- **`__init__(self, ...)`:** Handles object initialization (the constructor).

- **`__del__(self)`:** Handles object destruction when instances are garbage collected.

### String & Representation

- **`__str__(self)`:** Defines a human-readable string representation used by `print()` and `str()`.

- **`__repr__(self)`:** Defines an unambiguous string representation for debugging and `repr()`.

- **`__format__(self, format_spec)`:** Customizes behavior for `format()` and f-strings.

- **`__bytes__(self)`:** Defines the output when converted via `bytes()`.

### Comparison Operators

- **`__eq__(self, other)`:** Implements the equality operator (`==`).

- **`__ne__(self, other)`:** Implements inequality (`!=`).

- **`__lt__(self, other)`:** Implements less than (`<`).

- **`__le__(self, other)`:** Implements less than or equal to (`<=`).
- **`__gt__(self, other)`:** Implements greater than (`>`).

- **`__ge__(self, other)`:** Implements greater than or equal to (`>=`).

- **`__hash__(self)`:** Generates an integer hash used for dictionary keys and sets.

### Mathematical & Arithmetic Operations

- **`__add__(self, other)`:** Implements addition (`+`).

- **`__sub__(self, other)`:** Implements subtraction (`-`).

- **`__mul__(self, other)`:** Implements multiplication (`*`).

- **`__truediv__(self, other)`:** Implements true division (`/`).

- **`__floordiv__(self, other)`:** Implements floor division (`//`).

- **`__mod__(self, other)`:** Implements modulo (`%`).

- **`__pow__(self, other)`:** Implements exponentiation (`**`).

- **`__matmul__(self, other)`:** Implements matrix multiplication (`@`).

(Note: Adding an `r` prefix like `__radd__` implements the right-hand version for mixed-type operations, and an `i` prefix like `__iadd__` implements in-place augmented assignments like `+=`).

### Type Conversion & Type Emulation

- **`__bool__(self)`:** Evaluates truthiness within `if` conditions or `bool()`.

- **`__int__(self)`:** Converts an object to an integer using `int()`.

- **`__float__(self)`:** Converts an object to a float using `float()`.

- **`__index__(self)`:** Losslessly converts an object to an integer for slicing and indexing.

### Container & Sequence Emulation

- **`__len__(self)`:** Returns collection length via `len()`.

- **`__getitem__(self, key)`:** Accesses elements using index brackets (`obj[key]`).

- **`__setitem__(self, key, value)`:** Assigns a value to an index (`obj[key] = value`).

- **`__delitem__(self, key)`:** Deletes an item at an index (`del obj[key]`).

- **`__contains__(self, item)`:** Checks membership using the `in` operator.

### Iterators & Generators

- **`__iter__(self)`:** Returns an iterator object when passed to `iter()` or used in a `for` loop.

- **`__next__(self)`:** Fetches the next item from an iterator; raises `StopIteration` at the end.

- **`__reversed__(self)`:** Defines behavior for the built-in `reversed()` function.

### Attribute Access & Management

- **`__getattr__(self, name)`:** Invoked as a fallback when an attribute isn't found normally.

- **`__getattribute__(self, name)`:** Intercepts all attribute access attempts unconditionally.

- **`__setattr__(self, name, value)`:** Intercepts setting or updating any attribute.

- **`__delattr__(self, name)`:** Intercepts deleting any attribute.

- **`__dir__(self)`:** Lists all accessible attributes when calling `dir()`.

### Context Managers

- **`__enter__(self)`:** Sets up a runtime context block using the `with` statement.

- **`__exit__(self, exc_type, exc_val, exc_tb)`:** Tears down the context and handles exceptions when exiting a `with` block.

### Callable Objects

- **`__call__(self, ...)`:** Allows an object instance to be called like a function (e.g., `obj()`).

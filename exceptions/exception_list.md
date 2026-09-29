# Most Used Built-in Python Exceptions

### 1. Value and Type Errors

* `ValueError`: Raised when a function receives an argument with the right type but an inappropriate value (e.g., `int("xyz")`).
* `TypeError`: Raised when an operation or function is applied to an object of an inappropriate type (e.g., `len(5)`).

### 2. Data Structure Errors

* `IndexError`: Raised when a sequence subscript (like a list index) is out of range.
* `KeyError`: Raised when a mapping (dictionary) key is not found in the set of existing keys.
* `AttributeError`: Raised when an attribute reference or assignment fails (e.g., trying to call a string method on an integer).

### 3. Math and Calculation Errors

* `ZeroDivisionError`: Raised when the second argument of a division or modulo operation is zero.
* `OverflowError`: Raised when the result of an arithmetic operation is too large to be represented.

### 4. File and Environment Errors

* `FileNotFoundError`: Raised when a file or directory is requested but does not exist.
* `PermissionError`: Raised when trying to run an operation without the adequate access rights.
* `OSError`: A base class for system-related errors (like disk full, network errors, etc.).

### 5. Program Flow and Control Errors

* `StopIteration`: Raised by built-in next() to signal that an iterator has no further items.
* `KeyboardInterrupt`: Raised when the user hits the interrupt key (normally `Ctrl+C`).
* `ImportError`: Raised when the `import` statement has troubles trying to load a module.
* `ModuleNotFoundError`: A subclass of ImportError raised when a module cannot be located.


### Example

```py
def floor_division(a: int, b: int) -> int:

    if b == 0:
        raise ZeroDivisionError("Cannot divide a number by zero.")

    return a // b


try:
    print(floor_division(10, 0))
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("--- Task completed ---")
```
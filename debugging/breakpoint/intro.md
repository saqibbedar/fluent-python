# Python's Built-in Interactive Debugger (breakpoint())

Python (3.7+) has a built-in breakpoint tool that requires no setup.

Place breakpoint() right before the point of confusion:

```py
def floor_division(a: int, b: int) -> int:
    
    breakpoint()        # Execution pauses here
    
    if b == 0:
        raise ZeroDivisionError
    return a // b
```

When code hits breakpoint(), execution pauses in your terminal and gives you a (Pdb) prompt:

- Type any variable name (e.g. a) and press Enter to see its current value.
- Type p <expression> (e.g. p b==0, or b==0, or print(b)) to evaluate expressions on the fly.
- Type n to step to the next line.
- Type c to continue running.
- Type q to quit.
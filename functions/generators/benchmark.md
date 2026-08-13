# Fastest ways to consume a generator in Python

`[*gen]` and `list(gen)` are the fastest ways to consume a generator in Python. Both are implemented in optimized C code inside the interpreter, so they avoid much of the Python-level overhead that comes with manual loops.

## Performance comparison

Below is a benchmark that consumes a 10,000-item generator 1,000 times, for 10 million total items processed.

| Method | Syntax | Average execution time | Performance |
| --- | --- | --- | --- |
| List constructor | `list(gen())` | 0.86s | Fastest |
| Star unpacking | `[*gen()]` | 0.87s | Almost identical |
| Manual loop | `for x in gen(): res.append(x)` | 1.30s | ~50% slower |

## Why star unpacking and `list()` win

1. C-level optimization: both operations run in optimized interpreter internals rather than in Python bytecode loops.
2. Lower overhead: they avoid repeated attribute lookups and method calls like `result.append(...)` on each iteration.
3. Efficient list growth: Python allocates and resizes the underlying list efficiently in C.

> In practice, `[*gen]` and `list(gen)` are usually equivalent in speed. The tiny differences are not meaningful in most real-world code.

## Benchmark code

You can run this locally with Python’s built-in `timeit` module:

```python
import timeit

setup_code = """
def data_generator():
    for i in range(10_000):
        yield i
"""

unpack_time = timeit.timeit("[*data_generator()]", setup=setup_code, number=1000)
list_time = timeit.timeit("list(data_generator())", setup=setup_code, number=1000)

loop_setup = setup_code + """
def manual_loop():
    result = []
    for item in data_generator():
        result.append(item)
    return result
"""

loop_time = timeit.timeit("manual_loop()", setup=loop_setup, number=1000)

print(f"Star unpacking:  {unpack_time:.4f} seconds")
print(f"list():          {list_time:.4f} seconds")
print(f"Manual loop:     {loop_time:.4f} seconds")
```

## Summary

If your goal is to turn a generator into a list, prefer either:

```python
items = [*gen()]
```

or

```python
items = list(gen())
```

These are both fast and idiomatic. A manual `for` loop with `.append()` is usually slower and more verbose.

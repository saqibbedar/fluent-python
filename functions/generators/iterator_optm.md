# Generator unpacking and memory optimization

## Quick mental model

A generator is lazy. It produces values only when consumed.

When you unpack it, Python immediately pulls the values into a concrete container, which means:

- list unpacking creates a full in-memory list
- nested generator unpacking can trigger deeper generator execution
- large or infinite generators should be consumed in controlled chunks

> The shortcut rule: unpack only when you truly need the full collection in memory.

---

## 1) Outer unpacking vs deep unpacking

### Case A: unpack only the outer layer

If a generator yields other generators, then unpacking the outer generator gives you the inner generators themselves, not their values.

```python
nested_gen = ((x * y for y in range(3)) for x in range(3))

outer_only = [*nested_gen]
print(outer_only)
# Output:
# [<generator object ...>, <generator object ...>, <generator object ...>]
```

Why this happens:

- the outer generator yields 3 inner generators
- the outer list stores those generator objects
- the inner generators remain lazy until you iterate them

This is memory-friendly, but it is not flattening the data.

### Case B: flatten the nested generators

To get the actual values, you must iterate through each inner generator.

```python
nested_gen = ((x * y for y in range(1, 4)) for x in range(1, 4))

flattened = [item for sub_gen in nested_gen for item in sub_gen]
print(flattened)
# Output: [1, 2, 3, 2, 4, 6, 3, 6, 9]
```

This forces all nested generators to execute immediately.

That means:

- more memory use
- eager computation
- faster access once materialized

---

## 2) When unpacking becomes expensive

Unpacking is convenient, but it turns lazy data into eager data.

If the generator is large, this can create a sudden memory spike.

### Example: large generator

```python
def huge_numbers():
    for i in range(1_000_000):
        yield i

all_values = [*huge_numbers()]
```

This loads every item into memory at once.

For large datasets, this is usually a bad idea.

---

## 3) Best practice: use islice for partial consumption

If you need only a slice of a generator, use islice instead of unpacking everything.

```python
from itertools import islice


def infinite_counter():
    n = 1
    while True:
        yield n
        n += 1

first_five = [*islice(infinite_counter(), 5)]
print(first_five)
# Output: [1, 2, 3, 4, 5]
```

This is the safest pattern for:

- infinite generators
- large streams
- partial reads

---

## 4) Process data in chunks instead of all at once

When you must process a huge generator but cannot keep everything in memory, consume it in controlled chunks.

```python
from itertools import islice


def huge_generator():
    return (x for x in range(100_000))

iterator = huge_generator()

while True:
    chunk = [*islice(iterator, 3)]
    if not chunk:
        break
    print(chunk)
```

This pattern is useful for:

- streaming data
- batch processing
- memory-sensitive pipelines

---

## 5) Tuple vs list when you must materialize

If you need a fixed collection for read-only data, a tuple is usually a bit lighter than a list.

```python
import sys

gen_a = (x for x in range(1000))
gen_b = (x for x in range(1000))

list_unpack = [*gen_a]
tuple_unpack = tuple(gen_b)

print(sys.getsizeof(list_unpack))
print(sys.getsizeof(tuple_unpack))
```

This is not a huge difference for small data, but for large collections it can matter.

Use:

- list for mutability or append operations
- tuple for fixed, read-only data

---

## 6) Rule of thumb

### Use unpacking when

- the generator is small
- you need the full collection immediately
- readability and simplicity matter more than memory efficiency

### Avoid unpacking when

- the source is huge
- the generator is infinite or unbounded
- you only need a subset of values

### Prefer

- islice for partial reads
- chunked iteration for large streams
- tuple instead of list when immutability is acceptable

---

## One-line summary

A nested generator is not flattened by default; only the outer layer is consumed. To flatten it, iterate each inner generator. For memory-safe code, avoid full unpacking on large or infinite generators and process in slices or chunks instead.

---

## Quick reference

```python
# outer layer only
outer = [*nested_gen]

# full flattening
flat = [item for g in nested_gen for item in g]

# partial read
first_n = [*islice(gen, n)]

# chunked processing
chunk = [*islice(gen, 100)]
```

For performance, the answer depends on what you're trying to do.

### If you need index + value

```python
for i, num in enumerate(nums):
    ...
```

`enumerate()` is both the most Pythonic and usually the most efficient solution for index + value iteration.

Why?

* Implemented in C
* Doesn't create a list
* O(1) extra memory
* Faster than manually incrementing `i`

---

### If you need current + next element

Best choices:

```python
from itertools import pairwise

for curr, nxt in pairwise(nums):
    ...
```

or

```python
for curr, nxt in zip(nums, nums[1:]):
    ...
```

But there is an important difference:

#### `pairwise()` (better)

```python
pairwise(nums)
```

* Creates iterators only
* O(1) extra memory
* No slicing

#### `zip(nums, nums[1:])`

```python
zip(nums, nums[1:])
```

* `nums[1:]` creates a new list
* O(n) extra memory
* Copies all elements except the first

For huge lists:

```python
pairwise > zip(nums, nums[1:])
```

---

### Absolute fastest

If you're working with a list and care only about speed:

```python
for i in range(len(nums) - 1):
    curr = nums[i]
    nxt = nums[i + 1]
```

This is often the fastest because:

* Direct list indexing is very cheap
* No tuple creation
* No iterator wrappers

---

### Summary

General Python code:

```python
for i, num in enumerate(nums):
    ...
```

Adjacent comparisons:

```python
from itertools import pairwise

for a, b in pairwise(nums):
    ...
```

LeetCode / competitive programming where every microsecond matters:

```python
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        ...
```

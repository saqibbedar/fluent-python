# Python List Multiplication & Nested List Reference Trap

## 1. Understanding List Multiplication

### 1D List

```python
x = [0] * 5

print(x)
```

Output:

```python
[0, 0, 0, 0, 0]
```

### What does `[0] * 5` mean?

The list contains one element:

```python
[0]
```

List multiplication repeats the **reference to that element** five times.

Conceptually:

```text
ptr[0] ──┐
ptr[1] ──┤
ptr[2] ──┼──► 0
ptr[3] ──┤
ptr[4] ──┘
```

There are five references to the integer object `0`.

This is safe because integers are **immutable**.

---

# 2. Nested List Multiplication

Consider:

```python
m = [[0] * 3] * 3

print(m)
```

Output:

```python
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

Break the syntax into two operations.

First:

```python
[0] * 3
```

produces:

```python
[0, 0, 0]
```

Then the result is wrapped inside another list and multiplied:

```python
[[0, 0, 0]] * 3
```

List multiplication repeats the **reference to the inner list**, not the inner list itself.

Conceptually:

```text
ptr[0] ──┐
ptr[1] ──┼──► [0, 0, 0]
ptr[2] ──┘
```

Therefore, although the printed result looks like three rows, there is actually **one inner list object referenced three times**.

This is the classic nested-list reference trap.

---

# 3. Output Question

Consider:

```python
m = [[0] * 3] * 3

m[1] = [7, 7, 7]

m[0][0] = 99

print(m)
```

## Step 1 — Initial State

When `m` is created using:

```python
m = [[0] * 3] * 3
```

the outer list contains three references to the **same inner list**:

```text
m[0] ──┐
m[1] ──┼──► [0, 0, 0]
m[2] ──┘
```

So there is only **one inner list object**, but three references to it.

---

## Step 2 — `m[1] = [7, 7, 7]`

Now:

```python
m[1] = [7, 7, 7]
```

does not modify the existing inner list.

Instead, it replaces the reference stored at index `1`.

Before:

```text
m[0] ──┐
m[1] ──┼──► [0, 0, 0]
m[2] ──┘
```

After:

```text
m[0] ─────► [0, 0, 0]
m[1] ─────► [7, 7, 7]
m[2] ─────► [0, 0, 0]
```

The outer list now references **two different inner-list objects**:

* `m[0]` → `[0, 0, 0]`
* `m[1]` → `[7, 7, 7]`
* `m[2]` → the same `[0, 0, 0]` as `m[0]`

---

## Step 3 — `m[0][0] = 99`

Now:

```python
m[0][0] = 99
```

means:

1. Get the object at `m[0]`.
2. That object is the shared `[0, 0, 0]` list.
3. Change its index `0` to `99`.

So:

```text
m[0] ─────► [99, 0, 0]
m[1] ─────► [7, 7, 7]
m[2] ─────► [99, 0, 0]
```

Why did `m[2]` change too?

Because `m[0]` and `m[2]` still reference the **same inner-list object**.

We mutated the shared list itself.

---

# Final Output

Therefore:

```python
print(m)
```

produces:

```python
[
    [99, 0, 0],
    [7, 7, 7],
    [99, 0, 0]
]
```

Or simply:

```python
[[99, 0, 0], [7, 7, 7], [99, 0, 0]]
```

---

## Key Takeaway

There is an important difference between:

```python
m[1] = [7, 7, 7]
```

and:

```python
m[0][0] = 99
```

### `m[1] = ...`

Replaces the **reference stored in the outer list**.

```text
m[1] ──► old object
          ↓
       replaced by
          ↓
m[1] ──► new object
```

### `m[0][0] = ...`

Accesses the inner list and **mutates that object**.

Because `m[0]` and `m[2]` point to the same inner list, the mutation is visible through both references.

```text
m[0] ──┐
       ├──► SAME LIST ──► [99, 0, 0]
m[2] ──┘
```

> **Interview rule:** When solving nested-list output questions, always ask: **"Am I replacing a reference, or am I mutating the object that multiple references may share?"**

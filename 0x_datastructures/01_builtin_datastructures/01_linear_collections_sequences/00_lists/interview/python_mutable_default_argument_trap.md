# Python Mutable Default Argument Trap

## Introduction

Consider this function:

``` python
def make_row(row=[]):
    row.append(0)
    return row
```

At first glance, it may look as though `row=[]` means:

> "Every time I call `make_row()`, create a new empty list."

That is **not** what Python does.

The empty list used as the default argument is created **once**, when
Python executes the `def` statement. That same list object is then
reused by every call that does not explicitly provide `row`.

This creates the **mutable default argument trap**.

------------------------------------------------------------------------

# 1. First Understand the Syntax

The function has one parameter:

``` python
row
```

and a default value:

``` python
[]
```

So:

``` python
def make_row(row=[]):
```

means:

> If the caller does not provide `row`, use the default object
> associated with this parameter.

The crucial detail is **when that default object is created**.

It is created when Python executes the function definition, not every
time the function is called.

Conceptually, after Python executes:

``` python
def make_row(row=[]):
    row.append(0)
    return row
```

we can imagine the function object like this:

``` text
FUNCTION OBJECT
┌─────────────────────────────┐
│ name = make_row             │
│                             │
│ parameter = row             │
│ default ───────────────┐    │
└─────────────────────────┼────┘
                          │
                          ▼
                     ┌─────────┐
                     │  LIST   │
                     │   []    │
                     └─────────┘
```

Let's call this list **LIST A**.

The function's default argument is holding a reference to LIST A.

------------------------------------------------------------------------

# 2. First Function Call

Now:

``` python
x = make_row()
```

No argument was supplied, so Python uses the default list.

Conceptually:

``` text
row
 │
 ▼
LIST A
[]
```

Then the function executes:

``` python
row.append(0)
```

This mutates LIST A:

``` text
LIST A
[0]
```

Finally:

``` python
return row
```

returns a reference to that same list.

Therefore:

``` python
x = make_row()
```

can be visualized as:

``` text
x ─────────────────┐
                   │
row ───────────────┼──► LIST A
                   │    [0]
default ───────────┘
```

There is only **one list object** here.

------------------------------------------------------------------------

# 3. The Second Function Call

Now call:

``` python
y = make_row()
```

The important question is:

> Does Python create another `[]`?

**No.**

The default list was already created when the `def` statement executed.

So the second call also receives LIST A:

``` text
row
 │
 ▼
LIST A
[0]
```

Then:

``` python
row.append(0)
```

modifies the same object:

``` text
LIST A
[0, 0]
```

The returned value is again a reference to LIST A.

Now the memory relationship is:

``` text
x ────────────────┐
                  │
y ────────────────┼──► LIST A
                  │    [0, 0]
                  │
default ──────────┘
```

Therefore:

``` python
x is y
```

is:

``` text
True
```

This is the trap.

------------------------------------------------------------------------

# 4. The Important Insight: There Is No `*` Here

The earlier nested-list trap looked like this:

``` python
[[0] * 3] * 3
```

There, list multiplication explicitly creates multiple references to the
same inner list.

But our current example:

``` python
def make_row(row=[]):
```

contains **no multiplication at all**.

Yet we still get the same fundamental problem:

``` text
multiple references
        │
        ▼
same mutable object
```

The syntax is different, but the underlying object/reference behavior is
the same.

------------------------------------------------------------------------

# 5. What Happens When We Store Function Results in a List?

Consider:

``` python
m = [make_row(), make_row(), make_row()]
```

Let's execute it step by step.

## First call

``` python
make_row()
```

LIST A starts as:

``` text
LIST A
[]
```

`append(0)` changes it to:

``` text
LIST A
[0]
```

The returned reference is placed into the outer list:

``` text
m

┌─────────┐
│ ptr[0] ─────────► LIST A
└─────────┘          [0]
```

## Second call

Again, `make_row()` uses the same default LIST A.

Before:

``` text
LIST A
[0]
```

After:

``` text
LIST A
[0, 0]
```

The returned reference is placed into another slot:

``` text
m

┌─────────┬─────────┐
│ ptr[0]  │ ptr[1]  │
└────┬────┴────┬────┘
     │         │
     └────┬────┘
          ▼
       LIST A
       [0, 0]
```

## Third call

Again, the same LIST A is used:

``` text
LIST A
[0, 0]
```

After:

``` python
row.append(0)
```

we have:

``` text
LIST A
[0, 0, 0]
```

The returned reference becomes `m[2]`.

Final structure:

``` text
m
│
▼
OUTER LIST
│
├── ptr[0] ──┐
├── ptr[1] ──┼──► LIST A
└── ptr[2] ──┘    [0, 0, 0]
```

Therefore:

``` python
m = [make_row(), make_row(), make_row()]

print(m)
```

produces:

``` python
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

But there are **not three independent inner lists**.

There is **one list object referenced three times**.

------------------------------------------------------------------------

# 6. Proving the Trap

We can verify it with `is`:

``` python
m = [make_row(), make_row(), make_row()]

print(m[0] is m[1])
print(m[1] is m[2])
print(m[0] is m[2])
```

The result is:

``` text
True
True
True
```

All three references point to the same list object.

You can also inspect their identity:

``` python
print(id(m[0]))
print(id(m[1]))
print(id(m[2]))
```

The IDs will be the same.

------------------------------------------------------------------------

# 7. Why the Bug Becomes Visible

Now suppose:

``` python
m[0].append(99)
```

We are mutating the list referenced by `m[0]`.

But:

``` text
m[0] ──┐
m[1] ──┼──► SAME LIST
m[2] ──┘
```

Therefore the mutation is visible through all three references.

Before:

``` text
m[0] ──┐
m[1] ──┼──► [0, 0, 0]
m[2] ──┘
```

After:

``` text
m[0] ──┐
m[1] ──┼──► [0, 0, 0, 99]
m[2] ──┘
```

So:

``` python
print(m)
```

produces:

``` python
[[0, 0, 0, 99],
 [0, 0, 0, 99],
 [0, 0, 0, 99]]
```

Again, only **one list** was modified.

It merely had three references pointing to it.

------------------------------------------------------------------------

# 8. Why Explicitly Passing a List Is Different

Consider:

``` python
a = make_row([])
b = make_row([])
```

Here, each `[]` expression creates a **new list object**.

First call:

``` text
LIST A
[0]
```

Second call:

``` text
LIST B
[0]
```

So:

``` text
a ───► LIST A
       [0]

b ───► LIST B
       [0]
```

Therefore:

``` python
a is b
```

is:

``` text
False
```

This is because the lists were explicitly created separately.

------------------------------------------------------------------------

# 9. The Correct Way to Write the Function

The standard safe pattern is to use `None` as the default:

``` python
def make_row(row=None):
    if row is None:
        row = []

    row.append(0)
    return row
```

Now every call without an argument creates a **new list inside the
function**.

First call:

``` text
make_row()
    │
    ▼
new []
    │
    ▼
[0]
```

Second call:

``` text
make_row()
    │
    ▼
NEW []
    │
    ▼
[0]
```

Therefore:

``` python
a = make_row()
b = make_row()
```

gives:

``` text
a ───► LIST A
       [0]

b ───► LIST B
       [0]
```

and:

``` python
a is b
```

is:

``` text
False
```

------------------------------------------------------------------------

# 10. The General Bug Pattern

Do not memorize this merely as a "default argument trick."

The deeper rule is:

> **If multiple references point to the same mutable object, modifying
> that object through one reference is visible through all references.**

That same principle appears in many forms.

### List multiplication

``` python
x = [[0] * 3] * 3
```

``` text
ptr[0] ──┐
ptr[1] ──┼──► SAME LIST
ptr[2] ──┘
```

### Direct aliasing

``` python
a = []
b = a
```

``` text
a ──┐
    ├──► SAME LIST
b ──┘
```

### Mutable default argument

``` python
def f(x=[]):
    ...
```

Multiple calls without an explicit argument reuse the same default list.

### Shallow copying

``` python
b = a.copy()
```

The outer list may be new, but nested mutable objects can still be
shared.

All of these have the same underlying object-graph story:

``` text
REFERENCE A ──┐
              │
REFERENCE B ──┼──► MUTABLE OBJECT
              │
REFERENCE C ──┘
```

------------------------------------------------------------------------

# 11. The Interview Takeaway

When you see a Python question involving lists, dictionaries, sets,
default arguments, copying, or nested structures, ask:

> **"How many objects actually exist, and how many references point to
> each object?"**

Do not look only at the syntax.

For example:

``` python
def make_row(row=[]):
    row.append(0)
    return row
```

The important question is not:

> "Why does Python append multiple zeros?"

The important questions are:

1.  **When was the default list created?**
2.  **Is a new list created for every call?**
3.  **Which references point to the list?**
4.  **Is that object mutable?**
5.  **What happens when one reference mutates it?**

Once you answer those, the output becomes predictable without running
the code.

------------------------------------------------------------------------

# Final Mental Model

Keep this picture in your head:

``` text
             ┌─────────────────┐
             │  MUTABLE OBJECT │
             │                 │
             │    [0, 0, 0]    │
             └────────▲────────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          │           │           │
       ref A       ref B       ref C
```

The syntax that creates those references may differ:

``` python
[[0] * 3] * 3
```

``` python
b = a
```

``` python
def f(x=[]):
```

``` python
b = a.copy()
```

But the fundamental question is always the same:

> **Are multiple references sharing the same mutable object?**

If yes, mutating that object through one reference can affect what you
observe through every other reference.

That is the real concept behind Python's mutable-object traps.

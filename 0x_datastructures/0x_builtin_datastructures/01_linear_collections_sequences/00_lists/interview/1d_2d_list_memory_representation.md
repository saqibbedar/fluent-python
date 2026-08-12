# 1D and 2D List Memory Representation

This note explains how Python lists are stored in memory and why nested lists behave the way they do. The key idea is simple: a Python list does **not** store the actual objects directly. It stores pointers to those objects.

If you understand this page, the `[0] * 3` trap becomes much easier to read.

---

## 1) What a Python list stores

A Python list is a contiguous block of references. The actual integers, strings, or other objects live elsewhere on the heap. The list itself only keeps pointers to them.

Dynamic typing also follows this same pattern: Python looks at the object being referenced, checks its type information, and dispatches the correct behavior for that object.

```c
// Actual CPython code implementation
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;                 // Pointer to an array of PyObject pointers
    Py_ssize_t allocated;               // How much memory is allocated
} PyListObject;
```

### Mental model

- `x` is a label that points to a `PyListObject`.
- `PyListObject` contains `ob_item`, which points to an array of pointers.
- Each pointer in that array points to an actual Python object.

> Note: the type belongs to the object, not to the list container itself.

---

## 2) A simple 1D list example

Suppose we have:

```py
x = [1, 2, 3]
```

Conceptually, that looks like this:

```txt
x
│
▼
┌──────────────────────────────┐
│        PyListObject          │
│                              │
│ ob_size = 3 (allocated)      │
│ ob_item ─────────────────┐   │
└──────────────────────────┼───┘
                           │
                           ▼
                  ┌─────────────────────────────┐
                  │         Pointer Array       │
                  ├─────────┬─────────┬─────────┤
                  │ ptr[0]  │ ptr[1]  │ ptr[2]  │
                  └────┬────┴────┬────┴────┬────┘
                       │         │         │
                       ▼         ▼         ▼
                    ┌─────┐   ┌─────┐   ┌─────┐
                    │  1  │   │  2  │   │  3  │
                    │int  │   │int  │   │int  │
                    └─────┘   └─────┘   └─────┘
```

### What this means

- `x` points to the list object.
- The list points to three separate integer objects.
- The integers are not stored inside the list array itself.

---

## 3) How to read a 2D list

A 2D list is just a list of lists.

```py
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

At the memory level, the outer list points to three inner lists. Each inner list then points to its own elements.

```txt
Conceptually:

                         x
                         │
                         ▼
             ┌──────────────────────────┐
             │      PyListObject        │
             │                          │
             │      ob_size = 3         │
             │      ob_item ────────┐   │
             └──────────────────────┼───┘
                                    │
                              pointer array
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
               ptr[0]            ptr[1]            ptr[2]
                  │                 │                 │
                  ▼                 ▼                 ▼
           ┌────────────┐    ┌────────────┐    ┌────────────┐
           │ PyList     │    │ PyList     │    │ PyList     │
           │ [1,2,3]    │    │ [4,5,6]    │    │ [7,8,9]    │
           └─────┬──────┘    └─────┬──────┘    └─────┬──────┘
                 │                 │                 │
                 ▼                 ▼                 ▼
             ptr array          ptr array          ptr array
              │ │ │              │ │ │              │ │ │
              ▼ ▼ ▼              ▼ ▼ ▼              ▼ ▼ ▼
              1 2 3              4 5 6              7 8 9
```

### Simply put

```txt
x
│
▼
LIST
│
├──► LIST ──► 1
│         ├─► 2
│         └─► 3
│
├──► LIST ──► 4
│         ├─► 5
│         └─► 6
│
└──► LIST ──► 7
          ├─► 8
          └─► 9
```

---

## 4) How indexing works: `x[0][1]`

Accessing `x[0][1]` is really two separate indexing operations.

### First step: `x[0]`

The outer list returns the first inner list.

```txt
x
│
▼
Outer List
│
│
│                        x[0]
│                          │
│                          ▼
├── ptr[0] ───────────► [1,2,3]
├── ptr[1] ───────────► [4,5,6]
└── ptr[2] ───────────► [7,8,9]
```

### Second step: `x[0][1]`

Now Python indexes into the inner list.

```txt
    x
    │
    ▼
    outer list
    │
    │ [0]
    ▼
    inner list [1,2,3]
    │
    │ [1]
    ▼
    2
```

### Full view of the access path

```txt
x[0][1]

x
│
▼
┌───────────────┐
│ outer list    │
│               │
│ ptr[0] ───────────────┐
│ ptr[1] ────────┐      │
│ ptr[2]         │      │
└────────────────┘      │
                        ▼
                ┌─────────────┐
                │ inner list  │
                │             │
                │ ptr[0] ──► 1
                │ ptr[1] ──► 2 ◄── result
                │ ptr[2] ──► 3
                └─────────────┘
```

---

## 5) The main idea to remember

Python lists are not boxes holding raw values. They are arrays of pointers to values.

That is why:

- a 1D list is a pointer array to objects,
- a 2D list is a pointer array to other pointer arrays,
- and indexing follows those pointer chains step by step.

Once this mental model is clear, the aliasing behavior in repeated lists becomes much easier to understand.

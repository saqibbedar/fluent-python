/*
// Disclaimer: This following commented piece of code is from CPython's ceval.c file and its just a reference point for me to decode the complex syntax into normal C program so I get the idea what's going on. I am learning C and I am using CPython and other open-source projects to learn C perfectly by knowing complex design patterns and canonical way of using C.

const _Py_SpecialMethod _Py_SpecialMethods[] = {
    [SPECIAL___ENTER__] = {
        .name = &_Py_ID(__enter__),
        .error = (
            "'%T' object does not support the context manager protocol "
            "(missed __enter__ method)"
        ),
        .error_suggestion = (
            "'%T' object does not support the context manager protocol "
            "(missed __enter__ method) but it supports the asynchronous "
            "context manager protocol. Did you mean to use 'async with'?"
        )
    },
    [SPECIAL___EXIT__] = {
        .name = &_Py_ID(__exit__),
        .error = (
            "'%T' object does not support the context manager protocol "
            "(missed __exit__ method)"
        ),
        .error_suggestion = (
            "'%T' object does not support the context manager protocol "
            "(missed __exit__ method) but it supports the asynchronous "
            "context manager protocol. Did you mean to use 'async with'?"
        )
    },
    [SPECIAL___AENTER__] = {
        .name = &_Py_ID(__aenter__),
        .error = (
            "'%T' object does not support the asynchronous "
            "context manager protocol (missed __aenter__ method)"
        ),
        .error_suggestion = (
            "'%T' object does not support the asynchronous context manager "
            "protocol (missed __aenter__ method) but it supports the context "
            "manager protocol. Did you mean to use 'with'?"
        )
    },
    [SPECIAL___AEXIT__] = {
        .name = &_Py_ID(__aexit__),
        .error = (
            "'%T' object does not support the asynchronous "
            "context manager protocol (missed __aexit__ method)"
        ),
        .error_suggestion = (
            "'%T' object does not support the asynchronous context manager "
            "protocol (missed __aexit__ method) but it supports the context "
            "manager protocol. Did you mean to use 'with'?"
        )
    }
};
*/


// Person struct
struct Person {
    char *name;
    int age;
};

// Array of person struct
// Each cell is a whole object
struct Person people[] =
{
    // index 0
    [0] = {
        .name = "Saqib",
        .age = 22
    },

    // index 1
    [1] = {
        .name = "Hamza",
        .age = 23
    }
};

// syntax equivalence
/*
[0] = {
    .name = "Saqib",
    .age = 22
}

is equal to:

struct Person p = {
    .name = "Saqib",
    .age = 22
};
*/


/*
people

index 0
+----------------+
| name           |
| age            |
+----------------+

index 1
+----------------+
| name           |
| age            |
+----------------+

*/
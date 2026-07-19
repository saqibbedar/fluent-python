/*
Disclaimer: This following commented piece of code is from CPython's ceval.c file and its just a reference point for me to decode the complex syntax into normal C program so I get the idea what's going on. I am learning C and I am using CPython and other open-source projects to learn C perfectly by knowing complex design patterns and canonical way of using C.

const size_t _Py_FunctionAttributeOffsets[] = {
    [MAKE_FUNCTION_CLOSURE] = offsetof(PyFunctionObject, func_closure),
    [MAKE_FUNCTION_ANNOTATIONS] = offsetof(PyFunctionObject, func_annotations),
    [MAKE_FUNCTION_KWDEFAULTS] = offsetof(PyFunctionObject, func_kwdefaults),
    [MAKE_FUNCTION_DEFAULTS] = offsetof(PyFunctionObject, func_defaults),
    [MAKE_FUNCTION_ANNOTATE] = offsetof(PyFunctionObject, func_annotate),
};
*/

/*

Part A: Simple variable story

1. Starting from:
int x = 5;                  variable x with type->int

2. Now:
size_t x = 5;               variable x with type->size_t        (size_t is unsigned integer used for sizes)


3. Now add const:
const size_t x = 5;         x is constant with type->size_t which can't be modified.


Part B: Array [] instead fo single variable, store multiple elements into array

4. const size_t x[];
    
    Array examples in C.

    int numbers[] = {1, 2, 3, 4};
    
    accessing:

    index       value
    0      ->   1
    1      ->   2
    2      ->   3
    3      ->   4


5. Enhanced or unusual syntax:

int numbers[] = {
    // index        value
        [0]         1
        [2]         2
        [4]         3
        [6]         4
}

    Result:

    index       value
    0      ->   1
    1      ->   0                   # missing indices become zero.
    2      ->   2
    3      ->   0                   # missing indices become zero.
    4      ->   3
    5      ->   0                   # missing indices become zero.
    6      ->   4

*/



// Why it is useful?

/*
Suppose:
enum {
    APPLE,
    BANANA,
    ORANGE
};

Normally:
int price[] = {
    5,
    8,
    10
};

It means:
APPLE -> 5
BANANA -> 8
ORANGE -> 10


But later someone changes the enum.

enum {
    APPLE,
    MANGO,
    BANANA,
    ORANGE
};

Now everything is wrong.


So, instead we write:

int price[] = {
    [APPLE] = 5,
    [BANANA] = 8,
    [ORANGE] = 10
};

*/



const int table[] = {
    [2] = 100,
    [5] = 200,
    [9] = 300,
};

// indexes
#define APPLE 0
#define BANANA 1    
#define ORANGE 3                // index 2 is missing—compiler will fill the missing entry index with 0.        

// prices per fruit (index | fruit, value)
const int prices[] = {
    [APPLE] = 300,
    [BANANA] = 150,
    [ORANGE] = 180
};
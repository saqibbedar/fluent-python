#include <stdio.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

#define ADD 0
#define SUB 1
#define MUL 2

// Dispatch table: array of pointers
int (*ops[])(int, int) = {add, sub, mul};

int main(){
    pprintf("%d\n", ops[ADD](5, 5));
    return 0;
}

---
tags:
    - programming-in-c
    - programming
    - computer-science
---

# Command-Line Arguments

The [main function](TODO) take optionally take arguments when invoked:

```c
int main(int argc, char *argv []);
```

The first parameter (`argc`) contains the number of arguments passed, while the second parameter (`argv`) is an [array](./Data%20Types/Arrays.md) of [strings](./Data%20Types/Strings.md) which stores the parameters themselves. The first command-line argument is always the path through which the program was invoked.
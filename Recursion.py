"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


##fib_seq = []
##fib_seq[0] = 0
##fib_seq[1] = 1
##fib_seq[2] = 1
##fib_seq[3] = 2
##fib_seq[4] = 3
##fib_seq[5] = 5
##fib_seq[6] = 8
##fib_seq[7] = 13
##fib_seq[8] = 21
##fib_seq[9] = 34
def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    return get_fib(position -1)+ get_fib(position-2)

# Test cases
print (get_fib(9))
print (get_fib(11))
print (get_fib(0))

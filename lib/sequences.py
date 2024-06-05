#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fib_sequence = [0, 1]
        for i in range(2, length):
            next_num = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_num)
        print(fib_sequence)
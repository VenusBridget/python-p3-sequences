#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    seq = []
    if length > 0:
        seq.append(0)
    if length >= 2:
        seq.append(1)
        for i in range(2, length):
            seq.append(seq[-1] + seq[-2])
            
    print(seq)
print_fibonacci(9)
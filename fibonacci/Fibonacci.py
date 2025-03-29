# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 04:25:05 2025

@author: SEA4720
"""
number = int(input('Please enter a positive integer: '))

a, b = 0, 1
fib = []

# Generate Fibonacci sequence up to the nth term
for i in range(number):
    fib.append(a)
    a, b = b, a + b

# Print the Fibonacci sequence, separated by commas
print(*fib, sep=',')

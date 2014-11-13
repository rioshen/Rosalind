#!/usr/bin/env python

'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Fibonacci Numbers 
Rosalind ID: FIBO
Algorithmic Heights #: 001
URL: http://rosalind.info/problems/fibo
'''

def fib(n):
    '''Returns the value of F(N).'''
    a, b = 0, 1
    while n:
        a, b = b, a+b
        n -= 1
    return a

if __name__ == '__main__':
    with open('../data/algo/rosalind_fibo.txt') as f:
        num = int(f.read().strip())
        print fib(num)

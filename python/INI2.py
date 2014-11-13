#!/usr/bin/env python

"""
A solution to a ROSALIND problem from the Python location.
Problem Title: Variables and Some Arithmetic
Rosalind Python ID: INI2
Rosalind Python #: 002
URL: http://rosalind.info/problems/ini2/
"""

if __name__ == '__main__':
    with open('../data/python/rosalind_ini2.txt') as f:
        a, b = map(int, f.read().strip().split())
        print (a**2 + b**2)

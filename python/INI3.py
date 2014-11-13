#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Python location.
Problem Title: Strings and Lists
Rosalind Python ID: INI3
Rosalind Python #: 003
URL: http://rosalind.info/problems/ini3/
'''

if __name__ == '__main__':
    with open('../data/python/rosalind_ini3.txt') as f:
        s, digits = [line.strip() for line in f.readlines()]
        a, b, c, d = map(int, digits.split())
        print ' '.join([s[a:b+1], s[c:d+1]])

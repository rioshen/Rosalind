#!/usr/bin/env python

'''
A solution to a ROSALIND problem from the Python location.
Problem Title: Working with Files
Rosalind Python ID: INI5
Rosalind Python #: 005
URL: http://rosalind.info/problems/ini5/
'''

if __name__ == '__main__':
    with open("../data/python/rosalind_ini5.txt") as f:
        content = [line.strip() for number, line in enumerate(f.readlines()) if number % 2 != 0]
        print '\n'.join(content)

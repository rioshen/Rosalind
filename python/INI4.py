#!/usr/bin/env python

'''
'''

if __name__ == '__main__':
    with open('../data/python/rosalind_ini4.txt') as f:
        a, b = map(int, f.read().strip().split())
        result = sum((val for val in xrange(a, b+1) if val % 2 != 0))
        print result

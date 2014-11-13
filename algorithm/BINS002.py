#!/usr/bin/env python

'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Binary Search
Rosalind ID: BINS
Algorithmic Heights #: 002
URL: http://rosalind.info/problems/bins
'''

def bsearch(seq, target):
    lo, hi = 0, len(seq)-1
    while lo <= hi:
        mid = (hi+lo) // 2
        if seq[mid] == target:
            return mid
        elif seq[mid] > target:
            hi = mid-1
        else:
            lo = mid+1
    return -1

if __name__ == '__main__':
    with open('../data/algo/rosalind_bins.txt') as f:
        n, m = [int(f.readline().strip()) for repeat in xrange(2)]
        sequence = map(int, f.readline().strip().split())
        targets = map(int, f.readline().strip().split())
        result = [bsearch(sequence, target) for target in targets]
        print ' '.join([str(index+1) if index >= 0 else str(-1) for index in result])
        

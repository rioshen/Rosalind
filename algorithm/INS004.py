#!/usr/bin/env python

'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Insertion Sort
Rosalind ID: INS
Algorithmic Heights #: 004
URL: http://rosalind.info/problems/ins/
'''
def insertionsort(seq):
    count = 0
    for i in xrange(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
            count += 1
    return count


if __name__ == '__main__':
    with open('../data/algo/rosalind_ins.txt') as f:
        seq = map(int, f.readlines()[1].strip().split())
        print insertionsort(seq)

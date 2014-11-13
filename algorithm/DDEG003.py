#!/usr/bin/env python

'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Degree Array
Rosalind ID: DEG
Algorithmic Heights #: 003
URL: http://rosalind.info/problems/deg/
'''

def degree(verties, edges):
    degree = [0]*verties
    for edge in edges:
        for node in edge:
            degree[node-1] += 1
    return degree


if __name__ == '__main__':
    with open('../data/algo/rosalind_deg.txt') as f:
        n, m = map(int, f.readline().strip().split())
        edges = [map(int, line.strip().split()) for line in f.readlines()]
        print ' '.join(map(str, degree(n, edges)))

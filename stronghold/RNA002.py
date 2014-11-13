#!/usr/bin/env python

def dna2rna(dna):
    return dna.replace('T', 'U')

def dna2rna2(dna):
    return ''.join(['U' if x == 'T' else x for x in dna])

if __name__ == '__main__':
    with open('../data/stronghold/rosalind_rna.txt') as f:
        dna = f.read().strip()
        print dna2rna(dna)


#!/usr/bin/env python

def countdna(dna):
    counter = {key: 0 for key in 'ACGT'}
    for elem in dna:
        if elem in counter:
            counter[elem] += 1
    sorted(counter)
    return map(str, [counter['A'], counter['C'], counter['G'], counter['T']])

def countdna2(dna):
    from collections import Counter
    count = Counter(dna)
    return [str(count[elem]) for elem in 'ACGT']

if __name__ == '__main__':
    with open('../data/rosalind_dna.txt') as f:
        dna = f.read().strip()
        print ' '.join(countdna(dna))
        print ' '.join(countdna2(dna))

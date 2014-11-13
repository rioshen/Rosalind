#!/usr/bin/env python

'''
'''

with open('../data/python/rosalind_ini6.txt') as input_data:
    words = input_data.read().strip().split()

word_count_dict = dict()
for word in words:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

word_count = [map(str, count) for count in word_count_dict.items()]

with open('Python_INI6.txt', "w") as output_data:
    output_data.write(' '.join(word_count[0]))
    for count in word_count[1:]:
        output_data.write('\n'+' '.join(count))

#!/usr/local/bin/python3

import sys

# open file as an argument
file = open(sys.argv[1], 'r')


data = file.read()

# Remove puncuation
for x in "!@#$%^&*()_+-={}|:\"<>?[]\\;\',./":
    data = data.replace(x, "")

words = data.split()

# get the count and the word length
count = {}
for y in words:
	word_length = len(y)
	count[word_length] = count.get(word_length, 0) + 1

# print the count and word length
print ("Length Count")
for key, value in count.items() :
    print('{} {}'.format(key, value))

file.close()



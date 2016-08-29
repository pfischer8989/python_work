#!/usr/local/bin/python3

import sys


file = open(sys.argv[1], 'r')
#file = open('declaration.txt','r')


data = file.read()

# Remove puncuation
for x in "!@#$%^&*()_+-={}|:\"<>?[]\\;\',./":
    data = data.replace(x, "")

# print (data)

words = data.split()

# print (words)
# print (words(len))

count = {}
for y in words:
	word_length = len(y)
	count[word_length] = count.get(word_length, 0) +1


print ("Length Count")
for key, value in count.items() :
   # print (key, value)
    print('{} {}'.format(key, value))


#for y in count:
#	print (y, ':', count[y])


# for x, letter in enumerate(data):
#	print (letter)


# def process (file):
	# for x, line in enumerate(file):
		# print (line)
		# print (x)
		
		#clean = line.read().replace(punct, '')

		#print (clean)
	


	#	for y, word in enumerate(line):
	#		print (word)
	#		clean = ""
			
	#		if word not in punct:
	#			clean = clean + word
			#	print ("this is clean", clean)
			
			# for z, clean in enumerate(line.split(' ')):
			#	print (clean)
			#	print (line)
			#	print (y)

#def chop (file):
#	for x in sting.punctuation:
#		cleaned = file.replace(punct, "")

# readin = readin.replace("\n", " ")
# readin = readin.replace("  ", " ")


# process (file)
# chop (file)


# data = file.read().replace('\n', '')




#!/usr/local/bin/python3

import sys

# open file as an argument
file = open('declaration.txt', 'r')
# file = open(sys.argv[1], 'r')


data = file.read()

# Remove puncuation
for x in "!@#$%^&*()_+-={}|:\"<>?[]\\;\',./":
    data = data.replace(x, "")

words = data.split()

# get the count and the word length
count = {}
for y in words:
	word_length = len(y)
	count[word_length] = count.get(word_length, 0) +1

# print the count and word length
print ('{:<5} {:>8}'.format('Length', 'Count'))
for key, value in count.items():
    print('{:>6} {:>9}'.format(key, value))



print ('\n')


y_axe = 400
x_axe = 17
c = 1
draw = ""



# Vertical Axis  
for x in range (y_axe, 0, -20):
	
	    
	for i in range (1, x_axe):
	
	    if i in count.keys() and count[i] >= x:
			draw += '***'
	    else:
			draw += '   '
	
	if (x % 100) == 0:
		print(" " + str(x) + "-| {0}".format(draw))
	else:
		print ("     | {:>6}".format(draw))
	
	# reset draw
	draw = ""
	
		


# Horizontal X Axis
hdraw = '    -+'	
for e in range(1, 20):
	hdraw += '-+-'
hdraw += '>'
print (hdraw)

# Horizontal X Index
idraw = ''
for y in range (1, x_axe):
	idraw += ' %d ' % y
print ("     |{:>40}".format(idraw)) 

file.close()





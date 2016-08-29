__author__ = 'pfischer'

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop thru the list
for number in the_count:
    print("This is count %d" % number)

# same as above
for fruit in fruits:
    print(" A fruit of type: %s" % fruit)

# we can go thu mixed lists too
# we have to use %r since we dont know what in it
for i in change:
    print("I got %r" % i)

# we can also build lists

elements = []

# use range function to do the 0 to 5
for i in range(0, 6):
    print(" Adding %d to the list" % i)
    elements.append(i)

# now print them
for i in elements:
    print("Element was: %d" % i)


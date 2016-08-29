from functools import partial
# from itertools import zip

v = 25
u = 0
t = 10

x = (v - u) / t

print("This is a {}".format(x))

a = 0
b = 0
q = 0

if a and b and q == 1:
	print(True)
	
if a and b and q == 0:
	print(False)

else: 
	print('One is false')


fn = 0
f0 = 0
f1 = 1


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg



list = [1, 3, 4, 2, 5]

list.sort()
list2 = sorted(list)
list2.reverse()
print(list2)


key = '239482349299:sajshdjekkwkksk'
keyid = key.split(':')

print (keyid[0])

colors = ['red', 'blue', 'yellow', 'green']

foocol = colors.sort()
# print sorted(foocol, key=len)

blocks = []
#for block in iter(partial(f.read, 32), ''):
#	blocks.append(block)

names = ['paul', 'rhys', 'kirsten', 'lachlan']
colors = ['red', 'green', 'blue', 'yellow']

d = dict(zip(names, colors))

print (d)

		
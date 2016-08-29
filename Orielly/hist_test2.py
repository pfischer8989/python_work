data = {1:16, 2:267, 3:267, 4:169, 5:140, 6:112, 7:99, 8:68, 9:61, 10:56, 11:35, 12:13, 13:9, 14:7, 15:2}

y_axe = 400
x_axe = 17
c = 1
draw = ""

print (data)

# Vertical Axis 
for x in range (y_axe, 0, -20):
	

	
		# print(draw)
		#vdraw = '|'
	#else: 
		#print (" {:>6}".format(draw))
		#print (draw)
	    
	for i in range (1, x_axe):

		
	    if i in data.keys() and data[i] >= x:
			draw += '***'

			#print ("this is draw", draw)
			
	    else:
			draw += '  '
			#print ("this is the other draw", draw)
	
	# print (draw)
	if (x % 100) == 0:
		print(" " + str(x) + "-| {0}".format(draw))
	else:
		print ("     | {:>6}".format(draw))
	
	# reset draw
	draw = ""
	#print (" {:>6}".format(draw))
		


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
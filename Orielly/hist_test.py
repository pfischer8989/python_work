
data = {1:16, 2:267, 3:267, 4:169, 5:140, 6:112, 7:99, 8:68, 9:61, 10:56, 11:35, 12:13, 13:9, 14:7, 15:2}

y_axe = 400
x_axe = 20
c = 1
draw = ""

# Vertical Axis 
for x in range (y_axe, 0, -20):
	

	if (x % 100) == 0:
		print(" " + str(x) + " -|{0}".format(draw))
		# print("\n")
		#vdraw = '|'
	else: 

	    #print (" {:>6}".format(draw))
	#	print (draw)
	    
	    for i in range (1, x_axe):
		   if i in data.keys() and data[i] >= x:
			   draw += '***'
			   print ("this is draw", draw)
			
		   else:
			   draw += '  '
			   print ("this is the other draw", draw)
	    print (draw)
	#print (" {:>6}".format(draw))
		


# Horizontal X Axis
hdraw = '    -'	
for e in range(1, x_axe):
	hdraw += '-+-'
hdraw += '>'
print (hdraw)

idraw = ''
for y in range (1, x_axe):
	idraw += ' %d' % y
print (idraw)

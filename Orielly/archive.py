import os, tarfile, glob, shutil, zipfile

def zip_files(path):	
	
	zf = zipfile.ZipFile("my_archive.zip", 'w')
	dir = os.getcwd()
	

	for root, dirs, files in os.walk(path):
		for filename in files:	
			# grab hotels from the path		
			strip = os.path.basename(root)
			zf.write(os.path.join(root, filename), strip + '/' + filename, zipfile.ZIP_DEFLATED)
			

	zf.close()
	zf.namelist()
	

if __name__ == "__main__":
	# create_files()
	# zip_files()

	hotels = ["sheraton", "hilton", "marriot"]
	thepath = "/tmp/hotels" # all students have v:/workspace, only hotels is new
	# I had to sort your list because when files are created in a directory on unix they are put in alphabetical order.
	expected = sorted(["hotels/"+hotel for hotel in hotels])

	if not os.path.exists(thepath):
		os.mkdir(thepath)

	for n in hotels: # effectively setUp()
		f = open(os.path.join(thepath,n), 'w')
		f.write("website: hits:")
		f.close()

	zip_files("/tmp/hotels")
	zf = zipfile.ZipFile("my_archive.zip") # the name you gave it
	observed = zf.namelist()
	print("namelist:", observed)
	print("expected:", expected)

	if set(expected) == set(observed):
		print("The test passes")
	else:
		print("The test fails")

	shutil.rmtree(thepath) # effectively tearDown()
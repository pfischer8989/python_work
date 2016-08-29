import os, tarfile, glob, shutil, zipfile

def zip_files(path):
	
	zf = zipfile.ZipFile("my_archive.zip", 'w')
	
	for root, dirs, files in os.walk('hotels/'):
		for files in files:
			zf.write(os.path.join(root, files))

	zf.close()
	zf = zipfile.ZipFile("my_archive.zip")
	zf.namelist()
	

if __name__ == "__main__":

	hotels = ["sheraton", "hilton", "marriot"]
	thepath = "/Users/pfischer/Documents/python/test/hotels" # all students have v:/workspace, only hotels is new
	expected = ["hotels/"+hotel for hotel in hotels]

	if not os.path.exists(thepath):
		os.mkdir(thepath)

	for n in hotels: # effectively setUp()
		f = open(os.path.join(thepath,n), 'w')
		f.write("website: hits:")
		f.close()

	zip_files("/Users/pfischer/Documents/python/test/hotels")
	zf = zipfile.ZipFile("my_archive.zip") # the name you gave it
	observed = zf.namelist()
	print("namelist:", observed)
	print("expected:", expected)

	if set(expected) == set(observed):
		print("The test passes")
	else:
		print("The test fails")

	shutil.rmtree(thepath) # effectively tearDown()
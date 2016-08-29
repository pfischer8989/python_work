#!/usr/bin/env python
import os
import zipfile

def zipdir(path, zip):
    for root, dir, files in os.walk(path):
    	print ("This is root", root)
    	print ("This is files", files)
    	print ("This is dirs", dir)
        for file in files:
            zip.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w')
    zipdir('archive/', zipf)
    zipf.close()

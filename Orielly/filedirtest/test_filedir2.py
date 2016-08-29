import unittest
import tempfile
import shutil
import glob
import os
from filedir import cwdpath, dirsearch, output

rootpath = "/Users/pfischer/Documents/python/test/filedirtest"
testpath = "/Users/pfischer/Documents/python/test/filedirtest/testdir"

teststore = {}

class TestFile(unittest.TestCase):

    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = os.makedirs("testdir")
        os.chdir(testpath)

    def test_1(self):
        "Verify creation of files is possible"
        os.chdir(testpath)
        for filename in ("foo.py", "goo.py", "bro.pyc"):
            f = open(filename, "w")
            f.write("Some text\n")    
            f.close()

        os.chdir(rootpath)
        shutil.rmtree('testdir')

    
        


if __name__ == "__main__":
    unittest.main()






 
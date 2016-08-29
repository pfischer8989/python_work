"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible"
        for filename in ("this.txt", "that.txt", "the_other.txt"):
            f = open(filename, "w")
            f.write("Some text\n")    
            #f.close()
            #self.assertTrue(f.closed) 
                 
        genfiles = os.listdir(self.dirname)
        currentdir = os.listdir(self.dirname)
        self.assertEqual(genfiles, currentdir, "The files are not Equal")

        
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        f = open('binfile', 'wb')
        f.write(b'1'*1000000)  
        f.close()
        
        filestat = os.stat("binfile")
        filelen = filestat.st_size
        
        self.assertEqual(filelen, 1000000, "The file is not the correct length")    

    def tearDown(self):
        pass
        # os.chdir(self.origdir)
        # shutil.rmtree(self.dirname)


if __name__ == "__main__":
    unittest.main()


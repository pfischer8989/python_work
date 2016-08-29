import unittest
import filedir

class TestFile(unittest.TestCase):

	def test_path(self):
		#f = cwdpath()
		cwd = os.getcwd()
		self.failUnless(False)

if __name__ == "__main__":
    unittest.main()
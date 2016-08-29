import unittest
import filedir

class TestFile(unittest.TestCase):

	def test_path(self):
		f = cwdpath()
		cwd = os.getcwd()
		self.failUnless(f.matches(cwd))

if __name__ == "__main__":
    unittest.main()
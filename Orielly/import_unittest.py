import unittest

class TestMeNow(unittest.TestCase):
    def test_very_important(self):
        print("If this doesn't run, I'm in big trouble")
        self.assertNotEqual(2 + 2, 4, "They're the same!")

if __name__ == "__main__":
    unittest.main()

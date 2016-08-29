import unittest
import glob
import os
from shelf2 import shelfme

class TestShelf(unittest.TestCase):

    def testStoreHighScore(self):
        HighScore = shelfme
        self.assertEqual(-100, HighScore('joe', -100))
        self.assertGreater(-99, HighScore('joe', -100))
        self.assertEqual(0, HighScore('joe', 0))
        self.assertLess(0, HighScore('chris', 100))
        self.assertEqual(1000, HighScore('chris', 1000))
        self.assertLess(100, HighScore('chris', 1000))
        self.assertEqual(0, HighScore('joe', -1))



    def test_many_scores(self):
        HighScore = shelfme
        self.assertEqual(50, HighScore('Kirby', 50))
        self.assertEqual(150, HighScore('Kirby', 150))
        self.assertEqual(150, HighScore('Kirby', 40))
        self.assertEqual(150, HighScore('Kirby', 95))
        self.assertTrue(HighScore('Kirby', 180) == 180, 'Kirby should have 180 as a top score')

    def tearDown(self):
        try:
            files = glob.glob("*.db")
            for f in files:
                os.remove(f)

        except Exception:
            pass 




if __name__ == "__main__":
    unittest.main()
import unittest


def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]

class TestTitle(unittest.TestCase): 
    
    def test_string(self):
        self.assertEqual(title("foobar foobar"), "Foobar Foobar", "Should return Foobar")
     
    def test_2(self):
        s = "foobar"
        self.assertEqual(s.title(), title(s), "Outcome is not the same")
     
        
if __name__ == "__main__":
    unittest.main()

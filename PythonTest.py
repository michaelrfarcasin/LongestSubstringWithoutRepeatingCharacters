import unittest

class PythonTest(unittest.TestCase):
    def test_strIn(self):
        self.assertTrue('a' in "abc")
        
    def test_strIn_false(self):
        self.assertFalse('d' in "abc")
    
if __name__ == '__main__':
    unittest.main()

import unittest
from LongestSubstring import LongestSubstring

class LongestSubstringTest(unittest.TestCase):
    def setUp(self):
        self.useCase = LongestSubstring()
    
    def test_getLength_emptyString(self):
        self.assertEqual(0, self.useCase.getLength(""))
        
    def test_getLength_oneCharacter(self):
        self.assertEqual(1, self.useCase.getLength("a"))
        
    def test_getLength_twoCharacters_same(self):
        self.assertEqual(1, self.useCase.getLength("aa"))
        
    def test_getLength_twoCharacters_different(self):
        self.assertEqual(2, self.useCase.getLength("ab"))
        
    def test_getLength_threeCharacters_allDifferent(self):
        self.assertEqual(3, self.useCase.getLength("abc"))
        
    def test_getLength_threeCharacters_firstTwoSame(self):
        self.assertEqual(2, self.useCase.getLength("aab"))
        
    def test_getLength_threeCharacters_lastTwoSame(self):
        self.assertEqual(2, self.useCase.getLength("abb"))
        
    def test_getLength_threeCharacters_firstAndLastSame(self):
        self.assertEqual(2, self.useCase.getLength("aba"))
        
    def test_getLength_fourCharacters_allDifferent(self):
        self.assertEqual(4, self.useCase.getLength("abcd"))
        
    def test_getLength_fourCharacters_firstTwoSame(self):
        self.assertEqual(3, self.useCase.getLength("bbcd"))
        
    def test_getLength_fourCharacters_lastTwoSame(self):
        self.assertEqual(3, self.useCase.getLength("abcc"))
        
    def test_getLength_fourCharacters_middleTwoSame(self):
        self.assertEqual(2, self.useCase.getLength("abbc"))
        
    def test_getLength_leetCodeExampleOne(self):
        self.assertEqual(3, self.useCase.getLength("abcabcbb"))
        
    def test_getLength_leetCodeExampleTwo(self):
        self.assertEqual(1, self.useCase.getLength("bbbbb"))
        
    def test_getLength_leetCodeExampleThree(self):
        self.assertEqual(3, self.useCase.getLength("pwwkew"))
        
    def test_getLength_leetCodeExampleFour(self):
        self.assertEqual(3, self.useCase.getLength("dvdf"))
        
if __name__ == '__main__':
    unittest.main()

from fourthtask import find_largest_palindrome
import unittest

class Test(unittest.TestCase):

    def testProcess(self):
        self.assertTrue(find_largest_palindrome(100, 100, 1000, 1000), 906609)


if __name__ == '__main__':
    unittest.main()
from fifthtask import smallest_multiple
import unittest

class Test(unittest.TestCase):

    def testProcess(self):
        self.assertTrue(smallest_multiple(2520), 232792560)


if __name__ == '__main__':
    unittest.main()
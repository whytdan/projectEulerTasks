from firsttask import multiplesOf3and5
import unittest

class Test(unittest.TestCase):
    def testIfInt(self):
        self.assertEqual(multiplesOf3and5(1.5), 'Number can not be float! Int is required!')

    def testIfNumGtThan3(self):
        self.assertEqual(multiplesOf3and5(3), 'Number must be greater than 3!')

    def testProcess(self):
        self.assertEqual(multiplesOf3and5(1001), 234168)


if __name__ == '__main__':
    unittest.main()
from secondtask import sum_of_fibo_list
import unittest

class Test(unittest.TestCase):

    def testIfInt(self):
        self.assertEqual(sum_of_fibo_list(1.5), 'Number can not be float! Int is required!')

    def testIfPositive(self):
        self.assertEqual(sum_of_fibo_list(-1), 'Number must be positive!')

    def testProcess(self):
        self.assertTrue(sum_of_fibo_list(33), 4613732) #2,8 First even numbers of Fibonacci lt 10


if __name__ == '__main__':
    unittest.main()
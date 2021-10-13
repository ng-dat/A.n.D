import unittest
import sys

sys.path.append('./')
from search.quick_select.python.quick_select import *


class TestSortingMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNormalArrayInput1(self):
        arr = [0, 4, 2, 3, 1]
        start = 0
        end = 4
        i = 4
        ith_smallest = random_select(arr, start, end, i)
        self.assertEqual(3, ith_smallest)

    def testNormalArrayInput2(self):
        arr = [0, 4, 2, 3, 1]
        start = 0
        end = 4
        i = 2
        ith_smallest = random_select(arr, start, end, i)
        print(arr)
        self.assertEqual(1, ith_smallest)

    def testNormalArrayInput3(self):
        arr = [0, 4, 2, 3, 1]
        start = 0
        end = 4
        i = 5
        ith_smallest = random_select(arr, start, end, i)
        self.assertEqual(4, ith_smallest)

    def testNormalArrayInput4(self):
        arr = [0, 4, 2, 3, 1]
        start = 0
        end = 4
        i = 1
        ith_smallest = random_select(arr, start, end, i)
        self.assertEqual(0, ith_smallest)

    def testNormalArrayInput5(self):
        arr = [3]
        start = 0
        end = 0
        i = 1
        ith_smallest = random_select(arr, start, end, i)
        self.assertEqual(3, ith_smallest)

    def testNormalArrayInput6(self):
        arr = [1,3,2]
        start = 0
        end = 2
        i = 4
        ith_smallest = random_select(arr, start, end, i)
        self.assertEqual(3, ith_smallest)


if __name__ == '__main__':
    unittest.main()

import unittest
import sys

sys.path.append('./')
from sorting.python import bubble_sort
from sorting.python import heap_sort
from sorting.python import insertion_sort
from sorting.python import merge_sort
from sorting.python import quick_sort
from sorting.python import selection_sort
from sorting.python import tim_sort


class TestSortingMethods(unittest.TestCase):

    def setUp(self):
        self._sortFunc = sortFunc

    def tearDown(self):
        pass

    def testNormalArrayInput(self):
        arr = [0, 4, 2, 3, 1]
        expected_arr = [0, 1, 2, 3, 4]
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)

    def testEmptyArrayInput(self):
        arr = []
        expected_arr = []
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)

    def testSingleElementArrayInput(self):
        arr = [1]
        expected_arr = [1]
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)

    def testSortedArrayInput(self):
        arr = [1, 2, 4, 8]
        expected_arr = [1, 2, 4, 8]
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)

    def testReverselySortedArrayInput(self):
        arr = [8, 4, 2, 1]
        expected_arr = [1, 2, 4, 8]
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)

    def testRepeatedElementsArrayInput(self):
        arr = [1, 1, 1, 1]
        expected_arr = [1, 1, 1, 1]
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)

    def testDuplicatedElementsArrayInput(self):
        arr = [8, 1, 4, 1]
        expected_arr = [1, 1, 4, 8]
        sorted_arr = self._sortFunc(arr)
        self.assertEqual(sorted_arr, expected_arr)


def normalSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


sort_funcs = {
    'test': normalSort,
    'bubble': bubble_sort.sort,
    'heap': heap_sort.sort,
    'insertion': insertion_sort.sort,
    'merge': merge_sort.sort,
    'quick': quick_sort.sort,
    'selection': selection_sort.sort,
    'tim': tim_sort.sort
}

if __name__ == '__main__':
    sort_type_code = 'bubble' if (not sys.argv or len(sys.argv) != 2 or sys.argv[1] is None) else str(sys.argv[1])
    sortFunc = sort_funcs[sort_type_code]

    unittest.main(argv=[sys.argv[0]])

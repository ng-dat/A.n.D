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
        expectedArr = [0, 1, 2, 3, 4]
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)

    def testEmptyArrayInput(self):
        arr = []
        expectedArr = []
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)

    def testSingleElementArrayInput(self):
        arr = [1]
        expectedArr = [1]
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)

    def testSortedArrayInput(self):
        arr = [1, 2, 4, 8]
        expectedArr = [1, 2, 4, 8]
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)

    def testReverselySortedArrayInput(self):
        arr = [8, 4, 2, 1]
        expectedArr = [1, 2, 4, 8]
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)

    def testRepeatedElementsArrayInput(self):
        arr = [1, 1, 1, 1]
        expectedArr = [1, 1, 1, 1]
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)

    def testDuplicatedElementsArrayInput(self):
        arr = [8, 1, 4, 1]
        expectedArr = [1, 1, 4, 8]
        sortedArr = self._sortFunc(arr)
        self.assertEqual(sortedArr, expectedArr)


def normalSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

sortFuncs = {
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
    sortTypeCode = 'bubble' if (not sys.argv or len(sys.argv) != 2 or sys.argv[1] == None) else str(sys.argv[1])
    sortFunc = sortFuncs[sortTypeCode]

    unittest.main(argv=[sys.argv[0]])

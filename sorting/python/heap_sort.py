'''
    Refer to: http://www.cs.utsa.edu/~wagner/CS3343/r6/r6ans.html
'''

def sort(array):
    def _exchange(array, i, j):
        array[i], array[j] = array[j], array[i]

    def _left(i):
        return 2 * (i + 1) - 1

    def _right(i):
        return 2 * (i + 1) + 1 - 1

    def _maxHeapify(array, i):
        l = _left(i)
        r = _right(i)
        largest = i
        if l < _heapSize[0] and array[l] > array[largest]:
            largest = l
        if r < _heapSize[0] and array[r] > array[largest]:
            largest = r
        if largest != i:
            _exchange(array, i, largest)
            _maxHeapify(array, largest)

    def _buildMaxHeap(array):
        _heapSize[0] = len(array)
        nonLeafNodesCount = int((len(array)) / 2)
        for i in range(nonLeafNodesCount + 1):
            _maxHeapify(array, nonLeafNodesCount - i)

    _heapSize = [0]
    _buildMaxHeap(array)
    for sortedSize in range(len(array) - 1):
        heapLastIndex = _heapSize[0] -1
        _exchange(array, 0, heapLastIndex)
        _heapSize[0] -= 1
        _maxHeapify(array, 0)
    return array

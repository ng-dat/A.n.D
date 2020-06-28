"""
    Refer to: http://www.cs.utsa.edu/~wagner/CS3343/r6/r6ans.html
"""


def sort(array):

    def __exchange(array, i, j):
        array[i], array[j] = array[j], array[i]

    def __left(i):
        return 2 * (i + 1) - 1

    def __right(i):
        return 2 * (i + 1) + 1 - 1

    def __maxHeapify(array, i):
        l = __left(i)
        r = __right(i)
        largest = i
        if l < __heapSize[0] and array[l] > array[largest]:
            largest = l
        if r < __heapSize[0] and array[r] > array[largest]:
            largest = r
        if largest != i:
            __exchange(array, i, largest)
            __maxHeapify(array, largest)

    def __buildMaxHeap(array):
        __heapSize[0] = len(array)
        non_leaf_nodes_count = int((len(array)) / 2)
        for i in range(non_leaf_nodes_count + 1):
            __maxHeapify(array, non_leaf_nodes_count - i)

    __heapSize = [0]
    __buildMaxHeap(array)
    for sorted_size in range(len(array) - 1):
        heap_last_index = __heapSize[0] -1
        __exchange(array, 0, heap_last_index)
        __heapSize[0] -= 1
        __maxHeapify(array, 0)
    return array

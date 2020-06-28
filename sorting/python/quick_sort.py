import random


def sort(array):

    def __exchange(array, i, j):
        array[i], array[j] = array[j], array[i]

    def __quickSort(array, start, end):
        if (end - start) <= 0:
            return array

        pivot = __partition(array, start, end)

        __quickSort(array, start, pivot - 1)
        __quickSort(array, pivot + 1, end)

        return array

    def __partition(array, start, end):
        mark_value = array[start]
        left_control = start + 1
        right_control = end

        while (right_control >= left_control):
            if array[left_control] < mark_value:
                left_control += 1
            elif array[right_control] > mark_value:
                right_control -= 1
            else:
                __exchange(array, left_control, right_control)
                left_control += 1
                right_control -= 1
        __exchange(array, start, right_control)

        return right_control

    random.shuffle(array) # To make sure the array is not in the worst case. This function has O(n) complexity
    return __quickSort(array, 0, len(array) - 1)

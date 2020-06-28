def sort(array):
    for sorted_size in range(0, len(array) - 1):
        swapped = False
        for i in range(0, len(array) - 1 - sorted_size):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:
            break
    return array

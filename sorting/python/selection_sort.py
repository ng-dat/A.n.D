def sort(array):
    for sortedSize in range(len(array) - 1):
        minIndex = sortedSize
        for i in range(sortedSize, len(array)):
            if array[i] < array[minIndex]:
                minIndex = i
        array[sortedSize], array[minIndex] = array[minIndex], array[sortedSize]
    return array

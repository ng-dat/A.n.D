def sort(array):
    for sortedSize in range(len(array) - 1):
        minValueIndex = sortedSize
        for i in range(sortedSize, len(array)):
            if array[i] < array[minValueIndex]:
                minValueIndex = i
        array[sortedSize], array[minValueIndex] = array[minValueIndex], array[sortedSize]
    return array

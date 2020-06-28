def sort(array):
    def _merge(leftArray, rightArray):
        array = []
        while leftArray and rightArray:
            if leftArray[0] < rightArray[0]:
                array.append(leftArray.pop(0))
            else:
                array.append(rightArray.pop(0))
        array.extend(leftArray)
        array.extend(rightArray)
        return array

    if len(array) <= 1:
        return array

    midIndex = int((len(array) + 1) / 2)

    leftArray = sort(array[:midIndex])
    rightArray = sort(array[midIndex:])

    return _merge(leftArray, rightArray)

def sort(array):
    for sortedSize in range(len(array)):
        insertedValue = array[sortedSize]
        indexToInsert = sortedSize - 1
        while indexToInsert >= 0:
            if array[indexToInsert] > insertedValue:
                array[indexToInsert + 1] = array[indexToInsert]
            else:
                break
            indexToInsert -= 1
        indexToInsert += 1
        array[indexToInsert] = insertedValue
    return array

def sort(array):

    def _merge(left_array, right_array):
        array = []
        while left_array and right_array:
            if left_array[0] < right_array[0]:
                array.append(left_array.pop(0))
            else:
                array.append(right_array.pop(0))
        array.extend(left_array)
        array.extend(right_array)
        return array

    if len(array) <= 1:
        return array

    mid_index = int((len(array) + 1) / 2)

    left_array = sort(array[:mid_index])
    right_array = sort(array[mid_index:])

    return _merge(left_array, right_array)

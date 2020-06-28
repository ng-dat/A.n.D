def sort(array):
    for sorted_size in range(len(array) - 1):
        min_value_index = sorted_size
        for i in range(sorted_size, len(array)):
            if array[i] < array[min_value_index]:
                min_value_index = i
        array[sorted_size], array[min_value_index] = array[min_value_index], array[sorted_size]
    return array

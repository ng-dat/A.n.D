def sort(array):
    for sorted_size in range(len(array)):
        inserted_value = array[sorted_size]
        index_to_insert = sorted_size - 1
        while index_to_insert >= 0:
            if array[index_to_insert] > inserted_value:
                array[index_to_insert + 1] = array[index_to_insert]
            else:
                break
            index_to_insert -= 1
        index_to_insert += 1
        array[index_to_insert] = inserted_value
    return array

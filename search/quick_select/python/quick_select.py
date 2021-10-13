import random


def random_select(A, start, end, i):
    """
        Find the i-th smallest number in A from index start to index end.
        Time complexity: O(N) average
        Reference: "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. Introduction to Algorithms, 3rd Edition. MIT Press 2009. Chapter 9.2"
    :param A: Array of elements
    :param start
    :param end
    :param i
    :return:
        i-th smallest number
    """
    if start >= end:
        return A[end]
    pivot = randomized_partition(A, start, end)
    k = pivot - start + 1
    if k == i:
        return A[pivot]
    elif k > i:
        return random_select(A, start, pivot-1, i)
    return random_select(A, pivot+1, end, i-k)


def randomized_partition(A, start, end):
    """
        Partition the array while guaranteeing the randomness
    :param A: Array of elements
    :param start
    :param end
    :return:
        The pivot
    """
    if start < end:
        pivot = int(random.uniform(start, end))
        swap(A, pivot, end)
        return partition(A, start, end)
    return end


def partition(A, start, end):
    """
            Partition elements of a from start to end so that there is a position "pivot", and every element in the left of pivot is smaller than it while the rest is greater than or equal to it.
    :param A: Array of elements
    :param start:
    :param end:
    :return:
            The pivot
    """
    pivot_value = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] < pivot_value:
            i += 1
            swap(A, i, j)
    swap(A, i+1, end)
    return i+1


def swap(A, x, y):
    """
        Swap 2 elements in position x and y in A
    :param A: The array of elements
    :param x:
    :param y:
    :return:
        None
    """
    t = A[x]
    A[x] = A[y]
    A[y] = t

from random import random

a = [int(30 * random()) for i in range(30)]

def bubblesort(a):
    """Sort the list a to a assend order
    
    >>> bubblesort([2, 1, 4])
    [1, 2, 4]
    >>> bubblesort([1])
    [1]
    """

    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
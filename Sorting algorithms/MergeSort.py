def MergeSort(a):
    """
    The implementation of merge sort algorithm
    
    >>> MergeSort([2, 4, 1, 7, 3, 4])
    [1, 2, 3, 4, 4, 7]"""
    n = len(a)
    if n == 0 or n == 1:
        return a
    left, right = a[:n // 2], a[n // 2:]
    # print(left, right)
    return merge(MergeSort(left), MergeSort(right))

def merge(a, b):
    """
    The merge operation assums that a and b are sorted lists, 
    and the goal is to merge this two lists into one sorted list
    
    >>> merge([1, 4, 6], [2, 3, 4])
    [1, 2, 3, 4, 4, 6]
    >>> merge([0], [1])
    [0, 1]
    >>> merge([2], [1, 4, 7])
    [1, 2, 4, 7]"""
    m, n = len(a), len(b)
    result = []
    passed = 0
    for i in range(len(a)):
        for j in range(passed, len(b)):
            if a[i] < b[j]:
                result.append(a[i])
                m -= 1
                if m == 0:
                    result = sum([b[j:]], result)
                    n = 0
                passed = j
                # print(result, m)
                break
            else:
                result.append(b[j])
                n -= 1
        if n == 0 and m != 0:
            result = sum([a[i:]], result)
            # print(result)
            break
    return result
            

        

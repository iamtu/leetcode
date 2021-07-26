def bs_recursive(A, item):
    if not A:
        return False
    if len(A) == 1:
        if A[0] == item:
            return True
        else:
            return False
    mid = len(A) // 2
    if item == A[mid]:
        return True
    elif item > A[mid]:
        return bs_recursive(A[mid:], item)
    else:
        return bs_recursive(A[:mid], item)

def bs(A, item):
    if not A:
        return -1
    N = len(A)
    i = 0; j = N-1
    while (i <= j):
        mid = (i+j) // 2
        if item == A[mid]:
            return mid
        elif item > A[mid]:
            i = mid+1
        else:
            j = mid-1
    return -1


if __name__ == '__main__':
    A = [1, 4, 5, 6, 10, 15, 18]
    item = 10
    idx = bs(A, item)
    print (idx)
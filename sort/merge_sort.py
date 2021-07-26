''' Merge sort
Work well with link-list
'''
def merge_sort(A):
    if len(A) == 1:
        return A
    N = len(A)
    left = merge_sort(A[:N/2])
    right = merge_sort(A[N/2:])
    b = combine(left, right)
    for i in range(N):
        A[i] = b[i]
    return b

def combine(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        while i < len(left):
            res.append(left[i])
            i += 1
    if j < len(right):
        while j < len(right):
            res.append(right[j])
            j += 1
    return res

if __name__ == '__main__':
    A =  [2, 5, 9, 4, 10]
    left  = [1]
    right = [2]
    # print (combine(left, right))
    B = merge_sort(A)
    print (B)
    print (A)
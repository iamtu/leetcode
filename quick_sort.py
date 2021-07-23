def quick_sort(A):
    if len(A) == 1:
        return A
    pivot = 0
    #partition based on pivot

    
    left = quick_sort(A[:pivot])
    right = quick_sort(A[pivot+1:])
    A = left + [A[pivot]] + right
    return A

if __name__ == '__main__':
    A =  [2, 5, 9, 4, 10]
    left  = [1]
    right = [2]
    # print (combine(left, right))
    B = quick_sort(A)
    print (B)
    print (A)
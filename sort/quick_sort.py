def quick_sort(A):
    if len(A) == 0:
        return []    
    x = A[0]
    pivot_idx = 0 #save index to swap
    for i in range(1, len(A)):
        if A[i] < x:
            pivot_idx += 1
            tmp = A[i]
            A[i] = A[pivot_idx]
            A[pivot_idx] = tmp
    A[0] = A[pivot_idx]
    A[pivot_idx] = x
    
    left = quick_sort(A[:pivot_idx])
    right = quick_sort(A[pivot_idx+1:])
    A = left + [A[pivot_idx]] + right
    return A

if __name__ == '__main__':
    A =  [2, 5, 9, 4, 10, 3]
    B = quick_sort(A)
    print (B)
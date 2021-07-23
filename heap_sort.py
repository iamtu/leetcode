def heapify(A, l, position):
    '''
    max-heapify array A with len l
    from wrong position
    '''
    # find the largest among postion/left_child/right_child
    left_child = 2*position+1
    right_child = 2*position+2

    largest = position
    if left_child < l and A[left_child] > A[position]:
        largest = left_child
    if right_child < l and A[right_child] > A[largest]:
        largest = right_child

    #if wrong position
    if largest != position:
        #exchange A[largest], A[position]
        x = A[largest]
        A[largest] = A[position]
        A[position] = x
        heapify(A, l, largest)
    return

def build_max_heap(A):
    N = len(A)
    for i in range(N/2, -1, -1):
        heapify(A, N, i)
    return

def heap_sort(A):
    build_max_heap(A)
    N = len(A)
    for i in range(N-1,-1,-1):
        #swap A[last] to A[0]
        x = A[i]
        A[i] = A[0]
        A[0] = x
        heapify(A, i, 0)


if __name__ == '__main__':
    A = [100, 4, 8, 7, 6, 5, 10, 30, 20]
    # heapify(A, 5, 0)
    print (A)
    heap_sort(A)
    print (A)

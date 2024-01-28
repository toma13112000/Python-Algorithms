def Parent(i):
    return i//2
def Left(i):
    return 2*i
def Right(i):
    return 2*i+1
def Min_heapify(A, heap_size, i):
    l = Left(i)
    r = Right(i)
    if l < heap_size and A[l] < A[i]:
        largest = l
    else: largest = i
    if r < heap_size and A[r] < A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        Min_heapify(A, heap_size, largest)
def Build_Max_Heap(A):
    heap_size = len(A)
    for i in range(heap_size//2-1, -1, -1):
        Min_heapify(A, heap_size, i)
def HeapSort(A):
    heap_size = len(A)
    Build_Max_Heap(A)
    for i in range(heap_size-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size - 1
        Min_heapify(A, i, 0)
A = [5,13,2,25,7,17,20,8,4] #Lesson Example
HeapSort(A)
print(A)
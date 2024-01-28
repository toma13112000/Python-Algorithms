import random
def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r],A[i+1]
    return i+1
def Randomized_Partition(A,p,r):
    i = random.randrange(p,r)
    A[r], A[i] = A[i], A[r]
    return Partition(A,p,r)
def Randomized_Quicksort(A,p,r):
    if p<r:
        q = Randomized_Partition(A, p, r)
        Randomized_Quicksort(A, p, q - 1)
        Randomized_Quicksort(A, q + 1, r)
A = [2,8,7,1,3,5,6]
print("Array before sorting : ", A)
n = len(A)
Randomized_Quicksort(A,0,n-1)
print("Sorted array : ",A)

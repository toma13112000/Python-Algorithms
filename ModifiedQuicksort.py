def Quicksort(A,p,r):
    if p<r:
        q = partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A, q + 1, r)
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r],A[i+1]
    return i+1
A = []
n = int(input('Enter amount of variables in array:'))
for i in range(n):
    i = str(i+1)
    print("Enter the " + i +" element", end=" ")
    A.append(int(input()))
Quicksort(A,0,n-1)
print('Sorted list: ', end='')
print(A)
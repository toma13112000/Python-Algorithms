def Counting_sort(A,B, k):
    C = [0]*(k+1)
    for i in range(0,k+1):
        C[i] = 0
    for j in range(0,n):
        C[A[j]] = C[A[j]]+1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    for j in range(n-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1
    for i in range(0,n):
        A[i] = B[i]
    B.clear()
    C.clear()
    return A
def Radix_Sort(A,d):
    for i in range(d):
        Counting_sort(A, B, k)
A = [2,5,3,0,2,3,0,3]
k = max(A)
n = len(A)
B = [0]*n
d = 1
Radix_Sort(A,d)
print(A)
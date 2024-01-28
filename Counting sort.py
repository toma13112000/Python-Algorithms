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
n = int(input())
A=[0]*n
for i in range(n):
    A[i] = int(input())
k = max(A)
n = len(A)
B = [0]*n
Counting_sort(A,B,k)
print(A)
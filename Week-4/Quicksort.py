import random

def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1

#Quicksort Function
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)

        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

#Generate one random array of size 10
A = [random.randint(1, 100) for _ in range(10)]

print("Original Array:", A)

#Apply quicksort
quicksort(A, 0, len(A) - 1)

print("Sorted Array: ", A)
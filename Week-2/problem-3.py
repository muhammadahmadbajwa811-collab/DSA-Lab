import random
import time


def RandomArray(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, 50000))
    return arr


def Merge(array, p, q, r):
    left = array[p : q + 1]
    right = array[q + 1 : r + 1]

    i = 0
    j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1


def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)


arr = RandomArray(30000)

start_time = time.time()
MergeSort(arr, 0, len(arr) - 1)
end_time = time.time()

runtime = end_time - start_time
print("Runtime of MergeSort is", runtime, "seconds")

file = open("SortedMergeSort.csv", "w")
for val in arr:
    file.write(str(val) + "\n")
file.close()
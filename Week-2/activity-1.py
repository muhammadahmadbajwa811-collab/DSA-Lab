import random
import time
import csv

def randomArray(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def InsertionSort(array, start, end):
    for i in range(start +1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def main():
    size = 1000

    A = randomArray(size)

    start_time = time.time()
    InsertionSort(A, 0, size - 1)
    end_time = time.time()

    elapsed = end_time - start_time
    print(f"InsertionSort took {elapsed: .4f} seconds to sort {size} integers. ")

    with open("SortedInsertionSort.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        for num in A:
            writer.writerow([num])

print("Sorted array saved to SortedInsertionSort.csv")

if __name__ == "__main__":
    main()
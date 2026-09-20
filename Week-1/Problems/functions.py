# Problem 1:
def SearchA(Arr, x):
    indices = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            indices.append(i)
    return indices


# Problem 2:
def SearchB(Arr, x):
    indices = []

    for i in range(len(Arr)):
        if Arr[i] == x:
            indices.append(i)
        elif Arr[i] > x:

            break

    return indices


# Problem 3:
def Minimum(Arr, starting, ending):
    min_index = starting

    for i in range(starting, ending + 1):
        if Arr[i] < Arr[min_index]:
            min_index = i

    return min_index


# Problem 4:
def Sort4(Arr):
    n = len(Arr)

    for i in range(n):
        min_index = Minimum(Arr, i, n - 1)

        Arr[i], Arr[min_index] = Arr[min_index], Arr[i]

    return Arr


# Problem 5:
def StringReverse(str, starting, ending):
    portion = str[starting:ending + 1]

    def reverse_helper(s):
        if len(s) <= 1:
            return s
 
        return s[-1] + reverse_helper(s[:-1])

    return reverse_helper(portion)


# Problem 6:
def SumIterative(number):
    number = abs(number)

    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total

def SumRecursive(number):
    number = abs(number)

    if number == 0:
        return 0
    
    return number % 10 + SumRecursive(number // 10)


# Problem 7:
def RowWiseSum(Mat):
    row_sums = []

    for row in Mat:
        row_sums.append(sum(row))

    return row_sums

def ColumnWiseSum(Mat):
    col_sums = [0] * len(Mat[0])

    for row in Mat:
        for j in range(len(row)):
            col_sums[j] += row[j]

    return col_sums


# Problem 8:
def SortedMerge(Arr1, Arr2):

    merged = []
    i = 0
    j = 0

    while i < len(Arr1) and j < len(Arr2):
        if Arr1[i] <= Arr2[j]:
            merged.append(Arr1[i])
            i += 1
        else:
            merged.append(Arr2[j])
            j += 1

    while i < len(Arr1):
        merged.append(Arr1[i])
        i += 1

    while j < len(Arr2):
        merged.append(Arr2[j])
        j += 1

    return merged


# Problem 9:
def PalindromRecursive(str):
    if len(str) <= 1:
        return True
    
    if str[0] != str[-1]:
        return False

    return PalindromRecursive(str[1:-1])


# Problem 10
def Sort10(Arr):
    Arr = Sort4(Arr[:])  

    for i in range(0, len(Arr) - 1, 2):
        Arr[i], Arr[i + 1] = Arr[i + 1], Arr[i]

    return Arr
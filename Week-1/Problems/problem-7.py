from functions import RowWiseSum, ColumnWiseSum

A = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]

print("Matrix:", A)
print("Row-wise:", RowWiseSum(A))
print("Column-wise:", ColumnWiseSum(A))
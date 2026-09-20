from functions import SumIterative, SumRecursive

number = int(input("Enter a number: "))
print("Sum of digits (iterative):", SumIterative(number))
print("Sum of digits (recursive):", SumRecursive(number))
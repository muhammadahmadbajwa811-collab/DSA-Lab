from functions import PalindromRecursive

word = input("Enter a string: ")
if PalindromRecursive(word):
    print("Palindrome")
else:
    print("Not a palindrome")
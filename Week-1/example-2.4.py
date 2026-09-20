def recur_factorial(num):
    if num < 0:
        return - 1
    elif num ==0 or num==1:
        return 1
    else:
        return num*recur_factorial(num-1)

num = int(input("Enter a number: "))

print("The factorial of", num, "is", recur_factorial(num))
    
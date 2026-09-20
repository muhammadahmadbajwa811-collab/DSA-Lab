given_file = open(file='test.txt', mode='r')
lines = given_file.read()

numbers = []

array = lines.split() 
for s in array:
    num = int(s) 
    numbers.append(num)

print(numbers)
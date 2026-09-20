array = ['Hello world', 'UET']

f = open (file='text.txt', mode='w')

for i in array:
    f.write(i + "\n")
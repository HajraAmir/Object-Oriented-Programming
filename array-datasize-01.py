arraySize = 100
a = [0]*arraySize

dataSize = 0
num = 1
while dataSize < arraySize and num > 0:
    num = int(input("Enter a number, 0 to quit"))
    if num > 0:
        a[dataSize] = num
        dataSize = dataSize + 1

sum = 0
i=0
while i<dataSize:
    sum = sum+a[i]
    i = i+1

print(sum, end=" is sum of ")

i=0
while i<dataSize:
    print(a[i], end=" ")
    i = i+1

a = [1, 2, 3, 4, 5]
noOfRotation = 500000
for x in range(noOfRotation):
    temp = a[0]
    for index, item in enumerate(a):
        if index+1 < len(a):
            a[index] = a[index+1]
        if len(a) - 1 == index:
            a[index] = temp
print(a)

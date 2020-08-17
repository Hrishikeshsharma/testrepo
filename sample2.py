a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]
noOfRotation = 1000
totalElements = len(a)
position = (totalElements - noOfRotation) % totalElements
j = 0
p = -1
for i in range(totalElements):
    if (position + j) < totalElements:
        b[position + j] = a[i]
        j = j + 1
    else:
        p += 1
        b[p] = a[i]
print(b)

def solution (a,k):
    arraySize = len(a)
    newArray = [None] * arraySize
    for i in range(arraySize):
        newArray[(i+k)%arraySize] = a[i]
    return newArray
print(solution([1,2,3,4,5],3))

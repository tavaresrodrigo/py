arr = [1,2,3,-5,6,-7,8,9,]
def maxSum(arr, windowSize):
    arraySize = len(arr)
    if arraySize <= windowSize:
        print("Array Window is bigger or equal to array size")
        return -1
    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum
    for i in range(arraySize-windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(window_sum, max_sum)
    return max_sum
answer = maxSum(arr, 3)
print(answer)



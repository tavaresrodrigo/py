def binarySearch (array, target):
    left = 0 
    right = len(array) -1 
    while left <= right:
        mid = (left + right)//2
        if (array[mid] == target):
            return mid
        elif (array[mid] < target):
            left = mid+1
        else:
            right = mid-1
    return -1

array = [1,2,3,4,5]
target = 4
result = binarySearch(array,target)

if result == -1:
    print (f'Element {target} is not present in the array.')
else:
    print(f'The element {target} was found at the index {result} ')

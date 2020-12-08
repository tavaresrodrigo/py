import numpy as np
# Painless algorithm using numpy

def solutionM(x):
    sar = np.sum(x)
    esar = np.sum(np.arange(1,len(x)+2,1))-sar
    if esar >= 1:
        return int(esar)
    else:
        return None 

# Painless algorithm using only Python standard library
def solution(x):
    actual_sum = 0
    for i in x:
        actual_sum += i
    max_number = len(x) +1
    expected_sum = (max_number * (max_number+1)//2)
    return expected_sum - actual_sum 




print (solutionM([2,3,1,5,4,9,8,6,7,11,12,13,14,15,16,26,17,10,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,39]))
print (solution([2,3,1,5,4,9,8,6,7,11,12,13,14,15,16,26,17,10,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,39]))
print (solutionM([]))
print (solution([]))
print (solutionM([1,2,3,4]))
print (solution([1,2,3,4,]))

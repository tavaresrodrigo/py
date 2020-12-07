import numpy as np
# Quadratic algorithm - O(n²)
def solutionF(x):
    oar = np.sort(x)
    for i in range(1,len((oar)+1),1):
        if i+1 != oar[i]:
            return(i+1)
            break

# Painless algorithm using numpy

def solutionS(x):
    sar = np.sum(x)
    esar = np.sum(np.arange(1,len(x)+2,1))-sar
    if esar >1:
        return esar
    else:
        return None 

# Painless algorithm using only Python standard library

print (solutionF([2,3,1,5,4,9,8,6,7,11,12,13,14,15,16,26,17,10,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,39]))
print (solutionS([2,3,1,5,4,9,8,6,7,11,12,13,14,15,16,26,17,10,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,39]))
print (solutionF([]))
print (solutionS([]))
print (solutionF([1,2,3,4,5,6,7,8,9]))
print (solutionS([1,2,3,4,5,6,7,8,9]))

import sys

## grabbing the input from the sys.argv
def abs_sum (*args):
    listValue = [item for item in args]
    sumAbs = 0
    for n in sys.argv[1:]:
        sumAbs += abs(int(n))
    return sumAbs
    
print(abs_sum())

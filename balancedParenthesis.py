
'''
In every iteration, the innermost elements get eliminated (replaced with empty string in line 10). If we end up with an empty string, the initial one was balanced; otherwise, not.
'''

def checkP(inputString):
    elements = ['()', '{}', '[]']
    while any(x in inputString for x in elements):
        for br in elements:
            inputString = inputString.replace(br, '')
    return not inputString
        
string = "{[]{(())}}"
print(string, "-", "Yes" 
      if checkP(string) else "No") 
s = input ("Write the word to check: ")
def isPalindrome (s):
    isP = "Yes"
    palindromeS = s[::-1]
    if palindromeS != s:
        isP = "No"
    return isP
print(isPalindrome(s))

a=raw_input('enter the values of first  matrix')
def reverse(s):
    return s[::-1]
print(reverse(a))

def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False
print (isPalindrome(a))


def isPalindrome(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return isPalindrome(s, start + 1, end - 1)

s = input()
if isPalindrome(s, 0, len(s) - 1):
    print("Yes")
else:
    print("No")

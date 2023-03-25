def palindromeString(s) -> bool:
    n = len(s)
    for i in range(int(n / 2)):
        if s[i] != s[n - 1 - i]:
            return False
    return True


ans = palindromeString("ac")
if ans:
    print("yes")
else:
    print("no")

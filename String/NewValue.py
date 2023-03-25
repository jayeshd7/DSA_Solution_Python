def newValue(s, n):
    ans = ""
    lengthOfString = len(s)
    for i in range(0, lengthOfString):
        if "a" <= s[i] <= "z":
            ans = ans + chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))
        elif "A" <= s[i] <= "Z":
            ans = ans + chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))

    print(ans)


newValue(s="XYz", n=1)

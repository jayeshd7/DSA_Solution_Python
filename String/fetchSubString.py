def subString(s):
    n = len(s)
    ans = ""
    k = 0
    dic = {}
    for i in range(k, len(s)):
        for j in range(i + 1, len(s)):
            if ord(s[j]) < ord(s[i]):
                k = k + 1
                break
            else:
                if s[i] in ans:
                    ans = ans
                else:
                    dic[s[i]] = 1
                    dic[s[j]] = 1
                    if s[i] in dic:
                        dic[s[i]] = dic.get(s[i]) + 1
                    if s[j] in dic:
                        dic[s[j]] = dic.get(s[j]) + 1
                    ans = ans + s[i] + s[j]

    print(ans)


s = subString("sbccccabcxsjbkbmnoxsaxyz")

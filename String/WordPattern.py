class WordPattern:
    def wordPatternConcept(self, pattern, s):
        dic = {}
        seen = set()
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in dic:
                if s[i] in seen:
                    return False
                dic[pattern[i]] = s[i]
                seen.add(s[i])
            else:
                if dic[pattern[i]] != s[i]:
                    return False
        return True


if __name__ == "__main__":
    w = WordPattern
    print(w.wordPatternConcept(w, pattern="abba", s="dog cat cat dog"))

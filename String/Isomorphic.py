class Isomorphic:
    def solution(self, s, t) -> bool:
        forward = {}
        backward = {}

        for i in range(len(s)):
            a, b = s[i], t[i]
            if a in forward:
                if forward[a] == b:
                    continue
                else:
                    False
            else:
                forward[a] = b
                if b in backward:
                    if backward[b] != a:
                        return False
                else:
                    backward[b] = a
        return True

    def solution2(self, s, t) -> bool:
        d = {}
        s_d = ""
        if len(set(s)) != len(set(t)):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in d:
                    d[s[i]] = t[i]
                s_d += d[s[i]]

            return s_d == t


if __name__ == "__main__":
    i = Isomorphic
    print(i.solution(i, s="egg", t="add"))
    print(i.solution2(i, s="egg", t="ada"))

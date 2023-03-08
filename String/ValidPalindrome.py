


class ValidPalindrome:

    @staticmethod
    def expandFromMid(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

    def solution(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.expandFromMid(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.expandFromMid(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res



if __name__ == "__main__":
    vp = ValidPalindrome
    print(vp.solution(vp, "babacd"))

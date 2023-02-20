class ValidParenthess:
    def isValid(self, s) -> bool:
        dict = {")": "(", "}": "{", "]": "["}
        st = []
        for c in s:
            if len(st) == 0 or not c in dict.keys():
                st.append(c)
            elif dict.get(c) == st[-1]:
                st.pop()
            else:
                st.append(c)
        return len(st) == 0


if __name__ == "__main__":
    v = ValidParenthess
    print(v.isValid(v, "[}"))

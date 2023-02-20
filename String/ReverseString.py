class ReverseString:
    def solution(self, s):
        current_Str = [char for char in s]
        i = 0
        j = len(s) - 1
        while i < j:
            temp = current_Str[i]
            current_Str[i] = current_Str[j]
            current_Str[j] = temp
            i += 1
            j -= 1
        return "".join(current_Str)


if __name__ == "__main__":
    r = ReverseString
    print(r.solution(r, "jayesh is my name"))

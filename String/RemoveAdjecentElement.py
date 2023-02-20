
class RemoveAdjecentElement:

    def solution(self, s):
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

if __name__ == '__main__':
    r = RemoveAdjecentElement
    print(r.solution(r, "ABCCBCBA"))

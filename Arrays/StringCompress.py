from typing import List


class StringCompress:
    def stringCompressSolution(self, chars: List[str]) -> int:
        total = len(chars)
        count = 1
        s = ""
        s += chars[0]
        for i in range(1, total):
            curr = chars[i]
            prev = chars[i - 1]
            if curr != prev:
                if count > 1:
                    s += str(count)
                    count = 1
                s += curr

            else:
                count = count + 1

        if count > 1:
            s += str(count)
        return len(s)


if __name__ == "__main__":
    s = StringCompress
    print(s.stringCompressSolution(s, ["a", "a", "b", "b", "c", "c", "c"]))

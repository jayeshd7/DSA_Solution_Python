"""

S = “My Name is Jayesh”
Op = “Jayesh is Name My”

list = ["My", "name" , ]

reverse list = []


"""


class revereseString:
    def reverseStringSol(self, s):
        l1 = []
        s1 = ""
        for i in range(len(s)):
            l1 = s.split(" ")
        l1.reverse()
        for i in range(len(l1)):
            s1 += str(l1[i]) + " "
        print(s1.rstrip(" "))
        return s1


if __name__ == "__main__":
    r = revereseString
    r.reverseStringSol(r, "My Name is Jayesh")

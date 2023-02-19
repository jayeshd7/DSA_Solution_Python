class ValidAnagram:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False


if __name__ == "__main__":
    v = ValidAnagram
    print(v.isAnagram(v, s="tac", t="cat"))

class isPalindrome:
    def palindrome(self, s: str) -> bool:
        a = ""
        for i in s:
            if i.isalnum():
                a += i.lower()
        if a == a[::-1]:
            return True
        return False


if __name__ == "__main__":
    p = isPalindrome
    print(p.palindrome(p, "race a car"))

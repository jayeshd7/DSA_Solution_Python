
def partitonString(s:str)->int:
    last_pos = [0] * 26
    partition = 0
    last_end = 0

    for i in range(len(s)):
        if last_pos[ord(s[i]) -ord('a')] >= last_end:
            partition += 1
            last_end = i+1
        last_pos[ord(s[i]) -ord('a')] = i+1
    return partition



print(partitonString(s = "abacaba"))

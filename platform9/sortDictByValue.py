class sortDictByValue:
    def sortDictByValueSol(self, d):
        print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})


if __name__ == "__main__":
    s = sortDictByValue
    print(s.sortDictByValueSol(s, d={"jayesh": 33, "piyush": 35, "pooja": 31}))

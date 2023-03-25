class PythonClassConcept:
    def __int__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return PythonClassConcept(self.x + other.x + self.y + other.y)


if __name__ == "__main__":
    v1 = PythonClassConcept
    v1.__add__(1, 2)
    v2 = PythonClassConcept
    v2.__add__(2, 3)
    v3 = v1 + v2

    print(v3.x + v3.y)

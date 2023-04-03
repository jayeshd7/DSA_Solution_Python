
'''
class method
'''

import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age)


person = Person.from_birth_year("jayesh", 1991)
print(f"person name {person.name} and there age is: {person.age}")

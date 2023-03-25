class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.__email = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str) -> None:
        self.__email = new_email


c = Customer(name="jayesh", email="jayesh@gmail.com")

print(f"customer name is {c.name} and email is {c.email}")

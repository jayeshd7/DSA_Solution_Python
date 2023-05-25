import re


class DataValidator:
    @staticmethod
    def is_valid_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        else:
            return False


email_address = "jayeshdalal7@gmail.com"

print(DataValidator.is_valid_email(email_address))

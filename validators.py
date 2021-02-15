import re


class EmailValidator:
    def __init__(self, regex=r'^[a-z0-9]+([\._]?[a-z0-9])+[@]+(\w+[.])+\w{2,3}$'):
        self.regex = regex

    def validate(self, email_address: str) -> bool:
        """validates an email address"""
        return True if re.search(self.regex, email_address) else False


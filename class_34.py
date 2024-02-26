class PhoneNumber:

    def __init__(self, phone_number) -> None:
        if ' ' in phone_number:
            no_space = phone_number.replace(' ', '')
            self.phone_number = no_space
        else:
            self.phone_number = phone_number

    def __str__(self) -> str:
        return '(' + self.phone_number[:3] + ') ' + self.phone_number[3:6] + '-' + self.phone_number[6:]

    def __repr__(self) -> str:

        return (f"PhoneNumber('{self.phone_number}')")


phone = PhoneNumber('9173963385')

print(str(phone))
print(repr(phone))

phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))

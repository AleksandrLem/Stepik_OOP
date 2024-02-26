class Validator:

    def __init__(self, obj) -> None:
        self.obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):

    def __init__(self, obj) -> None:
        super().__init__(obj)

    def is_valid(self):
        if isinstance(self.obj, (int, float)):
            return True
        else:
            return False


print(issubclass(NumberValidator, Validator))

validator1 = Validator('beegeek')
validator2 = Validator(1)
validator3 = Validator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

validator1 = NumberValidator('beegeek')
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

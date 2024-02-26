

class Calculator:

    def __call__(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/' and b != 0:
            return a / b
        elif operation == '/' and b == 0:
            return 'Деление на ноль невозможно'


calculator = Calculator()

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 2, '/'))

# Решение преподавателя


class Calculator:
    def __call__(self, a, b, operation):
        if operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        return eval(f'{a}{operation}{b}')

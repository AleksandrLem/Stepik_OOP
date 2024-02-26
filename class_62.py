# Реализуйте класс User, описывающий пользователя некоторого
# интернет-ресурса. При создании экземпляра класс должен принимать один аргумент:

# name — имя пользователя
# Класс User должен иметь один метод экземпляра:

# skip_ads() — метод, всегда возвращающий False
# Также реализуйте класс PremiumUser, наследника класса User,
# описывающий пользователя некоторого интернет-ресурса с
# премиум подпиской. Процесс создания экземпляра класса PremiumUser
# должен совпадать с процессом создания экземпляра класса User.

# Класс PremiumUser должен иметь один метод экземпляра:

# skip_ads() — метод, всегда возвращающий True


class User:

    def __init__(self, name) -> None:
        self.name = name

    def skip_ads(self):
        return False


class PremiumUser(User):
    def __init__(self, name) -> None:
        super().__init__(name)

    def skip_ads(self):
        return True


print(issubclass(PremiumUser, User))

user = User('Arthur')
premium_user = PremiumUser('Arthur')

print(user.skip_ads())
print(premium_user.skip_ads())

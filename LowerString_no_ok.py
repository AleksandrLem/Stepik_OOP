class LowerString(str):

    def __new__(cls, obj=''):
        instance = super().__new__(cls, obj).lower()
        # instance = str(instance.lower())
        return instance


print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))

s = LowerString('BeeGeek')

print(s[0], s[3])


s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))

print(LowerString())

lowerstring = LowerString()
print(type(lowerstring))

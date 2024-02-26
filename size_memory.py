import sys

print(sys.getsizeof(list(range(10000))))
print(sys.getsizeof(range(10000)))
print(sys.getsizeof('b' * 10000))
print(sys.getsizeof(tuple(range(10000))))

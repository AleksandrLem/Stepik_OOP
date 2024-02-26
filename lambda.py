def k(x): return x > 5


numbers = [13, 1, 4, 10, 10, 7]
itog_list = []
for i in numbers:
    if k(i) == True:
        itog_list.append(i)

print(itog_list)

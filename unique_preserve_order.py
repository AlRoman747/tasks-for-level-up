from collections.abc import Iterable
from random import choice
#тест на числах, но если потребуется, могу написать для генирации тестов числа + строки
lst = []
while len(lst) < 100:
    lst.append(choice(range(0,100)))

print(lst, len(lst), sep='\n')

def unique_preserve_order(iterable):
    res = []
    if not(isinstance(iterable, Iterable)):
        return "ERR0R"

    for i in iterable:
        if i in res:
            continue
        res.append(i)

    return res
k = unique_preserve_order(lst)
print(k, len(k), sep='\n')


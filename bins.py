#Бинарный поиск с возратом индекса

import random

a = sorted(set([random.randint(1, 20) for i in range(15)]))

def bsi(lst, fs, fn, x):
    if fs == fn:
        return None
    else:
        mid = int((fs + fn) / 2)
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return bsi(lst, fs, mid, x)
        else:
            return bsi(lst, mid + 1, fn, x)

print(a)
print(bsi(a, 0, len(a), x))

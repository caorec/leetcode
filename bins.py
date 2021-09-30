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

def bs(lst, x):
    if not lst:
        return False
    else:
        if lst[int(len(lst) / 2)] == x:
            return True
        elif lst[int(len(lst) / 2)] > x:
            return bs(lst[:int(len(lst) / 2)], x)
        else:
            return bs(lst[int(len(lst) / 2) + 1:], x)

list = [1, 4, 6, 8, 9, 14, 39]
x = 9

print(a)
print(bsi(a, 0, len(a), x))

#test

import math


def binarySearch(a, l, r, x):
    length = len(a)

    if r >= l:
        mid = math.ceil(l + (r - l) / 2)

        if a[mid] == x:
            return mid

        if x <= a[0]:
            return 0
        elif x >= a[length - 2]:
            return length - 1

        if a[mid] <= x <= a[mid + 1]:
            return mid + 1

        elif a[mid] > x:
            return binarySearch(a, l, mid - 1, x)
        else:
            return binarySearch(a, mid + 1, r, x)

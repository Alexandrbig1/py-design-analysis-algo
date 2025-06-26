from random import randint


def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[randint(0, len(arr) - 1)]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quick_select(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quick_select(right, k - len(left) - len(mid))


arr1 = [5, 3, 8, 4, 2, 7, 1, 6]
arr2 = [11, 3, 15, 7, 9, 2, 8, 12, 4, 10, 6, 5, 1, 14]

k = 4
print(quick_select(arr1, k))

k = 1
print(quick_select(arr2, k))
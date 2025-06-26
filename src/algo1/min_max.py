def find_min_max(arr):
    def divide_and_conquer(left, right):
        if left == right:
            return arr[left], arr[left]

        if right - left == 1:
            return (min(arr[left], arr[right]), max(arr[left], arr[right]))

        mid = (left + right) // 2
        left_min, left_max = divide_and_conquer(left, mid)
        right_min, right_max = divide_and_conquer(mid + 1, right)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        raise ValueError("Array cannot be empty")

    return divide_and_conquer(0, len(arr) - 1)


arr = [14, 22, 1, 4, 15, 38, 3, 7, 12, 10, 5, 6, 8, 9, 11, 13, 2, 0]
print(find_min_max(arr))
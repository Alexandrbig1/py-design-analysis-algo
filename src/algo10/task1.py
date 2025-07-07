import random
import time
import numpy as np
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибір опорного елемента (середній елемент)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)


def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    random.seed(42)

    results = {
        "Randomized QuickSort": [],
        "Deterministic QuickSort": []
    }

    for size in sizes:
        arr = [random.randint(0, 1_000_000) for _ in range(size)]
        rand_time = measure_time(randomized_quick_sort, arr)
        det_time = measure_time(deterministic_quick_sort, arr)
        results["Randomized QuickSort"].append(rand_time)
        results["Deterministic QuickSort"].append(det_time)
        print(f"Array size: {size}")
        print(f"   Randomized QuickSort: {rand_time:.4f} seconds")
        print(f"   Deterministic QuickSort: {det_time:.4f} seconds")

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, results["Randomized QuickSort"], marker='o', label='Randomized QuickSort')
    plt.plot(sizes, results["Deterministic QuickSort"], marker='s', label='Deterministic QuickSort')
    plt.xlabel("Array size")
    plt.ylabel("Average time (sec)")
    plt.legend()
    plt.title("Comparison of Randomized and Deterministic QuickSort")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
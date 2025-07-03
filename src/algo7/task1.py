import random
import time
from functools import lru_cache

def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value

@lru_cache(maxsize=1000)
def range_sum_with_cache_tuple(array_tuple, L, R):
    return sum(array_tuple[L:R+1])

def range_sum_with_cache(array, L, R):
    return range_sum_with_cache_tuple(tuple(array), L, R)

def update_with_cache(array, index, value):
    array[index] = value
    range_sum_with_cache_tuple.cache_clear()

N = 100_000
Q = 50_000
array = [random.randint(1, 1000) for _ in range(N)]
queries = [(random.choice(['Range', 'Update']), random.randint(0, N-1), random.randint(0, N-1)) for _ in range(Q)]

queries = [(q[0], q[1], random.randint(1, 1000)) if q[0] == 'Update' else (q[0], min(q[1], q[2]), max(q[1], q[2])) for q in queries]

start = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_no_cache(array, query[1], query[2])
    else:
        update_no_cache(array, query[1], query[2])
time_no_cache = time.time() - start

start = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_with_cache(array, query[1], query[2])
    else:
        update_with_cache(array, query[1], query[2])
time_with_cache = time.time() - start

print(f"Execution time without caching: {time_no_cache:.2f} seconds")
print(f"Execution time with LRU cache: {time_with_cache:.2f} seconds")
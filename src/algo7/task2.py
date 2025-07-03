import timeit
import functools
import matplotlib.pyplot as plt
from prettytable import PrettyTable


@functools.lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


class SplayNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._rotate_right(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._rotate_left(root.left)
            return self._rotate_right(root) if root.left else root
        else:
            if root.right is None:
                return root
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._rotate_left(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._rotate_right(root.right)
            return self._rotate_left(root) if root.right else root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def insert(self, key, value):
        if self.root is None:
            self.root = SplayNode(key, value)
            return
        self.root = self._splay(self.root, key)
        if key == self.root.key:
            return
        new_node = SplayNode(key, value)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root.value if self.root and self.root.key == key else None


def fibonacci_splay(n, tree):
    if n < 2:
        return n
    stored = tree.search(n)
    if stored is not None:
        return stored
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


n_values = list(range(0, 951, 50))
lru_times = []
splay_times = []

for n in n_values:
    tree = SplayTree()

    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=5) / 5
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=5) / 5

    lru_times.append(lru_time)
    splay_times.append(splay_time)


table = PrettyTable()
table.field_names = ["n", "LRU Cache Time (s)", "Splay Tree Time (s)"]
for i in range(len(n_values)):
    table.add_row([n_values[i], f"{lru_times[i]:.9f}", f"{splay_times[i]:.9f}"])
print(table)

plt.figure(figsize=(10, 6))
plt.plot(n_values, lru_times, marker='o', linestyle='-', label='LRU Cache')
plt.plot(n_values, splay_times, marker='x', linestyle='-', label='Splay Tree')
plt.xlabel("Fibonacci Number (n)")
plt.ylabel("Average Execution Time (seconds)")
plt.title("Execution Time Comparison for LRU Cache and Splay Tree")
plt.legend()
plt.grid()
plt.show()
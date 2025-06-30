import csv
import timeit
from BTrees.OOBTree import OOBTree


def load_data(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['ID'] = int(row['ID'])
            row['Price'] = float(row['Price'])
            data.append(row)
    return data

def add_item_to_tree(tree, item):
    tree[item['ID']] = {'Name': item['Name'], 'Category': item['Category'], 'Price': item['Price']}

def add_item_to_dict(dictionary, item):
    dictionary[item['ID']] = {'Name': item['Name'], 'Category': item['Category'], 'Price': item['Price']}

def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item['Price'] <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]

data = load_data('generated_items_data.csv')

tree = OOBTree()
dictionary = {}

for item in data:
    add_item_to_tree(tree, item)
    add_item_to_dict(dictionary, item)

min_price, max_price = 10.0, 50.0

range_query_tree_time = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)
range_query_dict_time = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)

print(f"Total range_query time for OOBTree: {range_query_tree_time:.6f} seconds")
print(f"Total range_query time for Dict: {range_query_dict_time:.6f} seconds")
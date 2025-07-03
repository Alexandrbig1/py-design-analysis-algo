import string
import requests
import asyncio
from collections import defaultdict, Counter
from matplotlib import pyplot as plt

def get_text(url):
    """Fetch text content from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Requests error: {e}")
        return None

def map_function(text):
    """Map words to key-value pairs."""
    if text is None:
        return []
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return [(word.lower(), 1) for word in words]

def shuffle_function(mapped_values):
    """Group values by keys."""
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(key_values):
    """Reduce grouped values to their sum."""
    key, values = key_values
    return key, sum(values)

async def map_reduce(url):
    """Perform the MapReduce operation."""
    text = get_text(url)
    if text is None:
        return {}
    mapped_result = map_function(text)
    shuffled_words = shuffle_function(mapped_result)
    reduced_result = [reduce_function(values) for values in shuffled_words]
    return dict(reduced_result)

def visualize_top_words(result, top_n=10):
    """Visualize the top N most frequent words."""
    top_words = Counter(result).most_common(top_n)
    words, counts = zip(*top_words)
    plt.figure(figsize=(12, 9))
    plt.barh(words, counts, color="skyblue")
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title("Top 10 Most Frequent Words")
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == '__main__':
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    res = asyncio.run(map_reduce(url))
    if res:
        visualize_top_words(res)
    else:
        print("Failed to process the URL.")
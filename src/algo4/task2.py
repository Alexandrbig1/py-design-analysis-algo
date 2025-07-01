from trie import Trie

class LongestCommonWord(Trie):
    def __init__(self):
        super().__init__()

    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        for word in strings:
            self.put(word)

        common_prefix = ""
        current_node = self.root
        while len(current_node.children) == 1 and current_node.value is None:
            char, next_node = next(iter(current_node.children.items()))
            common_prefix += char
            current_node = next_node

        return common_prefix

if __name__ == "__main__":
    # Tests
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")
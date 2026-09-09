class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True


    def search(self, word: str) -> bool:
        def dfs(i, curr):
            if i == len(word):
                return curr.is_end
            char = word[i]

            if char != ".":
                if char not in curr.children:
                    return False
                return dfs(i+1, curr.children[char])
            
            else: 
                for child in curr.children.values():
                    # for each children of ".", "would rest of word match if go this path"
                    if dfs(i+1, child):
                        return True
                  # if none match
                return False
        return dfs(0, self.root)












class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()            
            curr = curr.children[char]
        curr.IsEnd = True

        

    def search(self, word: str) -> bool:
        def dfs(root, word):
            curr = root
            for i,char in enumerate(word):
                if char == ".":
                    for child in curr.children.values():
                        if dfs(child,word[i+1:]):
                            return True
                    return False                       
                if char not in curr.children:
                    return False
                curr = curr.children[char]
            return curr.IsEnd
        return dfs(self.root,word)
                
                

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
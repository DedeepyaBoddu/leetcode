class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur = cur.children[char]
        cur.IsEnd = True
        

    def search(self, word: str) -> bool:
        def dfs(root,word):
            cur = root
            for i,char in enumerate(word):
                if char == '.':
                    for j in cur.children:
                        if dfs(cur.children[j], word[i+1:]):
                            return True
                    return False
                elif char in cur.children:
                    cur = cur.children[char]
                else:
                    return False
            return cur.IsEnd
        return dfs(self.root,word)
                        

                
                    

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
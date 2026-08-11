class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.end = True
        
    def dfs(self,i,cur,word) -> bool:
            if i == len(word):
                return cur.end

            if word[i] == ".":
                for child in cur.children:
                    if self.dfs(i+1,cur.children[child],word):
                        return True
                return False

            if word[i] not in cur.children:
                return False
            else:
                return self.dfs(i+1, cur.children[word[i]],word)

    def search(self, word: str) -> bool:
        return self.dfs(0,self.root,word)
        
        

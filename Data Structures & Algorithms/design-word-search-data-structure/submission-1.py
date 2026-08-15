class Node:
    
    def __init__(self, val=None):
        self.val = val
        self.children = [None]*26
        self.end = False
    
    # Returns optional node, None or node
    def getChildFromChar(self,char):
        return self.children[ord(char)-ord('a')]
        
    
    def addChildFromChar(self,char):
        if not self.getChildFromChar(char):
            self.children[ord(char)-ord('a')] = Node(char)
        return self.getChildFromChar(char)


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            cur = cur.addChildFromChar(char)

        cur.end = True
    
    

    def search(self, word: str) -> bool:
        # Word up to idx i (not including) has been processed
        # cur = node to search from
        # means cur.val = word[i-1]
        def dfs(cur, i):
            if i == len(word):
                return cur.end

            char = word[i]

            if char == ".":
                for child in cur.children:
                    if child and dfs(child, i+1):
                        return True
                return False

            else:
                child = cur.getChildFromChar(char)
                if child:
                    return dfs(child, i+1)
                else:
                    return False
            
        return dfs(self.root,0)


        

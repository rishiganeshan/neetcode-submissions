from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        charToParent = defaultdict(set)
        charToNumDependencies = defaultdict(int)

        uniq = set()

        def addToGraph(smallWord, bigWord):
            
            if smallWord == bigWord:
                return True
            if len(bigWord) < len(smallWord) and smallWord.startswith(bigWord):
                return False
            

            for i in range(min(len(smallWord),len(bigWord))):
                if smallWord[i] != bigWord[i]:
                    if bigWord[i] not in charToParent[smallWord[i]]:
                        charToParent[smallWord[i]].add(bigWord[i])
                        charToNumDependencies[bigWord[i]] += 1
                    return True
            return True


        for i in range(len(words)):
            for char in words[i]:
                uniq.add(char)
            for j in range(i):
                if not addToGraph(words[j],words[i]):
                    return ""

        q = deque()
        for char in uniq:
            if not charToNumDependencies[char]:
                q.append(char)
        ans = []
        # if len(q) > 1:
        #     return ""
        print(charToNumDependencies)
        print(q)
        while q:
            cur = q.popleft()
            ans.append(cur)
            for parent in charToParent[cur]:
                charToNumDependencies[parent] -= 1
                if not charToNumDependencies[parent]:
                    q.append(parent)

        print(charToParent)
        
        print(ans)
        
        return ''.join(ans) if len(ans) == len(uniq) else ""




        
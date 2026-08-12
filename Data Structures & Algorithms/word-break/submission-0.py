from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i] reflects if s[i:] can work

        
        """

        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        successful_indices = set([len(s)])


        words = defaultdict(list)
        for word in wordDict:
            words[word[0]].append(word)

        for i in range(len(s)-1,-1,-1):
            for word in words[s[i]]:
                if i+len(word) in successful_indices and word == s[i:i+len(word)]:
                    dp[i] = True
                    successful_indices.add(i)
                    break
        
        return dp[0]
                
        
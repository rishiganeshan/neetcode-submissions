from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def vectorise(s):
            vector = [0] * 26
            for char in s:
                vector[ord(char)-ord('a')] += 1
            return tuple(vector)

        output = defaultdict(list)

        for s in strs:
            output[vectorise(s)].append(s)

        return list(output.values())


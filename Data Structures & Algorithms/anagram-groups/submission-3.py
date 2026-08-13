class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            counter = [0] * 26

            for char in s:
                counter[ord(char)-ord('a')] += 1
            
            counter = tuple(counter)
            if counter in groups:
                groups[counter].append(s)
            else:
                groups[counter] = [s]
        
        return list(groups.values())





        
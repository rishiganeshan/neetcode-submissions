class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def vectorise(s):
            lst = [0] * 26
            for char in s:
                lst[ord(char)-ord('a')] += 1
            return tuple(lst)

        count_to_str = {}

        for s in strs:
            v = vectorise(s)
            count_to_str[v] = count_to_str.get(v,[]) + [s]


        return list(count_to_str.values())
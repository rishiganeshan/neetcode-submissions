class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def convertToTuple(s: str) -> Tuple[int]:
            counter = [0]*26
            for char in s:
                counter[ord(char)-ord('a')] += 1
            return tuple(counter)

        res = {}

        for s in strs:
            tup = convertToTuple(s)
            res[tup] = res.get(tup,[]) + [s]

        return list(res.values())
        
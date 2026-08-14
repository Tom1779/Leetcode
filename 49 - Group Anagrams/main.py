class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sort = ["".join(sorted(s)) for s in strs]

        anagrams = {}

        for s in range(len(strs_sort)):
            if strs_sort[s] in anagrams:
                anagrams[strs_sort[s]].append(s)
            else:
                anagrams[strs_sort[s]] = [s]

        GA = []
        for k in anagrams:
            cur = []
            for i in anagrams[k]:
                cur.append(strs[i])
            GA.append(cur)

        return GA


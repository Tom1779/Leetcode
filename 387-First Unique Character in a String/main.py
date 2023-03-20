class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for letter in range(len(s)):
            if not s[letter] in char_dict.keys():
                char_dict[s[letter]] = [1,letter]
            else:
                char_dict[s[letter]][0] += 1
                
        for v in char_dict.values():
            if v[0] == 1:
                return v[1]
            
        return -1
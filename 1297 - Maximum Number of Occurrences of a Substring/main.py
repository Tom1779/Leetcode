class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = 0
        sub_occ = dict()

        while(i+minSize<=len(s)):
            if not s[i:i+minSize] in sub_occ:
                sub_occ[s[i:i+minSize]] = 1
            else:
                sub_occ[s[i:i+minSize]] += 1
            i+=1

        sub_occ = dict(sorted(sub_occ.items(), key=lambda item: item[1], reverse=True))

        for k in sub_occ:
            char_dict = set()
            under_max = True
            for c in k:
                if not c in char_dict:
                    char_dict.add(c)
                    if len(char_dict) > maxLetters:
                        under_max = False
                        break
            if under_max:
                return sub_occ[k]

        return 0
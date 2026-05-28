    class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters_dict = dict()

        for c in range(len(s)):
            if s[c] in letters_dict:
                letters_dict[s[c]][1] = c
            else:
                letters_dict[s[c]] = [c,c]

        p = []
        cur_start = -1
        cur_end = -1
        
        for k,v in letters_dict.items():
            if v[0] < cur_end:
                cur_end = max(cur_end, v[1])
            else:
                if cur_start != -1:
                    p.append(cur_end-cur_start + 1)
                cur_start = v[0]
                cur_end = v[1]
        p.append(cur_end-cur_start + 1)

        return p

        
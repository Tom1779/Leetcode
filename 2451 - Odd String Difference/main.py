class Solution:
    def oddString(self, words):
        diff_dict = {}
        for word in words:
            current_diff = tuple()
            for letter in range(1,len(word)):
                current_diff += ((ord(word[letter])-97)-(ord(word[letter-1])-97),)
            if not current_diff in diff_dict.keys():
                if len(diff_dict.keys()) > 1:
                    return word
                else:
                    diff_dict[current_diff] = [word]
            else:
                diff_dict[current_diff] += [word]
                
        for v in diff_dict.values():
            if len(v) == 1:
                return v[0]
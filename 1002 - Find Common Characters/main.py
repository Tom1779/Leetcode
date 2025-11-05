from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = list(words[0])

        if len(words) == 1:
            return common

        for word in words[1:]:
            common = list((Counter(common) & Counter(list(word))).elements())

        return common
from operator import itemgetter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()

        for char in s:
            if not char in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        new_str = ""

        for k,v in freq.items():
            new_str += k*v

        return new_str
class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        chars = dict()

        for char in s:
            if char not in chars.keys():
                chars[char] = 1
            else:
                chars[char] += 1
        middle = False
        for v in chars.values():
            if v % 2 == 0:
                total += v
            else:
                total += v-1
                middle = True

        if middle:
            total += 1
        return total
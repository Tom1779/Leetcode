class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for c in s[::-1]:
            if c != " ":
                length += 1
            else:
                if length == 0:
                    continue
                return length

        return length
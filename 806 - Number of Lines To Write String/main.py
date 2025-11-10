class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total = 0
        lines = 1

        for char in s:
            if total + widths[ord(char)-97] > 100:
                lines += 1
                total = widths[ord(char)-97]
            else:
                total += widths[ord(char)-97]
            

        return [lines, total]
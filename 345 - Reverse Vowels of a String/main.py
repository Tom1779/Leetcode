class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s_list = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        while(left < right):
            if s_list[left] in vowels and s_list[right] in vowels:
                temp = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = temp
                left += 1
                right -= 1
                continue
            if not s_list[left] in vowels:
                left += 1
            if not s_list[right] in vowels:
                right -= 1

        return "".join(s_list) 
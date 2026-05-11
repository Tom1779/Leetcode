class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        sep = []

        for num in nums:
            sep += list(map(int, str(num)))

        return sep
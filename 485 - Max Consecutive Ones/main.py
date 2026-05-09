class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        cur_ones = 0

        for num in nums:
            if num == 1:
                cur_ones += 1
                continue
            if max_ones < cur_ones:
                max_ones = cur_ones
            cur_ones = 0

        if max_ones < cur_ones:
                max_ones = cur_ones
                
        return max_ones
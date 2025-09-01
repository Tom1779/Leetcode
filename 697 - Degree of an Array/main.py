from collections import Counter

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        items_count = Counter(nums)
        rev_nums = nums[::-1]
        nums_len = len(nums)
        min_degree = 999999

        max_elements = [k for k, v in items_count.items() if v == max(items_count.values())]

        for element in max_elements:
            cur_degree = nums_len - rev_nums.index(element) - nums.index(element)
            if cur_degree == 1:
                return 1
            
            if cur_degree < min_degree:
                min_degree = cur_degree

        return min_degree
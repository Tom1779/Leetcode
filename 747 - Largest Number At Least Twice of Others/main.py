#could've used list sort functions, but it would require more loops, this saves space and time as we only do one pass

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -1
        sec_max_num = -1
        max_ind = 0
        for ind in range(len(nums)):
            if nums[ind] > max_num:
                sec_max_num = max_num
                max_num = nums[ind]
                max_ind = ind
                continue
            if nums[ind] > sec_max_num:
                sec_max_num = nums[ind]
        
        if max_num >= sec_max_num * 2:
            return max_ind
        
        return -1
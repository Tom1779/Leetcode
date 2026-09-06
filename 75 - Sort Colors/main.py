class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sort_nums = []
        for i in range(len(nums)):
            sort_nums.append(min(nums))
            nums.remove(min(nums))
            
        for n in sort_nums:
            nums.append(n)
        
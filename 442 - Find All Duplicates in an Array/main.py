class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        dups = []

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                dups.append(nums[i])
        
        return dups

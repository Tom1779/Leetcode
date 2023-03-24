class Solution:
    def findTheArrayConcVal(self, nums):
        value = 0
        while(len(nums) > 1):
            value += int(str(nums[0]) + str(nums[-1]))
            nums = nums[1:-1]
            
        if(len(nums) == 1):
            value += nums[0]
            
        return value
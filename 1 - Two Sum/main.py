class Solution:
    def twoSum(self, nums, target):
        complement = {}
        for num in range(len(nums)):
            if target - nums[num] in complement.keys():
                return [complement[target - nums[num]][1], num]
            if not nums[num] in complement.keys():
                complement[nums[num]] = [target - nums[num], num]
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = dict()

        for i in range(len(nums)):
            if nums[i] in num_dict:
                return [num_dict[nums[i]], i]
            else:
                num_dict[target-nums[i]] = i
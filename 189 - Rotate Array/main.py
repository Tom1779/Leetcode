class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_dict = dict()

        for i in range(len(nums)):
            num_dict[(i+k)%len(nums)] = nums[i]

        for i in range(len(nums)):
            nums[i] = num_dict[i]

        return nums
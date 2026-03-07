class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_max = max(nums)

        nums_list = []

        for i in range(len(nums)):
            if nums[i] == nums_max:
                nums_list.append(-1)
                continue
            search_index = i + 1
            if search_index == len(nums):
                search_index = 0
            while(nums[search_index] <= nums[i]):
                search_index += 1
                if search_index == len(nums):
                    search_index = 0
                continue
            nums_list.append(nums[search_index])

        return nums_list
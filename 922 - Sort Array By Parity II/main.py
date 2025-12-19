class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []

        for num in range(len(nums)):
            if num % 2 == 0 and nums[num] % 2 != 0:
                even.append(num)
            if num % 2 != 0 and nums[num] % 2 == 0:
                odd.append(num)

        for num in range(len(even)):
            temp = nums[even[num]]
            nums[even[num]] = nums[odd[num]]
            nums[odd[num]] = temp

        return nums

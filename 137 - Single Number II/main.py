class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = dict()

        for num in nums:
            if not num in nums_dict.keys():
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        for key,val in nums_dict.items():
            if val == 1:
                return key
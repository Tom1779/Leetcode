class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_dict = {key:0 for key in range(1,len(nums)+1)}
        errorNums = []

        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] == 2:
                errorNums.append(num)

        for key,val in nums_dict.items():
            if val == 0:
                errorNums.append(key)
                return errorNums
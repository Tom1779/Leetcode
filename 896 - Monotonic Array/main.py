class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True


        index = 1
        inc = -2

        while index < len(nums):
            if nums[index] < nums[index-1]:
                if inc == -2:
                    inc = -1
                elif inc == 1:
                    return False
            elif nums[index] > nums[index-1]:
                if inc == -2:
                    inc = 1
                elif inc == -1:
                    return False
            index += 1
            continue
            

        return True
class Solution:
    def getMinDistance(self, nums, target, start):
        if nums[start] == target:
            return 0
        
        #Begin at the starting point, this way we can return after the first target encounter knowing the difference is the smallest it can be
        left = start - 1
        right = start + 1
        
        while(True):
            if left >= 0:
                if nums[left] == target:
                    return abs(left-start)
                left -= 1
            
            if right < len(nums):
                if nums[right] == target:
                    return abs(right-start)
                right += 1
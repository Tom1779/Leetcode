class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[0:k])
        cur_sum = max_sum

        for i in range(1,len(nums)-k+1):
            cur_sum = cur_sum - nums[i-1] + nums[i+k-1]
            if cur_sum > max_sum:
                max_sum = cur_sum


        return max_sum/k

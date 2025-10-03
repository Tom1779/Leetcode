class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        indices = []

        for num in range(len(self.nums)):
            if self.nums[num] == target:
                indices.append(num)
        return indices[random.randint(0,len(indices)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
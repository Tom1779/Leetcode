import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.shuffled = nums.copy()

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuffled)):
            temp = self.shuffled[i]
            rand = random.randint(0,len(self.shuffled)-1)
            self.shuffled[i] = self.shuffled[rand]
            self.shuffled[rand] = temp

        return self.shuffled



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
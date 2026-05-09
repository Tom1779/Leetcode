import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.w_probs = dict()
        self.w_sum = sum(self.w)
        rang = 0
        for w in range(len(self.w)):
            rang += self.w[w]
            self.w_probs[rang] = w

    def pickIndex(self) -> int:
        rand_w = random.randint(1, self.w_sum)
        for k,v in self.w_probs.items():
            if k >= rand_w:
                return v



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
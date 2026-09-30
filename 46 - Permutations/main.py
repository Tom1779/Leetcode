class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = []

        for num in nums:
            self.get_perms([num], nums, permutations)

        return permutations
    
    def get_perms(self, cur_perm, nums, permutations):
        if len(cur_perm) == len(nums):
            permutations.append(cur_perm)
            return
        for num in nums:
            if num in cur_perm:
                continue
            self.get_perms(cur_perm+[num], nums, permutations)

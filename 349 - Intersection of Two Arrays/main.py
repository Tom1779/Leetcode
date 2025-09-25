class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set()

        for num in nums1:
            if num in nums2:
                inter.add(num)

        return list(inter)
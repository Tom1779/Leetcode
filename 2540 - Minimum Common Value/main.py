class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min1 = 0
        min2 = 0

        while(min1 < len(nums1) and min2 < (len(nums2))):
            if nums1[min1] == nums2[min2]:
                return nums1[min1]
            if nums1[min1] < nums2[min2]:
                min1 += 1
                continue
            else:
                min2 += 1

        return -1
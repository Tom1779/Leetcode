class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        nums1_min = 0
        nums2_min = 0

        inter = []

        while(nums1_min < len(nums1) and nums2_min < len(nums2)):
            if nums1[nums1_min] == nums2[nums2_min]:
                inter.append(nums1[nums1_min])
                nums1_min += 1
                nums2_min += 1
                continue
            if nums1[nums1_min] < nums2[nums2_min]:
                nums1_min += 1
                continue
            if nums2[nums2_min] < nums1[nums1_min]:
                nums2_min += 1
                continue

        return inter
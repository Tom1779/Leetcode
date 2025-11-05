class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ge = []
        for num1 in nums1:
            found = 0
            greater = 0
            for num2 in nums2:
                if num1 == num2:
                    found = 1
                    continue
                if found and num2 > num1:
                    ge.append(num2)
                    greater = 1
                    break
            if not greater:
                ge.append(-1)
        return ge
class Solution:
    def mostFrequentEven(self, nums):
        even_count = {}
        for num in nums:
            if num%2 == 0:
                if not num in even_count.keys():
                    even_count[num] = 1
                else:
                    even_count[num] += 1
        if len(even_count.keys()) == 0:
            return -1
        return max(sorted(even_count), key=even_count.get)
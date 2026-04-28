class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        right_ints = []
        new_int = []

        for arr in range(len(intervals)):
            new_int.append([intervals[arr][0], intervals[arr][1], arr])

        new_int.sort()

        for interval in intervals:
            found = False
            for sorted_int in new_int:
                if interval[1] <= sorted_int[0]:
                    right_ints.append(sorted_int[2])
                    found = True
                    break
            if not found:
                right_ints.append(-1)

        return right_ints